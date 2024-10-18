from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', TemplateView.as_view(template_name='Home.html'), name='home'),  # Home page
    path('about/', TemplateView.as_view(template_name='About.html'), name='about'),  # About page
    path('contact/', TemplateView.as_view(template_name='Contact.html'), name='contact'),  # Corrected to Contact.html
    path('admin/', admin.site.urls),  # Admin panel
    path('djangoapp/', include('djangoapp.urls')),
]
