from django import forms
from .models import *

class GrievanceForm(forms.ModelForm):

    DEPART=(
        (1,'Academics'),
        (0,'Accomodation')
    )
    STATUS=(
        (1,'Solved'),
        (0,'Not Solved')
    )

    name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter Name'}
    ), required=True, max_length=20)
    
    enroll = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter Enrollment no.'}
    ), required=True, max_length=20)
    
    depart = forms.ChoiceField(widget=forms.RadioSelect(), required=True, choices=DEPART)
    
    msg = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Description'}
    ), required=True, max_length=200)
    
    status = forms.ChoiceField(widget=forms.RadioSelect(), choices=STATUS)

    class Meta():
        model = Grievance
        fields = ['name','enroll','depart','msg']