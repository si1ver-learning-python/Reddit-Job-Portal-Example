from django.urls import path
from . import views


urlpatterns = [
    path("newcandidate/<str:candidate_name>/", views.new_candidate),
    path("newjob/<str:job_name>/<str:job_desc>/", views.new_job),
    path("apply/<str:candidate_name>/<str:job_name>/", views.apply),
    path("<str:candidate_name>/", views.get_jobs)
]