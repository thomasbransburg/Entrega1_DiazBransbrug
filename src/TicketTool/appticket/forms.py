from django.forms import Form, IntegerField, CharField, DateField, EmailField
from datetime import datetime



#Form to create ticket
class Open_Ticket(Form):
    date_open=DateField()
    description=CharField(max_length=500)
    category=CharField(max_length=150) 
    status=CharField(max_length=150)

class Create_User(Form):
    name=CharField(max_length=150)
    lastname=CharField(max_length=150)
    email=EmailField()
    workid=IntegerField()
class Create_Staff(Form):
    name=CharField(max_length=150)
    lastname=CharField(max_length=150)
    email=EmailField()
    jobtitle=CharField()


