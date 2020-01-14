from django.shortcuts import render
#from firstapp.models import User
from firstapp.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request,'firstapp/index.html')

def user(request):
    #to recive data from DB
    #user_list = User.objects.order_by('First_name')
    #my_dic={"user":user_list}
#-------------------------------------------------------
    form = NewUserForm()

    if request.method == "POST":
        form=NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error")


    return render(request, 'firstapp/users.html',{'form':form})
