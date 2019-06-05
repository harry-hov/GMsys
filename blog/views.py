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
	obj = Grievance.objects.all()
	return render(request,'grievances.html', {'obj':obj})

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

def search(request):
    if request.method=='GET':    
        query = request.GET.get('q')
        try:
            query = str(query)
        except TypeError:
            query = None
            results = None
        if query:
            results = Grievance.objects.filter(grievance_id = query)
        return render(request, 'status.html', {"results": results,})

def result(request):
    return render(request, 'results.html')


