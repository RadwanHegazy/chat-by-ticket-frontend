from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL

def LoginView (request) : 
    context = {}

    if request.method == "POST" : 
        action = Action(
            url = MAIN_URL + "/employee/login/",
            data = {
                "email" : request.POST.get('email',None),
                "password" : request.POST.get('password',None),
            }
        )

        action.post()

        if action.is_valid() : 
            respones = redirect('home')
            respones.set_cookie('user',action.json_data()['token'])
            return respones
        context['error'] = 'البيانات غير صحيحة'



    return render(request,'employee/login.html',context)


def LogoutView (request) : 
    response = redirect('register_client')
    response.delete_cookie('user')
    return response