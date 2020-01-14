from django import forms
from firstapp.models import User

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ['First_name','Last_name','Email']
