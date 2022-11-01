from django import forms
from Matrix.models import Nazvanie9models







class divan(forms.ModelForm):
    class Meta:
        model = Nazvanie9models

        fields = "__all__"