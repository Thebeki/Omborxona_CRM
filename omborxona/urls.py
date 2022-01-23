from django.contrib import admin
from django.urls import path, include
from ombor_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/', include('app1.urls')),
    path('stats/', include('statistika.urls')),
    path('', HomeView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

