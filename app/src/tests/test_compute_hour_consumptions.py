from django.test import TestCase
from ..use_cases import compute_hour_consumptions


class TestComputeHourConsumptions(TestCase):
    """A class to test the use case compute_hour_consumptions"""

    def test_1(self):
        self.assertEqual(
            compute_hour_consumptions(
                selected_appliances=[7, 8],
                max_energy_consumption=2,
            ),
            {
                1: 0,
                2: 0,
                3: 0,
                4: 0,
                5: 0,
                6: 0,
                7: 4,
                8: 2,
            },
        )
    
    def test_2(self):
        self.assertEqual(
            compute_hour_consumptions(
                selected_appliances=[3, 4, 5],
                max_energy_consumption=1.6,
            ),
            {
                1: 0,
                2: 0,
                3: 1,
                4: 0,
                5: 0,
                6: 0,
                7: 0,
                8: 0,
            },
        )
    
    def test_3(self):
        self.assertEqual(
            compute_hour_consumptions(
                selected_appliances=[3, 4, 5],
                max_energy_consumption=2.7,
            ),
            {
                1: 0,
                2: 0,
                3: 0,
                4: 1,
                5: 0,
                6: 0,
                7: 0,
                8: 0,
            },
        )
