from django.urls import path
from . import views


app_name = 'certificate'


urlpatterns = [
    path ('',views.all_certificate,name="all_certificate")
]
