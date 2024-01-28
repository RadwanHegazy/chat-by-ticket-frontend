from django.shortcuts import render, redirect
from globals.request_manager import Action
from frontend.settings import MAIN_URL
from django.contrib import messages

def ClientView (request) :
    context = {}
    
    if request.method == "POST" : 
        action = Action(
            url = MAIN_URL + "/client/create/",
            data = {
                "full_name" : request.POST.get('full_name',None),
                "email" : request.POST.get('email',None),
                "problem" : request.POST.get('problem',None),
            }
        )

        if 'picture' in request.FILES : 
            action.files = {
                'picture' : request.FILES.get('picture')
            }
        
        action.post()

        if action.is_valid(): 
            messages.success(request,"تم ارسال المشكلة بنجاح وسيتم الرد خلال 24 ساعة")
        else:
            messages.error(request,"الرجاء ادخال بيانات صحيحة")
                       
        return redirect('register_client')
        
    return render(request,'client/register.html')