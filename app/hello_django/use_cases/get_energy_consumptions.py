from .compute_hours_consumptions import compute_hour_consumptions
from ..constants import APPLIANCES

def get_energy_consumptions(selected_appliances, total_consumption):
    hour_consumptions2 = compute_hour_consumptions(
        selected_appliances=selected_appliances,
        max_energy_consumption=total_consumption
    )
    res = []
    total_energy = 0
    for appliance_id, appliance_info in APPLIANCES.items():
        if appliance_id in selected_appliances:
            power = appliance_info["power"]
            energy = round(hour_consumptions2[appliance_id]*power/1000, 2)
            total_energy += energy
            res.append(
              {"id": appliance_id, "hours": hour_consumptions2[appliance_id], "energy": energy}
            )
        else:
            res.append(
              {"id": appliance_id, "hours": 0, "energy": 0}
            )
    
    for result in res:
        result["proportion"] = round(100*result["energy"]/total_energy, 2)
    return {
      "energies": res,
      "total": round(total_energy, 2)
    }
