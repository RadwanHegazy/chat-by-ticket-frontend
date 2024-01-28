from django.shortcuts import render, HttpResponse
from django.http import Http404
from globals.request_manager import Action
from frontend.settings import MAIN_URL


def ChatView (request,ticket_id) : 

    user = request.COOKIES.get('user',None)

    
    action = Action(
        url = MAIN_URL + f"/client/ticket/{ticket_id}/",
    )

    if user != None :
        action.headers = {"Authorization" :  f"Bearer {user}"}
    
    action.get()
    
    context = {
        'ticket' : action.json_data()
    }
    if action.is_valid() : 
        return render(request,'chat.html',context)
    else:        
        raise Http404(request)