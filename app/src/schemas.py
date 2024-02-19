
from ninja import Schema
from typing import List
from pydantic import validator
from .constants import APPLIANCES
from .use_cases import get_min_energy

class MinSchema(Schema):
    selected_appliances: list[int]

    @validator("selected_appliances")
    def selected_appliances_validator(cls, selected_appliances) -> list[int]:
        if len(selected_appliances) == 0:
            raise ValueError("At least 1 appliance selected")
        for selected_appliance in selected_appliances:
            if selected_appliance not in APPLIANCES.keys():
                raise ValueError(f"Appliance id {selected_appliance} invalid")
        return selected_appliances

class EnergyConsumptionsInputSchema(MinSchema):
    total_consumption: str
    selected_appliances: list[int]
    
    @validator("total_consumption")
    def total_consumption_validator(cls, total_consumption, values) -> str:
        selected_appliances = values.get("selected_appliances", [])
        min_energy = round(get_min_energy(selected_appliances),2)
        if float(total_consumption) < min_energy:
            raise ValueError(f"Total consumption {total_consumption} is too small ( < {min_energy} kWh)")
        if float(total_consumption) > 75:
            raise ValueError(f"Total consumption {total_consumption} is too big ( > 75 kWh )")
        
        return total_consumption

class EnergyConsumptionResponseSchema(Schema):
    id: int
    hours: int
    energy: float
    proportion: float

class EnergyConsumptionsResponseSchema(Schema):
    energies: List[EnergyConsumptionResponseSchema]
    total: float