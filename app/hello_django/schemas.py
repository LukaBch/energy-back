
from ninja import Schema
from typing import List

class HelloWorldSchema(Schema):
    message: str

class MinSchema(Schema):
    selected_appliances: list[int]

class EnergyConsumptionsSchema(Schema):
    total_consumption: str
    selected_appliances: list[int]

class EnergyConsumptionsSchema(Schema):
    id: int
    hours: int
    energy: float
    proportion: float

class EnergyConsumptionsResponseSchema(Schema):
    energies: List[EnergyConsumptionsSchema]
    total: float