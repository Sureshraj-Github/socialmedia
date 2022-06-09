from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def profile(request):
    return render(request,'profile.html')
def document(request):
    return render(request,'document.html')
def view_document(request):
    return render(request,'view_document.html')
def view_table(request):
    return render(request,'view_table.html')