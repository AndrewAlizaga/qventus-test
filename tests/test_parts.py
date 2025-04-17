from fastapi.testclient import TestClient
from app.main import app
from tests.base import BasePartTest, mock_id

client = TestClient(app)

class TestPartEndpoints(BasePartTest):

    def test_post_part(self):
        part_data = {
            "name": "Test Part 2",
            "sku": "TEST1234",
            "description": "Just a mock part",
            "weight_ounces": 10,
            "is_active": True
        }

        response = client.post("/parts/", json=part_data)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == part_data["name"]
        assert data["id"] == mock_id

    def test_get_parts(self):
        response = client.get("/parts/")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert any(p["name"] == "Test Part" for p in data)

    def test_get_part(self):
        response = client.get(f"/parts/{self.fake_part_obj.id}")
        assert response.status_code == 200
        assert response.json()["id"] == self.fake_part_obj.id

    def test_put_part(self):
        updated_data = {
            "name": "Updated Test Part 2",
            "sku": "UPD123",
            "description": "Updated description",
            "weight_ounces": 20,
            "is_active": True
        }

        response = client.put(f"/parts/{self.fake_part_obj.id}", json=updated_data)
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Test Part 2"

    def test_delete_part(self):
        response = client.delete(f"/parts/{mock_id}")
        assert response.status_code == 200
