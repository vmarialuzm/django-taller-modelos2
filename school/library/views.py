from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,ListView
from .forms import InputForm
from .models import Book
from .tasks import send_book
import urllib.request
import json
import datetime

class BookView(View):
    def get(self,request):
        url_api = "https://firebasestorage.googleapis.com/v0/b/insta-tecsup-lh-2022-2.appspot.com/o/books_cleaned.json?alt=media&token=2bd5902d-5f98-4d93-ab16-b4927ae3e59b"
        
        response = urllib.request.urlopen(url_api)
        books = json.loads(response.read())
        #lista de objetos(lista de diccionarios)

        for book in books:
            if book["bookID"] != 12224:
                del book["bookID"]
                del book["FIELD13"]

                book["average_rating"] = float(book["average_rating"])
                book["num_pages"] = int(book["num_pages"])
                book["authors"] = book["authors"][:100]

                # m/d/Y -> Y-m-d
                format = book["publication_date"].split("/")
                if len(format)==3:
                    if int(format[1]) > 30:
                        format[1] = 30
                    if int(format[0]) > 12:
                        format[0] = 12
                    book["publication_date"] = datetime.date(int(format[2]),int(format[0]),int(format[1]))
                else:
                    book["publication_date"] = datetime.date(2000,1,1)

                Book.objects.create(**book)

        return render(request,"index.html")

#---------------------------------------------------

class BookList(ListView):
    model = Book
    template_name = 'booklist.html'

class BootstrapEj(View):
    def get(self, request):
        return render(request,'ejemplo_bootstrap.html')
    
#---------------------------------------------------

def select_book(request,id):
    book = Book.objects.get(id=id)
    request.session["authors"] = book.authors
    request.session["id"] = id

    context = {
        "book" : book,
        "form" : InputForm
    }

    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            send_book.delay(name,email)
            return HttpResponse(f"Nombre: {name} \n Email: {email}")

    return render(request,"one-book.html",context)

#---------------------------------------------------

class BookListView(ListView):
    model = Book
    template_name = "booklist.html"
    paginate_by = 20