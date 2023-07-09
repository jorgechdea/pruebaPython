from django.forms import ModelForm
from .models import License

class LicenseForm(ModelForm):
    class Meta:
        model = License
        fields = ['companyName', 'userName', 'jobTitle', 'email', 'softwareUserName', 'expirationDate', 'version']