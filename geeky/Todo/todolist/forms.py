from django import forms
from todolist.models import Todo


class ToDoListForm(forms.ModelForm):
    
    class Meta:
        model = Todo
        fields = ['title','status','priority']


