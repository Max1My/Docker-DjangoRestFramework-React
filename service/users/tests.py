import json
from pprint import pprint

from django.test import TestCase
from requests.auth import HTTPBasicAuth
from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    force_authenticate,
    APIClient,
    APISimpleTestCase,
    APITestCase, CoreAPIClient
)
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from users.views import ProjectModelViewSet,UserModelViewSet
from users.models import Project
from users.models import User as User_test

class TestProjectViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects')
        view = ProjectModelViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/',
                               {'name':'website','links_repo':'https://github.com/Max1My'},
                               format='json')
        view = ProjectModelViewSet.as_view({'get':'create'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_create_author_for_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/projects/',
                               {'name':'website','links_repo':'https://github.com/Max1My'},
                               format='json')
        admin = User.objects.create_superuser('maximy', 'mksadmin@gmail.com', 'sync')
        force_authenticate(request, admin)
        view = ProjectModelViewSet.as_view({'get': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_detail(self):
        project = Project.objects.create(name='Android',links_repo='https://github.com')
        client = APIClient()
        response = client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_edit_guest(self):
        project = Project.objects.create(name='Android',links_repo='https://github.com')
        client = APIClient()
        response = client.get(f'/api/projects/{project.id}/',{
            'name': 'WebApp',
            'links_repo': 'https://github.com'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('api/users')
        view = UserModelViewSet.as_view({'get':'list'})
        response = view(request)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_get_detail(self):
        user = User_test.objects.create(username='John', first_name='John',last_name='Cena',birthday_year=1998,email='john@gmail.com')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        user = User_test.objects.create(username='John', first_name='John',last_name='Cena',birthday_year=1998,email='john@gmail.com')
        client = APIClient()
        admin = User.objects.create_superuser('maximy', 'mksadmin@gmail.com', 'sync')
        client.login(username='maximy', password='sync')
        response = client.put(f'/api/users/{user.id}/', {
            'username': 'Klane',
            'first_name': 'John',
            'last_name': 'Klane',
            'birthday_year': 1997,
            'email': 'klane@gmail.com'
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User_test.objects.get(id=user.id)
        self.assertEqual(user.username, 'Klane')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Klane')
        self.assertEqual(user.birthday_year, 1997)
        self.assertEqual(user.email, 'klane@gmail.com')
        client.logout()

class TestUsersViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        project = Project.objects.create(name='Android',links_repo='https://github.com')
        user = User_test.objects.create(username='John', first_name='John',last_name='Cena',birthday_year=1998,email='john@gmail.com',project=project)
        admin = User.objects.create_superuser('maximy', 'admin@gmail.com', 'sync')
        self.client.login(username='maximy', password='sync')
        response = self.client.put(f'/api/users/{user.id}/', {'username': 'Klane',
                                                              'first_name': 'John',
                                                              'last_name': 'Klane',
                                                              'birthday_year': 1997,
                                                              'email': 'klane@gmail.com',
                                                              'project': user.project.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User_test.objects.get(id=user.id)
        self.assertEqual(user.username, 'Klane')

    def test_edit_mixer(self):
        test_user = mixer.blend(User_test)
        admin = User.objects.create_superuser('maximy', 'admin@gmail.com', 'sync')



        self.client.login(username='maximy', password='sync')
        response = self.client.put(f'/api/users/{test_user.id}/', {'username': 'Klane',
                                                              'first_name': 'John',
                                                              'last_name': 'Klane',
                                                              'birthday_year': 1997,
                                                              'email': 'klane@gmail.com',
                                                              })
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        test_user = User_test.objects.get(id=test_user.id)
        print(test_user.id,test_user.username)
        self.assertEqual(test_user.username,'Klane')

    def test_auth_coreapi(self):
        client = CoreAPIClient()
        schema = client.get('http://127.0.0.1:8000/schema/')
        client.session.auth = HTTPBasicAuth('user', 'pass')
        client.session.headers.update({'x-test': 'true'})