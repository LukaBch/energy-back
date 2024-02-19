from ninja import NinjaAPI, Router
from .schemas import MinSchema, EnergyConsumptionsSchema, EnergyConsumptionsResponseSchema
from .use_cases import get_min_energy, get_energy_consumptions

api = NinjaAPI()

hello_router = Router()

api.add_router("hello/", hello_router)
# test

@hello_router.post(
    "/min",
    response={200: str},
)
def min_route(request, fields: MinSchema):
    return 200, str(get_min_energy(fields.selected_appliances))


@hello_router.post(
    "/energyconsumptions",
    response={200: EnergyConsumptionsResponseSchema},
)
def energyconsumptions_route(request, fields: EnergyConsumptionsSchema):
    return 200, get_energy_consumptions(selected_appliances=fields.selected_appliances, total_consumption=float(fields.total_consumption))
