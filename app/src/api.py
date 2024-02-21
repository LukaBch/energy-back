from ninja import NinjaAPI
from .schemas import MinTotalEnergyConsumption, EnergyConsumptionsInputSchema, EnergyConsumptionsResponseSchema, AppliancesAndBoundariesResponseSchema
from .use_cases import get_min_total_energy_consumption, get_energy_consumptions, get_appliances_and_boundaries

api = NinjaAPI()

@api.get(
    "/appliances-and-boundaries",
    response={200: AppliancesAndBoundariesResponseSchema},
)
def appliances_and_boundaries_route(request):
    return 200, get_appliances_and_boundaries()

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
