from django import forms
from .models import *

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields =['c_stay','b_firstname','b_lastname','location','parents_name','gender','age','timeIn','timeOut']
        labels ={
            'c_stay': 'baby_id',
            'b_firstname': 'First Name',
            'b_lastname': 'Last Name',
            'location' : 'Location',
            'parents_name': 'Parents Name',
            'gender': 'Gender',
            'age': 'Age',
            'timeIn': 'TimeIn',
            'timeOut': 'TimeOut',
        }