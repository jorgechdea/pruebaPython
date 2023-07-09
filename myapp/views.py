from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import License
# Create your views here.

def hello(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("<h1>About</h1>")

def list_license(request):
    licenses = License.objects.all()
    return render(request, 'list_license.html', {"licenses": licenses})

def create_license(request):
    if request.method == 'POST':
        company_name = request.POST.get('companyName')
        user_name = request.POST.get('userName')
        job_title = request.POST.get('jobTitle')
        email = request.POST.get('email')
        software_user_name = request.POST.get('softwareUserName')
        expiration_date = request.POST.get('expirationDate')
        version = request.POST.get('version')

        license = License(
            companyName=company_name,
            userName=user_name,
            jobTitle=job_title,
            email=email,
            softwareUserName=software_user_name,
            expirationDate=expiration_date,
            version=version
        )
        license.save()

        return redirect('/license/')
    else:
        return render(request, 'create_license.html')

def update_license(request, license_id):
    license = get_object_or_404(License, pk=license_id)

    if request.method == 'POST':
        license.companyName = request.POST.get('companyName')
        license.userName = request.POST.get('userName')
        license.jobTitle = request.POST.get('jobTitle')
        license.email = request.POST.get('email')
        license.softwareUserName = request.POST.get('softwareUserName')
        license.version = request.POST.get('version')
        license.expirationDate = request.POST.get('expirationDate')
        license.save()

        return redirect('/license/')
    else:
        return render(request, 'update_license.html', {'license': license})


def delete_license(request, license_id):
    licensedelete = License.objects.get(id=license_id)
    licensedelete.delete()
    return redirect('/license/')