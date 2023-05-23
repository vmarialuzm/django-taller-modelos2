from django import forms
from .models import ClassRoom

class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    start_time = forms.TimeField(widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    last_name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    born_date = forms.DateField(widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    classroom_id = forms.ModelChoiceField(queryset=ClassRoom.objects.all(), widget=forms.Select(attrs={
        "class": "form-control mb-3"
    }))
