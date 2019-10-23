from django.contrib import admin
from django.urls import path, include
from allez.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('carnival/', include('carnival.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
    path('riders/', include('riders.urls')),

]



