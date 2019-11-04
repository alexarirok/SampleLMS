from django.shortcuts import render, redirect 
from profiles.models import Profile 
from profiles.forms import ProfileForm, ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def index(request):
    template = 'profiles/index.html'
    profile = Profile.objects.all 
    return render(request, template, {'profile':profile})

def about(request):
    template = 'profiles/about.html'
    return render(request, template, { })

def profile(request):
    template = 'profiles/profile.html'
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProfileForm 
    return render(request, template, {'form':form})

def base(request):
    template = 'profiles/base.html'
    return render(request, template, { })
