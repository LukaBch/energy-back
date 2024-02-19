from pulp import LpMaximize, LpProblem, LpVariable, LpSolverDefault
from ..constants import HOURS_CATEGORIES, APPLIANCES


def compute_hour_consumptions(selected_appliances, max_energy_consumption):
    """
    Maximizes sum(e_i * h_i) with integer constraints.
    given the constraints
    - sum(e_i * h_i) ≤ max_energy_consumption
    - h_i is an integer
    - 6 ≤    h_1 + h_2    ≤ 8
    - 1 ≤ h_3 + h_4 + h_5 ≤ 4
    - 4 ≤ h_6 + h_7 + h_8 ≤ 24
    - if e_i = 0 then h_i = 0
    """

    coefficients = {i: round(APPLIANCES[i]["power"] / 1000, 2) if i in selected_appliances else 0 for i in APPLIANCES.keys()}

    lp_problem = LpProblem(name="Maximize_Objective", sense=LpMaximize)

    variables = {i: LpVariable(f"x_{i}", lowBound=0, cat="Integer") for i in APPLIANCES.keys()}

    # Add the objective function to maximize
    lp_problem += (coefficients[1] * variables[1] + coefficients[2] * variables[2] + coefficients[3] * variables[3] + coefficients[4] * variables[4] + coefficients[5] * variables[5] + coefficients[6] * variables[6] + coefficients[7] * variables[7] + coefficients[8] * variables[8])

    # Add the constraints
    lp_problem += (coefficients[1] * variables[1] + coefficients[2] * variables[2] + coefficients[3] * variables[3] + coefficients[4] * variables[4] + coefficients[5] * variables[5] + coefficients[6] * variables[6] + coefficients[7] * variables[7] + coefficients[8] * variables[8] <= max_energy_consumption)
    for i in APPLIANCES.keys():
        if coefficients[i] == 0:
            lp_problem += variables[i] == 0
    
    if (coefficients[1] > 0 or coefficients[2] > 0):
        lp_problem += (HOURS_CATEGORIES["F"]["min"] <= variables[1] + variables[2])
        lp_problem += (variables[1] + variables[2] <= HOURS_CATEGORIES["F"]["max"])
    
    if (coefficients[3] > 0 or coefficients[4] > 0 or coefficients[5] > 0):
        lp_problem += (HOURS_CATEGORIES["A"]["min"] <= variables[3] + variables[4] + variables[5])
        lp_problem += (variables[3] + variables[4] + variables[5] <= HOURS_CATEGORIES["A"]["max"])
    
    if (coefficients[6] > 0 or coefficients[7] > 0 or coefficients[8] > 0):
        lp_problem += (HOURS_CATEGORIES["L"]["min"] <= variables[6] + variables[7] + variables[8])
        lp_problem += (variables[6] + variables[7] + variables[8] <= HOURS_CATEGORIES["L"]["max"])
    
    LpSolverDefault.msg = False

    # Solve the problem
    lp_problem.solve()

    return {i: round(variables[i].value(), 2) if variables[i].value() is not None else 0 for i in APPLIANCES.keys()}
