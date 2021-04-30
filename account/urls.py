from django.urls import path
from .import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('',views.accountlist,name ='accounts'),
    path('users',views.usersList,name ='users'),
    path('login',csrf_exempt(views.loginrequest),name ='login'),
    path('signedusers',views.signedUser,name ='signedusers'),
]