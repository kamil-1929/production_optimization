import pulp as pl

def set_objective(model, x1, x2, x3, x4, x5):
    """
    Sets the objective function for the linear programming model .
    """
    model += 5 * x1 + 4 * x2 + 6 * x3 + 7 * x4 + 8 * x5, "Total_Profit"
