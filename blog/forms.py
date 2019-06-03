from django import forms
from .models import *

class GrievanceForm(forms.ModelForm):

    '''
    DEPART=(
        ('Academics','Academics'),
        ('Hostel','Accomodation'),
    )
    STATUS=(
        ('Solved','Solved'),
        ('Not Solved','Not Solved')
    )
    '''
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter Name'}
    ), required=True, max_length=20)
    
    enroll = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Enter Enrollment no.'}
    ), required=True, max_length=20)
    
    #depart = forms.CharField(required=True, choices=DEPART)
    
    msg = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Description'}
    ), required=True, max_length=200)
    
    #status = forms.CharField(choices=STATUS)

    class Meta():
        model = Grievance
        fields = ['name','enroll','depart','msg']