from django.urls import path
from appticket.views import *

urlpatterns = [
    path("homepage/", index, name="homepage"),
    path("users/", users, name="users"),
    path("tickets/", tickets, name="tickets"),
    path("staff/", staff, name="staff"),
    path("createticket/", create_ticket, name="createticket"),
    path("ticketsearch_results/",search_ticket_results, name ="ticketsearch_results"),
    path("ticketsearch/",search_ticket, name ="ticketsearch"),
    path("createuser/",create_user, name ="createuser"),
    path("createstaff/",create_staff, name ="createstaff")
]