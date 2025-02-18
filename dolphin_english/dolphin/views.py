from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginUserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import auth
# Create your views here.
def home(request):
    # in ra xin chao
    return render(request, 'dolphin/base.html')

def gramma_view(request):
    return render(request, 'dolphin/grammar.html')

def listen_view(request):
    topics = [
        {
            "title": "Short Stories", 
            "levels": "A1-C1", 
            "lessons": 289, 
            "image": "dolphin/img/short-stories.jpg",
        },

        {
            "title": "Conversations", 
            "levels": "A1-B1", 
            "lessons": 100, 
            "image": "dolphin/img/conversations.jpg", 
        },
            
        {
            "title": "TOEIC Listening", 
            "levels": "A2-C1", 
            "lessons": 600, 
            "image": "dolphin/img/toeic.jpg", 
        },
        
        {
            "title": "IELTS Listening", 
            "levels": "B1-C2", 
            "lessons": 328, 
            "image": "dolphin/img/ielts.jpg", 
        },

        {
            "title": "TOEFL Listening", 
            "levels": "B1-C2", 
            "lessons": 54, 
            "image": "dolphin/img/toefl.jpg", 
        },
        
        {
            "title": "IPA", 
            "levels": "A1", 
            "lessons": 42, 
            "image": "dolphin/img/ipa.jpg", 
         },
        
        {
            "title": "Numbers", 
            "levels": "A1", 
            "lessons": 9, 
            "image": "dolphin/img/numbers.jpg", 
        },
        
        {
            "title": "Spelling Names", 
            "levels": "A1", 
            "lessons": 6, 
            "image": "dolphin/img/spelling-names.jpg", 
         },
    ]
    return render(request, 'dolphin/listen.html', {'topics': topics})

def login_view(request):
    form = LoginUserForm()
    if request.method=="POST":
        form = LoginUserForm(request, request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("home")
    context = {'loginform': form}
    return render(request, 'dolphin/login.html', context=context)


def register_view(request):
    if request.method == 'POST':
        forms = CreateUserForm(request.POST)
        if forms.is_valid():
            user = forms.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user) 
            return redirect('home')
        else:
            for error in list(forms.errors.values()):
                print(request, error)
    else:
        forms = CreateUserForm()
    
    context = {'registerform': forms}
    return render(request, 'dolphin/register.html', context=context)

def logout_view(request):
    logout(request)
    return redirect('home')