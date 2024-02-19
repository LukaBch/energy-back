
from ninja import Schema
from typing import List

class HelloWorldSchema(Schema):
    message: str

class MinSchema(Schema):
    selected_appliances: list[int]

class EnergyConsumptionsSchema(Schema):
    total_consumption: str
    selected_appliances: list[int]

class EnergyConsumptionResultSchema(Schema):
    id: int
    hours: int
    energy: float
    proportion: float

class TotoResultsSchema(Schema):
    energies: List[EnergyConsumptionResultSchema]
    total: float