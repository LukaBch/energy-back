from .compute_hours_consumptions import compute_hour_consumptions
from ..constants import APPLIANCES

def get_energy_consumptions(selected_appliances, total_consumption):
    hour_consumptions = compute_hour_consumptions(
        selected_appliances=selected_appliances,
        max_energy_consumption=total_consumption
    )
    
    total_energy = sum(
      [
        round(hour_consumptions[appliance_id]*APPLIANCES[appliance_id]["power"]/1000, 2) 
        for appliance_id in APPLIANCES.keys()
      ]
    )
    
    energy_consumptions = []
    for appliance_id, appliance_info in APPLIANCES.items():
        power = appliance_info["power"]
        energy = round(hour_consumptions[appliance_id]*power/1000, 2)
        energy_consumptions.append(
          {
            "id": appliance_id,
            "hours": hour_consumptions[appliance_id],
            "energy": energy,
            "proportion": round(100*energy/total_energy, 2)
          }
        )
    
    return {
      "energies": energy_consumptions,
      "total": round(total_energy, 2)
    }
