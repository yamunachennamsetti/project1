from django.db import models
class LibraryData(models.Model):
    book_name=models.CharField(max_length=50)
    author_name=models.CharField(max_length=50)
    book_id=models.IntegerField()
    num_of_copies=models.IntegerField()
    book_publisher=models.CharField(max_length=50)

class BorrowBook(models.Model):
    book_id=models.IntegerField()
    member_id=models.IntegerField()
    current_date=models.DateField()
    return_date=models.DateField()

class ReturnBook(models.Model):
    book_id=models.IntegerField()
    member_id=models.IntegerField()
    fine_day=models.DateField()
    fine_amount=models.IntegerField()
# Create your models here.
