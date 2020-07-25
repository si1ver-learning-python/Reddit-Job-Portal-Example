from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from . models import Application, Job, Candidate


def new_candidate(request, candidate_name):
    Candidate.objects.create(name=candidate_name)
    return redirect("/jobs/")


def new_job(request, job_name, job_desc):
    Job.objects.create(name=job_name, description=job_desc)
    return redirect("/jobs/")


def apply(request, candidate_name, job_name):
    """Apply for a job"""
    candidate = Candidate.objects.get(name=candidate_name)
    job = Job.objects.get(name=job_name)
    Application.objects.create(candidate=candidate, job=job)
    return redirect("/jobs/")


def get_jobs(request, candidate_name):
    """
    :param candidate_name: the candidate's name to get jobs for
    """
    # get the candidate instance
    candidate = Candidate.objects.get(name=candidate_name)
    # get all applications that the candidate has
    applications = Application.objects.filter(candidate=candidate.id)
    # get the job value of applications
    job_ids = applications.values("job")
    # get all jobs that are one of the job ids
    jobs = Job.objects.filter(id__in=job_ids).values()
    return HttpResponse(jobs)

