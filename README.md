## Production Optimization Project
This project contains tools and scripts for optimizing the production of products under given constraints to maximize profit.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Structure](#structure)
- [Contributing](#contributing)
- [Testing](#testing)

## Introduction
The primary goal of this project is to maximize the total profit from the production of five products (P1, P2, P3, P4, and P5) by optimizing their production quantities within given resource constraints. The constraints include limits on labor, machine time, raw materials, and specific production requirements for certain products.

## Installation
To set up this project, follow these steps:

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

## Usage
To run the optimization and solve the linear programming problem, execute the following command:

```sh
python -m scripts.run_optimization
```
The script will display the status of the solution, optimal production quantities for each product, total profit, and resource utilization.

## Structure

- **.github/**: GitHub workflows for CI/CD.
- **docs/**: Documentation files.
- **production_optimization/**: Main package.
- **tests/**: Unit tests.
- **config/**: Configuration files.
- **data/**: Input and output data directories.
- **scripts/**: Scripts to run the optimization.
- **examples/**: Example usage of the optimization tool.

## Testing
To run the tests, use the following command:

```sh
python -m unittest discover tests
```
## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the existing style and includes appropriate tests.


