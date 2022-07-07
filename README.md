# Pathfinding-on-a-2D-grid
## The Amazon Coding Exercise set during the Bright Network Technology Internship Experience UK 2022

Overview:

Implement Amazon's pathfinding algorithm for Amazon's self-driving delivery vehicles. The self-driving vehicle will need to create a path on a 2D-grid that contains a starting point, a delivery point and a number of obstacles. The vehicle can navigate to any of the adjacent squares (up, down, left, right or diagonally) as long as they are inbound and do not contain obstacles.

Phase 1:
Implement a 10x10 grid tht contains a starting point on (0,0), the delivery point on (99,9) and the following obstacle locations (9,7), (8,7), (7,7), and (7,8).

Phase 2: 
Add an additional 20 randomly placed obstacles and print their locations. They should not overlap with the start point, delivery point or any pther obstacles. Use the algorithm to calculate a valid path avoiding the obstacles and reaching the delivery point. 

BONUS:
If no such path is possible, the algorithm should print "Unable to reach delivery point" and identify which obstacles need to be removed for the vehicle to reach its destination.
