from django.test import TestCase
from JON.models import Project

class ProjectTest(TestCase):

    def setUp(self):
        Project.objects.create(name='Project1', is_active=True)
        Project.objects.create(name='Project2', is_active=False)

    def test_project(self):
        prj1 = Project.objects.get(name='Project1')
        prj2 = Project.objects.get(name='Project2')
        self.assertTrue(prj1.is_active,msg="prj1 is active")
        self.assertFalse(prj2.is_active,msg="prj2 is inactive")