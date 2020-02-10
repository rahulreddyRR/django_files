from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse

from django.http import HttpResponseRedirect,HttpResponse
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from basic_app.forms import UserRegisterForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def Register(request):
    register = False
    if request.method == "POST":
        user = UserCreationForm(data=request.POST)
        if user.is_valid():
            form = user.save()
            login(request, form)
            register = True
        else:
            print(UserCreationForm.errors)
    register_form = UserCreationForm()
    return render(request,'register.html',context={'register_form':register_form,'register':register})

def user_login(request):

    if request.method == "POST":
        user = AuthenticationForm(data=request.POST)
        if user.is_valid():
            username= user.cleaned_data.get('username')
            password= user.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                return render(request,'index.html')
            else:
                return HttpResponse('username or password is invaild')
        else:
            return HttpResponse('username or password is invaild')
    else:
        loginform = AuthenticationForm()
        return render(request,'login.html',{'loginform':loginform})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

class index(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    #ListView can auto name Context Dic ex: name of the model with school_list but if you want to control...written down line code
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model = models.School
    template_name = 'basic_app/school_details.html'

class SchoolCreateView(CreateView):
    fields = ['name','principal','location']
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ['name','principal']
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
