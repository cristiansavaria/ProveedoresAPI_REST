from django import forms
from .models import Proveedor
from django.contrib.auth.forms import UserCreationForm

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    pass