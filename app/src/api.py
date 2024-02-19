from ninja import NinjaAPI
from .schemas import MinSchema, EnergyConsumptionsInputSchema, EnergyConsumptionsResponseSchema
from .use_cases import get_min_energy, get_energy_consumptions

api = NinjaAPI()

@api.post(
    "/min",
    response={200: str},
)
def min_route(request, fields: MinSchema):
    return 200, str(get_min_energy(fields.selected_appliances))


@api.post(
    "/energyconsumptions",
    response={200: EnergyConsumptionsResponseSchema},
)
def energyconsumptions_route(request, fields: EnergyConsumptionsInputSchema):
    res = get_energy_consumptions(
        selected_appliances=fields.selected_appliances, 
        total_consumption=float(fields.total_consumption)
    )
    return 200, res
