import unittest
from production_optimization.optimization.solver import run_optimization

class TestOptimization(unittest.TestCase):

    def test_optimization_solution(self):
        model = run_optimization()
        
        # Check if the status is optimal 
        self.assertEqual(model.status, 1, "The optimization model did not solve to optimality.")
        self.assertGreaterEqual(model.objective.value(), 0, "The total profit should be non-negative.")

if __name__ == '__main__':
    unittest.main()
