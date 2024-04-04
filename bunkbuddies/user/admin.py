from django.contrib import admin

# Register your models here.
from .models import ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'email', 'created_at','message']
