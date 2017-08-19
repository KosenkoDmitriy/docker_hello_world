from __future__ import absolute_import, unicode_literals

from dddp.api import API, Collection, Publication
from JON import models

class Program(Collection):
    model = models.Program

class Project(Collection):
    model = models.Project

class Programs(Publication):
    queries = [
        models.Program.objects.all(),
    ]

class Projects(Publication):
    queries = [
        models.Project.objects.all(),
    ]


API.register([
    Program,
    Project,
    Programs,
    Projects,
])