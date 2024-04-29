from django.db import models
from django.utils import timezone

# Create your models here.
class Categorystay(models.Model):
    name= models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.name
    
    #the above line 4-5 tells django how our database table should look like in our database
    #we will have a table with one column naed Categorystay
    #line 6-7 is a method that defines how the class Categorystay should be referred to by other classes
    #meaning it will be reffered to by its name self.name it can also be self.gende or self.age


class Baby(models.Model):
        c_stay = models.ForeignKey(Categorystay, on_delete= models.CASCADE,  null= True, blank=True)
        b_firstname = models.CharField(max_length=200, null=True, blank=True)
        b_lastname = models.CharField(max_length=200, null=True, blank=True)
        age = models.IntegerField( null= True, blank=True)
        gender = models.CharField(max_length=10, null=True, blank=True)
        location = models. CharField(max_length=100, null=True, blank=True)
        parents_name = models.CharField(max_length=200, null=True, blank= True )
        timeIn =models.DateTimeField( null =True, blank= True)
        timeOut = models.DateTimeField(null = True, blank=True)
    
        def __str__(self):
            return f'Baby:{self.b_firstname}{self.b_lastname}'

class Sitter(models.Model):
        s_firstname = models.CharField(max_length=200, null=True, blank=True)
        s_lastname = models.CharField(max_length=200, null=True, blank=True)
        s_age = models.IntegerField( null= True, blank=True)
        s_gender = models.CharField(max_length=10, null=True, blank=True)
        s_location = models. CharField( default="Kabalagala",max_length=100, null=True, blank=True)
        s_recommenders_name = models.CharField(max_length=200, null=True, blank= True )
        s_NIN = models.CharField(max_length=200, null=True, blank= True )
        s_educationlevel= models.CharField(max_length=200, null=True, blank= True )
        s_contact= models.CharField(max_length=200, null=True, blank= True )
    
        def __str__(self):
            return self.b_name        

class Payment(models.Model):
     paye = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
     #c_payment = models.ForeignKey(Categorystay,on_delete=models.CASCADE, null = True, blank=True)#linking
     amount= models.FloatField(null= True, blank = True)
     pay_no= models.IntegerField( null=True, blank=True)
     currency = models.CharField(default="Ugx", blank=True, null = True,max_length=10)

     def __str__(self):
          return self.pay_no

class Procurement(models.Model):
     paye = models.ForeignKey(Baby, on_delete=models.CASCADE, null=True, blank=True)
     items= models.IntegerField(null= True, blank = True)
     amount= models.IntegerField( null=True, blank=True)
     currency = models.CharField(default="Ugx", blank=True, null = True,max_length=10)

     def __str__(self):
          return f'Item:{self.items}{self.currency}'