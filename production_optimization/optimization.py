import pulp as pl

def run_optimization():
    """
    Solves a linear programming problem to maximize profit from producing five products
    under given resource constraints.
    
    Decision Variables:
        x1: Units of product P1
        x2: Units of product P2
        x3: Units of product P3
        x4: Units of product P4
        x5: Units of product P5
        
    Objective:
        Maximize total profit from the production of products P1 to P5 .
        
    Constraints:
        - Labor constraint
        - Machine time constraint
        - Raw materials constraint
        - Maximum production limit for P1
        - Minimum combined production for P2 and P3
        - Minimum production for P4
    """
    
    # Create a linear programming problem instance
    model = pl.LpProblem("Maximize_Profit", pl.LpMaximize)

    # Define decision variables with lower bounds of 0 and integer category
    x1 = pl.LpVariable('x1', lowBound=0, cat='Integer')
    x2 = pl.LpVariable('x2', lowBound=0, cat='Integer')
    x3 = pl.LpVariable('x3', lowBound=0, cat='Integer')
    x4 = pl.LpVariable('x4', lowBound=0, cat='Integer')
    x5 = pl.LpVariable('x5', lowBound=0, cat='Integer')

    # Objective function: Maximize total profit
    model += 5 * x1 + 4 * x2 + 6 * x3 + 7 * x4 + 8 * x5, "Total_Profit"

    # Constraints
    model += 2 * x1 + 3 * x2 + x3 + 4 * x4 + 5 * x5 <= 100, "Labor_Constraint"
    model += 3 * x1 + 2 * x2 + 4 * x3 + x4 + 3 * x5 <= 80, "Machine_Time_Constraint"
    model += 4 * x1 + x2 + 3 * x3 + 2 * x4 + 2 * x5 <= 70, "Raw_Materials_Constraint"
    model += x1 <= 20, "P1_Max_Production"
    model += x2 + x3 >= 10, "P2_P3_Min_Combined_Production"
    model += x4 >= 5, "P4_Min_Production"

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

if __name__ == "__main__":
    run_optimization()
