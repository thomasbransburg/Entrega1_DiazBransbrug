from django.http import HttpResponse
from django.shortcuts import render
from appticket.models import *
from appticket.forms import *


# Create your views here.
def index(request):
    return render(request, "appticket/index.html")

def users(request):
    users=User.objects.all()
    context={"users":users}
    return render(request, "appticket/user.html",context)

def tickets(request):
    tickets=Ticket.objects.all()
    context={"tickets":tickets}
    return render(request, "appticket/ticket.html", context)

def staff(request):
    staff=Staff.objects.all()
    context={"staff":staff}
    return render(request, "appticket/staff.html", context)

def create_ticket(request):
    if request.method == "GET":
        ticket = Open_Ticket
        return render(request, "appticket/createticket.html", {"ticket": ticket})

    else:
        ticket = Open_Ticket(request.POST)
        
        if ticket.is_valid():
            data = ticket.cleaned_data
            date_open = data.get("date_open")
            description = data.get("description")
            category = data.get("category")
            status = data.get("status")
            new_ticket = Ticket(date_open=date_open, description = description, category = category,status = status )
            new_ticket.save()
            return render(request, "appticket/ticket.html")

        else:
            return HttpResponse("The form for creating the Ticket is not valid. Please try again!")

def search_ticket(request):
    return render(request, "appticket/ticketsearch.html")

def search_ticket_results(request):
    ticket_status = request.GET.get("status",None)

    if not ticket_status:
        return HttpResponse("No status indicated.")
    
    ticket_list = Ticket.objects.filter(status__icontains = ticket_status)  

    return render(request, "appticket/ticketsearch_results.html", {"status_searchs":ticket_list})  

def create_user(request):
    if request.method == "GET":
        user = Create_User
        return render(request, "appticket/createuser.html", {"user": user})

    else:
        user = Create_User(request.POST)
        
        if user.is_valid():
            data = user.cleaned_data
            name = data.get("name")
            lastname = data.get("lastname")
            email = data.get("email")
            workid = data.get("workid")

            new_user = User(name = name, lastname = lastname, email = email, workid = workid  )
            new_user.save()
            return render(request, "appticket/user.html")

        else:
            return HttpResponse("The form for creating the user is not valid. Please try again!")


def create_staff(request):
    if request.method == "GET":
        staff = Create_Staff
        return render(request, "appticket/createstaff.html", {"staff": staff})

    else:
        staff = Create_Staff(request.POST)
        
        if staff.is_valid():
            data = staff.cleaned_data
            name = data.get("name")
            lastname = data.get("lastname")
            email = data.get("email")
            jobtitle = data.get("jobtitle")

            new_staff = Staff(name = name, lastname = lastname, email = email, jobtitle = jobtitle )
            new_staff.save()
            return render(request, "appticket/staff.html")

        else:
            return HttpResponse("The form for creating the staff member is not valid. Please try again!")
