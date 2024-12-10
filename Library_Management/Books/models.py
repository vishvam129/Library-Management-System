from django.db import models
from django.utils.timezone import now

# Create your models here.

from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    copies = models.IntegerField()

    def __str__(self):
        return self.title
    
class Members(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    membership_date = models.DateField(default=now)  

    def __str__(self):
        return self.name
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    borrowed_on = models.DateField(auto_now_add=True)
    due_date = models.DateField(default=now)
    returned_on = models.DateField(null=True, blank=True)
    fine = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return self.book.title + ' - ' + self.member.user.username