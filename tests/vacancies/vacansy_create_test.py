from datetime import date

import pytest as pytest


@pytest.mark.django_db
def test_create_vacancy(client, hr_token):
    expected_response = {
        "id": 7,
        "created": date.today().strftime("%Y-%m-%d"),
        "skills": [],
        "text": "random text",
        "slug": "123",
        "status": "draft",
        "min_experience": None,
        "likes": 0,
        "updated_ad": None,
        "user": None
    }

    data = {
        "text": "random text",
        "slug": "123",
        "status": "draft"
    }

    response = client.post(
        "/vacancy/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + hr_token
    )

    assert response.status_code == 201
    assert response.data == expected_response

