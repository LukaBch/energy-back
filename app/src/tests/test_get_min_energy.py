from django.test import TestCase
from ..use_cases import get_min_total_energy_consumption

class TestGetMinEnergy(TestCase):
    """A class to test the use case get_min_total_energy_consumption"""
    def test_one_from_category_F(self):
        self.assertEqual(
            get_min_total_energy_consumption(selected_appliances=[1]),
            12,
        )
    
    def test_two_from_category_F(self):
        self.assertEqual(
            get_min_total_energy_consumption(selected_appliances=[1, 2]),
            12,
        )
    
    def test_one_from_category_A(self):
        self.assertEqual(
            get_min_total_energy_consumption(selected_appliances=[3]),
            1.5,
        )
    
    def test_one_from_category_L(self):
        self.assertEqual(
            get_min_total_energy_consumption(selected_appliances=[6]),
            2,
        )

    def test_almost_every_applyance_selected(self):
        self.assertEqual(
            get_min_total_energy_consumption(selected_appliances=[1,4,5,7,8]),
            14.9,
        )
    
    def test_every_applyance_selected(self):
        self.assertEqual(
            get_min_total_energy_consumption(selected_appliances=[1,2,3,4,5,6,7,8]),
            13.9,
        )
   