from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'firstapp/index.html')

def form_name_view(request):
    #here form is used to pass the data to html page
    form = forms.FormName()
    if request.method=='POST':
        #here down form is used to check valid and this bring data 
        form = forms.FormName(request.POST)
        if form.is_valid():
            #Do somethings codeing
            print("Validation successful")
            print("Name :",form.cleaned_data['name'])
            print("Name :",form.cleaned_data['email'])
            print("Name :",form.cleaned_data['text'])

    return render(request,'firstapp/basic_form.html',{'form':form})
