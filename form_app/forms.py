from django import forms
#from .models import Name
class NameForm (forms.Form):
    First_Name=forms.CharField(label="Enter your first Name",max_length=30)
    Last_Name=forms.CharField(label="Enter your last Name",max_length=30)