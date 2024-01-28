from django.shortcuts import render
from globals.decorators import Action
from globals.decorators import login_required
from frontend.settings import MAIN_URL

@login_required
def GetAllTickets (request) : 
    context = {}

    headers = {
        "Authorization" : f"Bearer {request.COOKIES.get('user')}"
    }

    action = Action(
        url = MAIN_URL + "/client/tickets/all/",
        headers=headers
    )

    action.get()

    context['tickets'] = action.json_data()
    context['ticket_count'] = len(action.json_data())

    return render(request,'employee/home.html',context)

