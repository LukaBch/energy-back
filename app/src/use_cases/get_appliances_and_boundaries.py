from ..constants import APPLIANCES, HOURS_CATEGORIES

def get_appliances_and_boundaries():
    return {
      "appliances": [{"id": id, **appliance} for id, appliance in APPLIANCES.items()],
      "boundaries": HOURS_CATEGORIES
    }