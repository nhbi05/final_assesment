from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    # stats
    count_babies = Baby.objects.count()
    count_sitters = Sitter.objects.count()
    count_payments = Payment.objects.count()
    context = {
        "count_babies": count_babies,
        "count_sitters": count_sitters,
        "count_payments": count_payments,
    }
    return render(request, "my_daycare/index.html", context)
#@login_required 

def sitter(request):
    return render(request , 'my_daycare/sitter.html', {
        'sitter':Sitter.objects.all(),
    })

def baby(request):
    return render(request , 'my_daycare/baby.html', {
        'sitter':Baby.objects.all(),
    })

def payment(request):
    return render(request, 'my_daycare/payment.html')

def procurement(request):
    return render(request, 'my_daycare/procurement.html')

#  trying to add babe form
def AddBaby(request):
    if request.method == 'POST':
        form = BabyForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'my_daycare/baby_reg.html', {
                'form': BabyForm(),
                'success': True,
            })
        else:
            print("Form is not valid")
            return render(request, 'my_daycare/baby_reg.html', {
                'form': form,  # Pass the invalid form back to the template
                'success': False,
            })
    else:
        form = BabyForm()
    return render(request, 'my_daycare/baby_reg.html', {
        'form': form
    })


def add_sitter(request):
    form1 = SitterForm(request.POST)
    if request.method == 'POST':
        if form1.is_valid():
            form1.save()
            return render(request, 'my_daycare/sitter_reg.html', {
                'form1': SitterForm(),
                'success': True,
            })
        else:
            print ("Form is not valid")
            return render(request, 'my_daycare/sitter_reg.html', {
              'form1': SitterForm(),
               'success': False,
            })
    else:
        form1 = SitterForm()
        return render(request, 'my_daycare/sitter_reg.html', {
            'form1' : SitterForm()
        })