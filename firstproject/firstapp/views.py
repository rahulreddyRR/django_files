from django.shortcuts import render
from django.http import HttpResponse
from firstapp.models import AccessRecord,Webpage,Topic

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    my_dic = {'access_record':webpage_list}
    return render(request,'index.html',context=my_dic)
