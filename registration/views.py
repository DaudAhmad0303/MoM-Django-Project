from django.shortcuts import render

def index(request):
    name = "Daud Ahmad"
    return render(request,'index.html',{"name":name})

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')