from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'my_daycare/index.html')

@login_required 

def sitter(request):
    return render(request, 'my_daycare/sitter.html')

def baby(request):
    return render(request, 'my_daycare/baby.html')

def payment(request):
    return render(request, 'my_daycare/payment.html')

def procurement(request):
    return render(request, 'my_daycare/peocurement.html')

#  trying to add babe form
def AddBabe(request):
    #addedbabe = Babe.objects.get(id=pk)
    getbabeform = AddBabeForm() 
    BabeForm = AddBabeForm(request.POST)
    if request.method == 'POST':
        if BabeForm.is_valid():
            BabeForm.save()
            return HttpResponseRedirect(reverse('home'))
         
    return render(request,'keshoapp/babe.html',{'getpaymentform' : getbabeform})    
def AddPayment(request):
   getpaymentform = AddPaymentForm()    
   return render(request,'keshoapp/payments.html',{'getpaymentform' : getpaymentform}) 
            