from django.shortcuts import render

# Create your views here.
def indix(request):
    return render(request, 'index.html')

def home(request):
    return 0
