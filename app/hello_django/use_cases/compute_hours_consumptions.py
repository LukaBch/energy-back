from pulp import LpMaximize, LpProblem, LpVariable, LpSolverDefault
from ..constants import HOURS_CATEGORIES, APPLIANCES


def compute_hour_consumptions(selected_appliances, max_energy_consumption):
    """
    Solves max(energy_F * h_F + energy_A * h_L + energy_L * h_L) with integer constraints.
    given the constraints
    - energy_F * h_F + energy_A * h_L + energy_L * h_L <= max_energy_consumption
    - h_F is an integer between 6 and 8
    - h_A is an integer between 1 and 4
    - h_L is an integer between 4 and 24
    """


    coefficients = [round(APPLIANCES[i]["power"]/1000, 2) if i in selected_appliances else 0 for i in APPLIANCES.keys() ]

    lp_problem = LpProblem(name="Maximize_Objective", sense=LpMaximize)

    # Define variables
    x_1 = LpVariable("x_1", lowBound=0, cat="Integer")
    x_2 = LpVariable("x_2", lowBound=0, cat="Integer")
    x_3 = LpVariable("x_3", lowBound=0, cat="Integer")
    x_4 = LpVariable("x_4", lowBound=0, cat="Integer")
    x_5 = LpVariable("x_5", lowBound=0, cat="Integer")
    x_6 = LpVariable("x_6", lowBound=0, cat="Integer")
    x_7 = LpVariable("x_7", lowBound=0, cat="Integer")
    x_8 = LpVariable("x_8", lowBound=0, cat="Integer")

    # Add the objective function to maximize

    lp_problem += (coefficients[0] * x_1 + coefficients[1] * x_2 + coefficients[2] * x_3 + coefficients[3] * x_4 + coefficients[4] * x_5 + coefficients[5] * x_6 + coefficients[6] * x_7 + coefficients[7] * x_8 )

    # Add the constraints
    lp_problem += (coefficients[0] * x_1 + coefficients[1] * x_2 + coefficients[2] * x_3 + coefficients[3] * x_4 + coefficients[4] * x_5 + coefficients[5] * x_6 + coefficients[6] * x_7 + coefficients[7] * x_8 <= max_energy_consumption)
    if coefficients[0] == 0:
        lp_problem += coefficients[0] == 0
    if coefficients[1] == 0:
        lp_problem += coefficients[1] == 0
    lp_problem += HOURS_CATEGORIES["F"]["min"] <= x_1 + x_2 <= HOURS_CATEGORIES["F"]["max"]
    if coefficients[2] == 0:
        lp_problem += x_3 == 0
    if coefficients[3] == 0:
        lp_problem += x_4 == 0
    if coefficients[4] == 0:
        lp_problem += x_5 == 0
    lp_problem += HOURS_CATEGORIES["A"]["min"] <= x_3 + x_4 + x_5 <= HOURS_CATEGORIES["A"]["max"]
    if coefficients[5] == 0:
        lp_problem += x_6 == 0
    if coefficients[6] == 0:
        lp_problem += x_7 == 0
    if coefficients[7] == 0:
        lp_problem += x_8 == 0
    
    lp_problem += HOURS_CATEGORIES["L"]["min"] <= x_6 + x_7 + x_8 <= HOURS_CATEGORIES["L"]["max"]
    
    LpSolverDefault.msg = False

    # Solve the problem
    lp_problem.solve()

    # Return the results
    return {
        1: round(x_1.value(),2) if x_1.value() is not None else 0,
        2: round(x_2.value(),2) if x_2.value() is not None else 0,
        3: round(x_3.value(),2) if x_3.value() is not None else 0,
        4: round(x_4.value(),2) if x_4.value() is not None else 0,
        5: round(x_5.value(),2) if x_5.value() is not None else 0,
        6: round(x_6.value(),2) if x_6.value() is not None else 0,
        7: round(x_7.value(),2) if x_7.value() is not None else 0,
        8: round(x_8.value(),2) if x_8.value() is not None else 0,
    }
