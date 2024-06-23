import pulp as pl

def add_constraints(model, x1, x2, x3, x4, x5):
    """
    Adds constraints to the linear programming model .
    """
    model += 2 * x1 + 3 * x2 + x3 + 4 * x4 + 5 * x5 <= 100, "Labor_Constraint"
    model += 3 * x1 + 2 * x2 + 4 * x3 + x4 + 3 * x5 <= 80, "Machine_Time_Constraint"
    model += 4 * x1 + x2 + 3 * x3 + 2 * x4 + 2 * x5 <= 70, "Raw_Materials_Constraint"
    model += x1 <= 20, "P1_Max_Production"
    model += x2 + x3 >= 10, "P2_P3_Min_Combined_Production"
    model += x4 >= 5, "P4_Min_Production"
