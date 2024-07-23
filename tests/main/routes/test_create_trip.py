from tests.settings.conftest2 import client


def test_create_trip(client):
    response = client.post("/trips", json={
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldo@email.com"
    }
                           )
    assert response.status_code == 201
