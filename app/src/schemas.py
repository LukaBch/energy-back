
from ninja import Schema
from typing import List
from pydantic import validator
from .constants import APPLIANCES, MAX_TOTAL_ENERGY_CONSUMPTION
from .use_cases import get_min_total_energy_consumption

class MinTotalEnergyConsumption(Schema):
    selected_appliances: list[int]

    @validator("selected_appliances")
    def selected_appliances_validator(cls, selected_appliances) -> list[int]:
        if len(selected_appliances) == 0:
            raise ValueError("At least 1 appliance selected")
        for selected_appliance in selected_appliances:
            if selected_appliance not in APPLIANCES.keys():
                raise ValueError(f"Appliance id {selected_appliance} invalid")
        return selected_appliances

class EnergyConsumptionsInputSchema(MinTotalEnergyConsumption):
    total_consumption: str
    
    @validator("total_consumption")
    def total_consumption_validator(cls, total_consumption, values) -> str:
        selected_appliances = values.get("selected_appliances", [])
        min_energy = get_min_total_energy_consumption(selected_appliances)
        if float(total_consumption) < min_energy:
            raise ValueError(f"Total consumption {total_consumption} is too small ( < {min_energy} kWh)")
        if float(total_consumption) > MAX_TOTAL_ENERGY_CONSUMPTION:
            raise ValueError(f"Total consumption {total_consumption} is too big ( > {MAX_TOTAL_ENERGY_CONSUMPTION} kWh )")
        
        return total_consumption


class ApplianceSchema(Schema):
    id: int
    category: str
    name: str
    power: float

class BoundariesCategorySchema(Schema):
    min: int
    max: int

class BoundariesSchema(Schema):
    F: BoundariesCategorySchema
    A: BoundariesCategorySchema
    L: BoundariesCategorySchema

class AppliancesAndBoundariesResponseSchema(Schema):
    appliances: List[ApplianceSchema]
    boundaries: BoundariesSchema

class EnergyConsumptionResponseSchema(Schema):
    id: int
    hours: int
    energy: float
    proportion: float

class EnergyConsumptionsResponseSchema(Schema):
    energies: List[EnergyConsumptionResponseSchema]
    total: float