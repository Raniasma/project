from django.shortcuts import render, redirect
from .forms import MyUserForms
from .models import MyUser
def create_user(request):
    form = MyUserForms(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect ('/crud')
    return render(request,'index.html',{'form':form, 'users':MyUser.objects.all()})
def update_user(request, id):
    id = MyUser.objects.get(id=id)
    form = MyUserForms(request.POST or None, instance=id)
    if form.is_valid():
        form.save()
        return redirect ('/crud')
    return render(request,'index.html',{'form':form, 'users':MyUser.objects.all()})
def delete_user(request, id):
    user = MyUser.objects.get(id=id)
    user.delete()
    return redirect ('/crud')
