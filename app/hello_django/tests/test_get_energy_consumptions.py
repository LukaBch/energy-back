from django.test import TestCase
from ..use_cases import get_energy_consumptions

class TestGetEnergyConsumptions(TestCase):
    """A class to test the use case get_energy_consumptions"""

    def test_one_from_category_F(self):
        expected_result = {
            "energies": [
                {'id': 1, 'hours': 8, 'energy': 16, 'proportion': 100},
                {'id': 2, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 3, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 4, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 5, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 6, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 7, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 8, 'hours': 0, 'energy': 0, 'proportion': 0},
            ],
            "total": 16
        }

        self.assertEqual(
            get_energy_consumptions(selected_appliances=[1], total_consumption=30),
            expected_result,
        )
    
    def test_example1(self):
        expected_result = {
            "energies": [
                {'id': 1, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 2, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 3, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 4, 'hours': 1, 'energy': 2.5, 'proportion': 41.67},
                {'id': 5, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 6, 'hours': 0, 'energy': 0, 'proportion': 0},
                {'id': 7, 'hours': 19, 'energy': 1.9, 'proportion': 31.67},
                {'id': 8, 'hours': 2, 'energy': 1.6, 'proportion': 26.67},
            ],
            "total": 6
        }

        self.assertEqual(
            get_energy_consumptions(selected_appliances=[4, 7, 8], total_consumption=6),
            expected_result,
        )
