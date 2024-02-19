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

    # def test_only_category_A(self):
    #     self.assertEqual(
    #         compute_hour_consumptions(
    #             energy_A=2,
    #             energy_F=0,
    #             energy_L=0,
    #             max_energy_consumption=17,
    #         ),
    #         {
    #             "F": 0,
    #             "A": 4,
    #             "L": 0,
    #         },
    #     )
    
    # def test_only_category_F(self):
    #     self.assertEqual(
    #         compute_hour_consumptions(
    #             energy_A=0,
    #             energy_F=4,
    #             energy_L=0,
    #             max_energy_consumption=73,
    #         ),
    #         {
    #             "F": 8,
    #             "A": 0,
    #             "L": 0,
    #         },
    #     )
    
    # def test_only_category_F_bis(self):
    #     self.assertEqual(
    #         compute_hour_consumptions(
    #             energy_A=0,
    #             energy_F=4,
    #             energy_L=0,
    #             max_energy_consumption=30,
    #         ),
    #         {
    #             "F": 7,
    #             "A": 0,
    #             "L": 0,
    #         },
    #     )
    
    # def test_two_categories(self):
    #     self.assertEqual(
    #         compute_hour_consumptions(
    #             energy_A=2.5,
    #             energy_F=0,
    #             energy_L=0.2,
    #             max_energy_consumption=6,
    #         ),
    #         {
    #             "F": 0,
    #             "A": 2,
    #             "L": 5,
    #         },
    #     )
