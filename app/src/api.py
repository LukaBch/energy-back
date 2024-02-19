from ninja import NinjaAPI
from .schemas import MinTotalEnergyConsumption, EnergyConsumptionsInputSchema, EnergyConsumptionsResponseSchema
from .use_cases import get_min_total_energy_consumption, get_energy_consumptions

api = NinjaAPI()

@api.post(
    "/min",
    response={200: str},
)
def min_total_energy_consumption_route(request, fields: MinTotalEnergyConsumption):
    return 200, get_min_total_energy_consumption(fields.selected_appliances)


@api.post(
    "/energyconsumptions",
    response={200: EnergyConsumptionsResponseSchema},
)
def energy_consumptions_route(request, fields: EnergyConsumptionsInputSchema):
    res = get_energy_consumptions(
        selected_appliances=fields.selected_appliances, 
        total_consumption=float(fields.total_consumption)
    )
    return 200, res
