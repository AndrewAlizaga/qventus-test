import pytest
from unittest.mock import MagicMock
from app.main import app
from app.db import get_db

mock_id = 999

class BasePartTest:
    def setup_method(self):
        # Fake Part object shared across tests
        self.fake_part_obj = MagicMock()
        self.fake_part_obj.id = 1
        self.fake_part_obj.name = "Test Part"
        self.fake_part_obj.sku = "TEST123"
        self.fake_part_obj.description = "Just a mock part"
        self.fake_part_obj.weight_ounces = 10
        self.fake_part_obj.is_active = True

        def override_get_db():
            db = MagicMock()

            # GET /parts/
            db.query.return_value.offset.return_value.limit.return_value.all.return_value = [self.fake_part_obj]

            # GET /parts/{id}, PUT, DELETE
            db.query.return_value.filter.return_value.first.return_value = self.fake_part_obj

            # POST: simulate ID assignment
            def refresh_stub(obj):
                obj.id = mock_id
            db.refresh.side_effect = refresh_stub
            db.add.return_value = None
            db.commit.return_value = None

            yield db

        app.dependency_overrides[get_db] = override_get_db

