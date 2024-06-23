import pulp as pl
from production_optimization.optimization.constraints import add_constraints
from production_optimization.optimization.objective import set_objective

def run_optimization():
    """
    Solves a linear programming problem to maximize profit from producing five products
    under given resource constraints.
    """
    # Create a linear programming problem instance
    model = pl.LpProblem("Maximize_Profit", pl.LpMaximize)

    # Define decision variables with lower bounds of 0 and integer category
    x1 = pl.LpVariable('x1', lowBound=0, cat='Integer')
    x2 = pl.LpVariable('x2', lowBound=0, cat='Integer')
    x3 = pl.LpVariable('x3', lowBound=0, cat='Integer')
    x4 = pl.LpVariable('x4', lowBound=0, cat='Integer')
    x5 = pl.LpVariable('x5', lowBound=0, cat='Integer')

    # Set objective function
    set_objective(model, x1, x2, x3, x4, x5)

    # Add constraints
    add_constraints(model, x1, x2, x3, x4, x5)

    # Solve the problem using the default solver
    model.solve()

    # Display the status of the solution
    print(f"Status: {pl.LpStatus[model.status]}")

    # Display the optimal production quantities for each product
    print(f"Optimal Production of P1: {x1.varValue}")
    print(f"Optimal Production of P2: {x2.varValue}")
    print(f"Optimal Production of P3: {x3.varValue}")
    print(f"Optimal Production of P4: {x4.varValue}")
    print(f"Optimal Production of P5: {x5.varValue}")

    # Display the total profit
    print(f"Total Profit: ${pl.value(model.objective)}")

    # Optional: Display the resource utilization for better insight
    labor_utilization = 2 * x1.varValue + 3 * x2.varValue + x3.varValue + 4 * x4.varValue + 5 * x5.varValue
    machine_time_utilization = 3 * x1.varValue + 2 * x2.varValue + 4 * x3.varValue + x4.varValue + 3 * x5.varValue
    raw_materials_utilization = 4 * x1.varValue + x2.varValue + 3 * x3.varValue + 2 * x4.varValue + 2 * x5.varValue

    print(f"Total Labor Utilization: {labor_utilization} units")
    print(f"Total Machine Time Utilization: {machine_time_utilization} units")
    print(f"Total Raw Materials Utilization: {raw_materials_utilization} units")

    return model
