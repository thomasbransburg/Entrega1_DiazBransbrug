from mailbox import NoSuchMailboxError
from django.db import models

# Create your models here.

class User(models.Model): #Usuarios que crean los tickets.
    name=models.CharField(max_length=150)
    lastname=models.CharField(max_length=150)
    email=models.EmailField()
    workid=models.IntegerField(max_length=6)

    def __str__(self):
        return f"{self.workid} - {self.name} {self.lastname}"
class Ticket(models.Model): #Tickets creados por usuarios que resuelven los de IT.
    date_open=models.DateField(blank=True, null=True)
    description=models.CharField(max_length=500)
    category=models.CharField(max_length=150) #Ver si puede haber un dropdown
    status=models.CharField(max_length=150) #Ver si puede haber un dropdown

    def __str__(self):
        return f"{self.category} - {self.status}" #Ver de agregar ID
class Staff(models.Model): #Personal de IT que va a resolver los tickets.
    name=models.CharField(max_length=150)
    lastname=models.CharField(max_length=150)
    email=models.EmailField()
    jobtitle=models.CharField(max_length=150) #Ver si puede haber un dropdown

    def __str__(self):
        return f"{self.jobtitle} - {self.name} {self.lastname}"

