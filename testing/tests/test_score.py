import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


# =========================
# NORMAL CASE
# =========================

def test_TC01_valid_score_gioi(client):
    response = client.get("/score?score=8.5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["score"] == 8.5
    assert data["classification"] == "Giỏi"


def test_TC02_valid_score_kha(client):
    response = client.get("/score?score=7.0")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Khá"


def test_TC03_valid_score_trung_binh(client):
    response = client.get("/score?score=5.5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Trung bình"


def test_TC04_valid_score_yeu(client):
    response = client.get("/score?score=3.0")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Yếu"


# =========================
# BOUNDARY CASE
# =========================

def test_TC05_score_minimum_0(client):
    response = client.get("/score?score=0")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Yếu"


def test_TC06_score_maximum_10(client):
    response = client.get("/score?score=10")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Giỏi"


def test_TC07_score_just_below_5(client):
    response = client.get("/score?score=4.9")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Yếu"


def test_TC08_score_exactly_5(client):
    response = client.get("/score?score=5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Trung bình"


def test_TC09_score_just_below_6_5(client):
    response = client.get("/score?score=6.4")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Trung bình"


def test_TC10_score_exactly_6_5(client):
    response = client.get("/score?score=6.5")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Khá"


def test_TC11_score_just_below_8(client):
    response = client.get("/score?score=7.9")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Khá"


def test_TC12_score_exactly_8(client):
    response = client.get("/score?score=8")

    assert response.status_code == 200

    data = response.get_json()

    assert data["classification"] == "Giỏi"


# =========================
# INVALID DATA
# =========================

def test_TC13_score_less_than_0(client):
    response = client.get("/score?score=-1")

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Score must be between 0 and 10"


def test_TC14_score_greater_than_10(client):
    response = client.get("/score?score=11")

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Score must be between 0 and 10"


def test_TC15_score_not_a_number(client):
    response = client.get("/score?score=abc")

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Score must be a valid number"


# =========================
# EMPTY DATA
# =========================

def test_TC16_empty_score(client):
    response = client.get("/score?score=")

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Score cannot be empty"


def test_TC17_missing_score_parameter(client):
    response = client.get("/score")

    assert response.status_code == 400

    data = response.get_json()

    assert data["error"] == "Score parameter is required"


# =========================
# ERROR HANDLING / SPECIAL VALUE
# =========================

def test_TC18_nan_score_should_be_rejected(client):
    response = client.get("/score?score=nan")

    # NaN không phải điểm hợp lệ.
    # Theo specification phải trả về HTTP 400.
    assert response.status_code == 400