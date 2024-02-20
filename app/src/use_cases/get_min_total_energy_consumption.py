from ..constants import APPLIANCES, HOURS_CATEGORIES

def get_min_total_energy_consumption(selected_appliances):
    selected_powers = {category: [] for category in HOURS_CATEGORIES.keys()}

    for appliance_id in selected_appliances:
        category = APPLIANCES[appliance_id]["category"]
        power = APPLIANCES[appliance_id]["power"]
        selected_powers[category].append(power)

    res = 0
    for category in HOURS_CATEGORIES.keys():
        res += min(selected_powers[category]) * HOURS_CATEGORIES[category]["min"] if len(selected_powers[category]) > 0 else 0

    return round(res / 1000, 2)
