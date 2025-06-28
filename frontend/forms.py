from django import forms
from .models import CreateTodoModel

class createTodoForm(forms.ModelForm):
    
    class Meta:
        model = CreateTodoModel
        fields = "__all__"
