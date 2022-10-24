
from fixtures.fixture import *

from students.models import Course, Student


@pytest.mark.django_db
def test_get_course(client, courses):
    # assert False, "Just test example"
    # Course.objects.create(name='fff')
    # Course.objects.create(name='HHH')
    # courses = course_factory(_quantity=2)

    response = client.get('/api/v1/courses/1/')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1


@pytest.mark.django_db
def test_get_list_course(client, courses):

    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_get_id_course(client, course_factory):

    course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()

    for i, obj in enumerate(data):
        any_id = obj['id']
        response_id = client.get(f'/api/v1/courses/?id={any_id}')
        assert response_id.status_code == 200

        data_id = response.json()
        assert data_id[i]['id'] == any_id


@pytest.mark.django_db
def test_get_name_course(client, courses):

    response = client.get(f'/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    for i, obj in enumerate(data):
        any_name = obj['name']
        response_name = client.get(f'/api/v1/courses/?name={any_name}')
        assert response_name.status_code == 200
        data_name = response.json()
        assert data_name[i]['name'] == any_name


@pytest.mark.django_db
def test_create_message(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'python'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_update_course(client, courses):

    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    for i, obj in enumerate(data):
        any_id = obj['id']
        response_id = client.put(f'/api/v1/courses/{any_id}/', data={'name': 'python'})
        assert response_id.status_code == 200
        data_new = response_id.json()

        assert data[i]['name'] != data_new['name']


@pytest.mark.django_db
def test_delete_course(client, courses):

    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data_before = response.json()
    for i, obj in enumerate(data_before):
        any_id = obj['id']
        response_delete = client.delete(f'/api/v1/courses/{any_id}/')
        assert response_delete.status_code == 204
        data_after = client.get('/api/v1/courses/').json()

        assert len(data_before) > len(data_after)


# @pytest.mark.django_db
# def test_delete2_course(client, course_factory):
#     course_factory(_quantity=10)
#     response = client.get('/api/v1/courses/')
#     assert response.status_code == 200
#     data_before = response.json()
#
#     response_delete = client.delete('/api/v1/courses/5/')
#     assert response_delete.status_code == 204
#     data_after = client.get('/api/v1/courses/').json()
#
#     assert len(data_before) > len(data_after)

