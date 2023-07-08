from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import License
# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def list_license(request):
    licenses = License.objects.all()
    return render(request, 'list_license.html', {"licenses": licenses})

def create_license(request):
    license = License(companyName=request.POST['companyName'], userName=request.POST['userName'], jobTitle=request.POST['jobTitle'], email=request.POST['email'], softwareUserName=request.POST['softwareUserName'], expirationDate=request.POST['expirationDate'], version=request.POST['version'] )
    license.save()
    return redirect('/license/')

def delete_license(request, license_id):
    licensedelete = License.objects.get(id=license_id)
    licensedelete.delete()
    return redirect('/license/')