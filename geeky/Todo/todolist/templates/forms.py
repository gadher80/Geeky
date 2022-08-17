from socket import fromshare
from django import forms


class signupRegistrations(forms.Form):

    Name = forms.CharField()
    Email= forms.EmailField()

