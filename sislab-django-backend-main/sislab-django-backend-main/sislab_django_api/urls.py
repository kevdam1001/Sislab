from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('GitHub/sislab-django-backend/admin/', admin.site.urls),
    path('GitHub/sislab-django-backend/sislab/', include('requests.urls'))
]
