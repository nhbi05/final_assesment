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
        'babies':Sitter.objects.all(),
    })

def baby(request):
    return render(request, 'my_daycare/baby.html')

def payment(request):
    return render(request, 'my_daycare/payment.html')

def procurement(request):
    return render(request, 'my_daycare/procurement.html')

#  trying to add babe form
def AddBaby(request):
    BabeForm = BabyForm(request.POST)
    if request.method == 'POST':
        if BabeForm.is_valid():
            BabeForm.save()
            return render(request, 'my_daycare/baby_reg.html', {
                'form': BabyForm(),
                'success': True,
            })
        else:
            print ("Form is not valid")
            return render(request, 'my_daycare/baby_reg.html', {
              'form': BabyForm(),
               'success': False,
            })
    else:
        form = BabyForm()
        return render(request, 'my_daycare/baby_reg.html', {
            'form' : BabyForm()
        })


def add_sitter(request):
    message = None

    if request.method == "POST":
        s_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        age = request.POST["age"]
        gender = request.POST["gender"]

        student_obj = Sitter(
            s_name=s_name,
            last_name=last_name,
            email=email,
            age=age,
            gender=gender,
        )
        student_obj.save()
        message = "Sitter added successfully"
        return redirect('sitter_reg')  # Redirect to the add_student page after adding a student

    context = {"message": message}
    return render(request, "my_daycare/sitter_reg.html", context)