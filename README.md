# How to use:
1) Start django server.
2) Migrate database.
3) Go to /jobs/, which will show a 404 with the available links.
4) Create a new candidate object at /jobs/newcandidate/<str:candidate_name>/, where <str:candidate_name> is the name.
5) Create a new job object at /jobs/newjob/<str:job_name>/<str:job_desc>/, where <str:job_name> and <str:job_desc> is the name and description.
6) Apply a candidate for a job at /jobs/apply/<str:candidate_name>/<str:job_name>/, where <str:candidate_name> is candidate name and <str:job_name> is the job name.
7) View all jobs that a candidate has applied for at /jobs/<str:candidate_name>/, where <str:candidate_name> is the candidate's name.
