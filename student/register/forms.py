from django.db import models
from django import forms
from .models import Detail

class infor(forms.ModelForm):

    class Meta:
        model=Detail
        fields='__all__'