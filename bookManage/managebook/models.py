
from django.db import models
# Create your models here.
class Author(models.Model):
    AuthorID = models.CharField(max_length = 100)
    Name = models.CharField(max_length = 100)
    Age = models.IntegerField()
    Country = models.CharField(max_length = 100)

class Book(models.Model):
    ISBN = models.CharField(max_length = 100)
    Title = models.CharField(max_length = 100)
    AuthorID = models.CharField(max_length = 100)
    Publisher = models.CharField(max_length = 100)
    PublishDate = models.DateField()
    Price = models.FloatField()

# Create your models here.
