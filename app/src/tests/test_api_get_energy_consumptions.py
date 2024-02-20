from django.test import Client, TestCase


class TestAPIGetEnergyConsumptions(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_success(self):
        resp = self.client.post(
            "/api/energyconsumptions",
            data={
              "selected_appliances": [1, 2, 3, 4, 5, 6, 7, 8],
              "total_consumption": "50"
            },
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 200)
    
    def test_fail_empty_selected_appliances(self):
        resp = self.client.post(
            "/api/energyconsumptions",
            data={
              "selected_appliances": [],
              "total_consumption": "50"
            },
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 422)
    

    def test_fail_invalid_appliance(self):
        resp = self.client.post(
            "/api/min",
            data={
              "selected_appliances": [1, 7, 99],
              "total_consumption": "50"
            },
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 422)
    
    def test_fail_too_small(self):
        resp = self.client.post(
            "/api/energyconsumptions",
            data={
              "selected_appliances": [1, 2, 3, 4, 5, 6, 7, 8],
              "total_consumption": "5"
            },
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 422)
    
    def test_fail_too_big(self):
        resp = self.client.post(
            "/api/energyconsumptions",
            data={
              "selected_appliances": [1, 2, 3, 4, 5, 6, 7, 8],
              "total_consumption": "87"
            },
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 422)