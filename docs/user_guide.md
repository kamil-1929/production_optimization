## Production Optimization User Guide

## Introduction
This user guide provides detailed instructions on how to use the Production Optimization project. The project aims to maximize profit from the production of five products (P1, P2, P3, P4, and P5) while adhering to various resource constraints.

## Getting Started

## Prerequisites
Ensure you have the following installed on your system:

- Python 3.x
- pip (Python package installer)

## Installation
1. Clone the repository:
```sh
git clone https://github.com/yourusername/production_optimization.git
```
2. Navigate to the project directory:
```sh
cd production_optimization
```
3. Install the required dependencies:
```sh
pip install -r requirements.txt
```
## Running the Optimization
To run the optimization script, execute the following command in your terminal:

```sh
python optimization.py
```
## Output
The script will output the following information:

Status: Indicates whether the optimization problem was successfully solved.
Optimal Production Quantities: The optimal number of units to produce for each product (P1 to P5).
Total Profit: The maximum achievable profit based on the optimized production quantities.
Resource Utilization: The total usage of labor, machine time, and raw materials.

## Example Output
```sh
Status: Optimal
Optimal Production of P1: 10.0
Optimal Production of P2: 0.0
Optimal Production of P3: 10.0
Optimal Production of P4: 5.0
Optimal Production of P5: 6.0
Total Profit: $147.0
Total Labor Utilization: 99.0 units
Total Machine Time Utilization: 78.0 units
Total Raw Materials Utilization: 68.0 units
```

## Testing
To run the test cases and validate the optimization logic, execute the following command:

```sh
python -m unittest discover -s tests
```

## Additional Information
For more details on the constraints and objective function used in the optimization, refer to the comments and documentation within the optimization.py script.

## Support
If you encounter any issues or have questions, please open an issue on the GitHub repository.

## Conclusion
This user guide provides a comprehensive overview of the Production Optimization project, from installation to running the optimization and interpreting the results. For further assistance, refer to the provided support options.
