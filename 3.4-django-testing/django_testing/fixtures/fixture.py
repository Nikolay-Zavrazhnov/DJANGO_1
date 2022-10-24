
import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker


from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user('admin')


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def courses(course_factory):
    return course_factory(_quantity=10)