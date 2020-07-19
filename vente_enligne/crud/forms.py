from django import forms
from .models import MyUser
class MyUserForms(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['name','email','password']
