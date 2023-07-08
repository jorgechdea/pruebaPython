from django.urls import path
from .views import list_license, create_license, delete_license
urlpatterns = [
    path('', list_license),
    path('new_license/', create_license, name="create_license"),
    path('delete_license/<int:license_id>/', delete_license, name="delete_license")

]