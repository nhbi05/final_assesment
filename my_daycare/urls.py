from django.urls import path
from my_daycare import views
#accessing the functionality of login view inbuilt iin django to correspond to line 13
from django.contrib.auth import views as auth_views

urlpatterns =[
    path('',views.index,name="index"),
    path('baby/',views.baby,name="baby"),
    path('babe/',views.AddBabe,name="AddBabe"),
    path('sitter/',views.sitter,name="sitter"),
    path('payment/',views.AddPayment,name="payment"),
    path('payment/',views.payment,name="payment"),
    path('login/',auth_views.LoginView.as_view(template_name="my_daycare/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="my_daycare/logout.html"),name="logout"),
]