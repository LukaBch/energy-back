from ..constants import APPLIANCES, HOURS_CATEGORIES

def get_min_total_energy_consumption(selected_appliances):
    selected_powers = {category: [] for category in HOURS_CATEGORIES.keys()}

    for appliance_id in selected_appliances:
        category = APPLIANCES[appliance_id]["category"]
        power = APPLIANCES[appliance_id]["power"]
        selected_powers[category].append(power)

    res = 0
    for category in HOURS_CATEGORIES.keys():
        existing_powers_in_category = selected_powers[category]
        if len(existing_powers_in_category) > 0:
            res += min(existing_powers_in_category) * HOURS_CATEGORIES[category]["min"]

    return round(res / 1000, 2)
