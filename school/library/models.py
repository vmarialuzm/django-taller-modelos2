from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=400)
    authors = models.CharField(max_length=120)
    average_rating = models.FloatField()
    isbn = models.CharField(max_length=100)
    isbn13 = models.CharField(max_length=100)
    language_code = models.CharField(max_length=20)
    num_pages = models.IntegerField()
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=400)

    class Meta:
        db_table="library_books"

    
