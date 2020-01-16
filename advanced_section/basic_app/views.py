from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from . import models
# Create your views here.

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
