from datetime import date
import pytest


@pytest.mark.django_db
def test_retrieve_vacancy(client, vacancy, hr_token):
    expected_response = {
        "id": vacancy.pk,
        "created": date.today().strftime("%Y-%m-%d"),
        "skills": [],
        "text": "test text",
        "slug": "test",
        "status": "draft",
        "min_experience": None,
        "likes": 0,
        "updated_ad": None,
        "user": vacancy.user_id
    }

    response = client.get(
        f"/vacancy/{vacancy.pk}/",
        HTTP_AUTHORIZATION="Token " + hr_token
    )

    assert response.status_code == 200
    assert response.data == expected_response
