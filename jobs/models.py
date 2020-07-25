from django.db.models import *


class Candidate(Model):
    name = CharField(max_length=50, unique=True)


class Job(Model):
    name = CharField(max_length=50)
    description = TextField()


class Application(Model):
    candidate = ForeignKey(Candidate, on_delete=CASCADE)
    job = ForeignKey(Job, on_delete=CASCADE)
