from django.contrib import admin
from django.urls import path, include
import jobs.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobs/', include(jobs.urls))
]
