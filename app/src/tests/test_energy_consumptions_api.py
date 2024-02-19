from django.test import Client, TestCase


class UpdateDraftInformationAPI(TestCase):
    """Test of update draft information API."""

    def setUp(self):
        self.client = Client()

    def test_update_success(self):
        resp = self.client.post(
            "/api/min",
            data={
              "selected_appliances": [1, 2, 3, 4, 5, 6, 7, 8]
            },
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 200)
        # print(resp.content)