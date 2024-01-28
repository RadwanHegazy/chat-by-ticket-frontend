from django.urls import path 
from .views.chat.chat import ChatView
from .views.employee import auth, get 
from .views.client import create



urlpatterns = [
    path("client/register/",create.ClientView,name='register_client'),
    path('',get.GetAllTickets,name='home'),
    path('ticket/<str:ticket_id>/',ChatView,name='ticket'),
    path('login/',auth.LoginView,name='login'),
    path('logout/',auth.LogoutView,name='logout'),
]
