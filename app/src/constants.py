APPLIANCES = {
    1: {"category": "F", "name": 'Fridge', "power": 2000},
    2: {"category": "F", "name": 'Freezer', "power": 2500},
    3: {"category": "A", "name": 'Washing machine', "power": 1500},
    4: {"category": "A", "name": 'Dishwasher', "power": 2500},
    5: {"category": "A", "name": 'Induction Stove', "power": 3000},
    6: {"category": "L", "name": 'TV', "power": 500},
    7: {"category": "L", "name": 'Small Light', "power": 100},
    8: {"category": "L", "name": 'Big Light', "power": 800},
}

HOURS_CATEGORIES = {
    "F": {
        "min": 6,
        "max": 8
    },
    "A": {
        "min": 1,
        "max": 4
    },
    "L": {
        "min": 4,
        "max": 24
    }
}

MAX_TOTAL_ENERGY_CONSUMPTION = 75