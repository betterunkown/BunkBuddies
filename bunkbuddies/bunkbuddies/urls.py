
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # Other URL patterns...
  
     path('user/', include('user.urls')),
    # Assuming you have an app named 'myapp'
]

# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
