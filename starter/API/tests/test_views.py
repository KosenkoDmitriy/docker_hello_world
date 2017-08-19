from django.test import TestCase, Client
# from django.urls import reverse # django 1.10
from django.core.urlresolvers import reverse  # django 1.9
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from JON.models import Project
from django.contrib.auth.models import User

from API.serializers import ProjectSerializer
import json

# initialize the APIClient app
user, is_new_user = User.objects.get_or_create(username='test', password='123')
# token, is_new_token = Token.objects.get_or_create(user=user)
client = APIClient()
# client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
client.force_authenticate(user=user)
# schema = client.get(reverse('docs'))
schema = client.get('http://localhost:8000/schema')


class ProjectTest(TestCase):
    def setUp(self):
        Project.objects.create(name='Project1', is_active=True)
        Project.objects.create(name='Project2', is_active=False)
        Project.objects.create(name='Project3', is_active=True)
        Project.objects.create(name='Project4', is_active=False)

    def test_create_project(self):
        prj_name = 'Project New'
        prj_tags = ['tag1','tag2']
        params = {'name': prj_name, 'is_active': 'true', 'tags': prj_tags}
        path = reverse('project_list')
        response = client.post(path, data=params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        items = Project.objects.filter(name=prj_name)
        self.assertEqual(items.count(), 1)
        self.assertEqual(items[0].name, prj_name)
        tags = [tag for tag in items[0].tags.names()]
        self.assertListEqual(tags, prj_tags)

    def test_get_all_projects(self):
        response = client.get(reverse('project_list'))
        list = Project.objects.all()
        serializer = ProjectSerializer(list, many=True)
        self.assertEqual(response.data["count"], list.count())
        # self.assertEqual(response.data["results"][0], serializer.data) # check why is_active field converted to isActive
        # self.assertEqual(response.data, serializer.data)
        # self.assertEqual(response.content, serializer.data) # content in json
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_project(self):
        item = Project.objects.first()
        response = client.get(reverse('project_detail', kwargs={'pk': item.pk}))
        serializer = ProjectSerializer(item)
        self.assertEqual(response.data, serializer.data)

    def test_patch_project(self):
        item = Project.objects.first()
        prj_name = 'Patched Project'
        prj_text = 'Putted text'
        params = {"name": prj_name}
        path = reverse('project_detail', kwargs={'pk':item.pk})
        response = client.patch(path, data=params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Project.objects.filter(name=prj_name).count(), 1)
        self.assertEqual(Project.objects.filter(name=prj_name)[0].name, prj_name)

    def test_put_project(self):
        item = Project.objects.first()
        prj_name = 'Putted Project'
        prj_text = 'Putted text'
        prj_tags = ['tag1','tag2']
        params = {"name": prj_name, 'text': prj_text, "tags": prj_tags}
        path = reverse('project_detail', kwargs={'pk':item.pk})
        response = client.put(path, data=params, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item_after = Project.objects.get(pk=item.pk)
        item_tags_after = [tag for tag in item_after.tags.names()]
        self.assertEqual(item_after.name, prj_name)
        self.assertEqual(item_after.text, prj_text)
        self.assertEqual(item_tags_after, prj_tags)
