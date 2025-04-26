# Jacobi Method Solver

This Python program implements the Jacobi iterative method for solving systems of linear equations. It allows users to input matrices either manually or from files and performs calculations with various convergence checks. The program includes features to ensure matrix properties like irreducibility and diagonal dominance to guarantee solution accuracy.

---

## Features
- **Jacobi Iterative Method**: Solves systems of linear equations using the Jacobi iterative algorithm.
- **Matrix Validations**:
  - Checks for irreducibility of the coefficient matrix.
  - Verifies weak diagonal dominance with at least one strict dominance.
  - Ensures no zero values exist on the diagonal.
- **Convergence Controls**: Supports customized stopping criteria like iteration limits or error thresholds.
- **Input Options**: Matrices can be loaded from user input or text files.
- **Error Handling**: Provides warnings for matrices that may not converge.
