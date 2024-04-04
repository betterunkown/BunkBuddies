
from django.urls import path
from .views import contact_submit

urlpatterns = [
    # Other URL patterns specific to your app...
    path('contact_submit/', contact_submit, name='contact_submit'),
]

