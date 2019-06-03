from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *

# Create your views here.
def home(request):
	return render(request,'index.html')

def about(request):
	return render(request,'about.html')

def contributors(request):
	return render(request,'contributors.html')

def status(request):
	return render(request,'status.html')

def grievances(request):
	return render(request,'grievances.html')

def medium(request):
	return render(request, 'gitCard/medium.html')

def submitGrievance(request):
    if request.method=='POST':
        form = GrievanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/submit/')
    else:
        form = GrievanceForm()
    return render(request, 'submit.html', {'form':form})