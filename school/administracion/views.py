from django.shortcuts import redirect,render
from .models import ClassRoom,Student
from django.views.generic import TemplateView,FormView,View
from .forms import ClassRoomForm,StudentForm

class AdministracionView(TemplateView):
    template_name = "administracion/index.html"
    extra_context = {"classrooms": ClassRoom.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classrooms"] = ClassRoom.objects.all()
        return context
    
class ClassRoomCreate(FormView):
    model = ClassRoom
    template_name = "administracion/create.html"
    form_class = ClassRoomForm

    def form_valid(self,form):
        ClassRoom.objects.create(**form.cleaned_data)
        return redirect("index")
    
def deleteClassRoom(request,id):
    classroom = ClassRoom.objects.get(id=id)
    classroom.delete()
    return redirect("index")

#----------------------TAREA----------------------

def vista1(request):
    context={
        "name":"Luz",
        "edad":26
    }
    return render(request,"administracion/vista1.html",context)

class Vista2(View):

    def get(self,request):
        context = {
            "name":"Luz",
            "lista_numeros":[1,2,3,4]
        }
        return render(request,"administracion/vista2.html",context)
    
# clase que permite crear un nuevo estudiante

class StudentCreate(FormView):
    model = Student
    template_name = "administracion/create_student.html"
    form_class = StudentForm

    def form_valid(self,form):
        Student.objects.create(**form.cleaned_data)
        return redirect("index")
    
# clase que permite ver los datos por estudiante

def obtenerStudent(request,first_name):
    student = Student.objects.get(first_name=first_name)
    context={
        "student":student
    }
    return render(request,"administracion/student.html",context)