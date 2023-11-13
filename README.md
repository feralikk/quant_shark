Test assignment 
for the Junior Python Developer position


Imagine that a telecommunications company is working on designing an efficient 7G-network layout for a new city. The city can be represented as a grid, where some blocks are obstructed and cannot have towers, while others can. The goal is to provide the maximum coverage with the minimum number of towers.

Task 1: Grid Representation
Create a class CityGrid that can represent the city as an N x M grid. During the initialization of the class, obstructed blocks are randomly placed with coverage >30% (we can change this parameter).

Task 2: Tower Coverage
Each tower has a fixed range R (in blocks) within which it provides coverage. This coverage is a square, with the tower in the center.
Implement a method in the CityGrid class to place a tower and visualize its coverage.

Task 3: Optimization Problem
Design an algorithm to place the minimum number of towers such that all of non-obstructed blocks are within the coverage of at least one tower. The algorithm cannot place towers on obstructed blocks.
Implement a method in the CityGrid class to display the placement of towers.

Task 4: Path Reliability
Imagine that data is transmitted between towers. For simplicity, assume that each tower can directly communicate with any other tower within its range.
Design an algorithm to find the most reliable path between two towers. The reliability of a path decreases with the number of hops (tower-to-tower links). So, a path with fewer hops is more reliable.

Task 5: Visualization
Implement functions to visualize the CityGrid, including obstructed blocks, towers, coverage areas, and data paths.
Use any Python plotting library of your choice, such as matplotlib or seaborn.

Bonus tasks (optional):
Extend the optimization problem: Now towers have a cost, and you have a limited budget. Modify your algorithm to maximize coverage while staying within the budget.

Consider different types of towers with different ranges and costs. How would this change your optimization approach?

Result with N = 10, M = 10, coverage_threshold = 0.3, tower_radius = 3
![image](https://github.com/feralikk/quant_shark/assets/66134845/fa2fcc07-7eff-444d-a584-e84285061be8)

Result with N = 15, M = 15, coverage_threshold = 0.2, tower_radius = 4
![image](https://github.com/feralikk/quant_shark/assets/66134845/1cd5ade1-eea6-4ac7-ba47-5bb445d015d0)

Result with N = 30, M = 30, coverage_threshold = 0.4, tower_radius = 8
![image](https://github.com/feralikk/quant_shark/assets/66134845/7e71732a-27be-4419-893a-44d31dbce526)
