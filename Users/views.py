from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} Account has been created. Now you are able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'Users/register.html',{'form':form})
