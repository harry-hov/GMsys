from django import forms
from .models import *

class GrievanceForm(Forms.ModelForm):
    name = forms.CharField()
    enroll = forms.CharField()
    depart = forms.BooleanField()
    msg = forms.CharField()
    status = forms.BooleanField()

    class Meta():
        model = Grievance
        fields = ['name', 'enroll', 'depart', 'msg']