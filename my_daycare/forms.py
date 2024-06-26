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

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields =['s_firstname','s_lastname','s_location','s_recommenders_name','s_gender','s_age','s_NIN','s_educationlevel', 's_contact']
        labels = {
            's_firstname' : 'First Name',
            's_lastname' : 'Last Name',
            's_location': 'Location',
            's_recommenders_name': 'Recommenders Name',
            's_gender' : 'Gender',
            's_age': 'Age',
            's_NIN': 'Nin',
            's_educationlevel': 'Education Level', 
            's_contact' : 'Contact',
        }