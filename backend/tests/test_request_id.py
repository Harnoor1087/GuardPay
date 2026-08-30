from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_request_id_is_generated():

    response = client.get("/health")

    assert response.status_code == 200

    request_id = response.headers.get("X-Request-ID")

    assert request_id is not None
    assert len(request_id) > 0


def test_client_request_id_is_preserved():

    request_id = "test-request-123"

    response = client.get(
        "/health",
        headers={
            "X-Request-ID": request_id,
        },
    )

    assert response.status_code == 200
    assert response.headers["X-Request-ID"] == request_id

def test_request_id_length_is_bounded():

    request_id = "a" * 500

    response = client.get(
        "/health",
        headers={
            "X-Request-ID": request_id,
        },
    )

    assert response.status_code == 200

    returned_id = response.headers["X-Request-ID"]

    assert len(returned_id) <= 128


def test_request_id_with_newline_is_not_accepted():

    request_id = "valid-request-id\ninjected-log-entry"

    response = client.get(
        "/health",
        headers={
            "X-Request-ID": request_id,
        },
    )

    assert response.status_code == 200

    returned_id = response.headers["X-Request-ID"]

    assert "\n" not in returned_id
    assert "\r" not in returned_id