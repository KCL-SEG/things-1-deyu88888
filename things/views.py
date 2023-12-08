from django.shortcuts import render
# from things import views

# Create your views here.

def home(request):
    return render(request, 'things.html')