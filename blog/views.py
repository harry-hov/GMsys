from django.shortcuts import render

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