# 0x08. Making Change

## Introduction
Welcome to the "0x08. Making Change" project repository. This project challenges you to tackle the classic coin change problem using dynamic programming and greedy algorithms. The objective is to find the minimum number of coins required to make up a given total amount, given a list of coin denominations. By leveraging your understanding of algorithms and problem-solving strategies, you'll devise efficient solutions to address this task.

## Project Details
- **Algorithm**: Python

## Key Concepts
### Greedy Algorithms
- Understanding the workings of greedy algorithms and their suitability for the coin change problem.
- Recognizing the limitations of greedy algorithms and identifying scenarios where they might not provide the optimal solution.

### Dynamic Programming
- Grasping the fundamental principles of dynamic programming for solving optimization problems.
- Understanding overlapping subproblems and optimal substructure in the context of the coin change problem.

### Algorithmic Complexity
- Analyzing the time and space complexity of algorithms.
- Striving for solutions with lower complexity to meet runtime constraints.

### Problem-Solving Strategies
- Decomposing the problem into smaller, manageable sub-problems.
- Exploring both iterative and recursive approaches to dynamic programming.

### Python Programming
- Proficient manipulation of lists and utilization of list comprehensions.
- Implementing functions with efficient looping and conditional statements.

## Resources
- **Python Official Documentation**: Explore more Control Flow Tools such as for loops and if statements.
- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials**: Dynamic Programming - Coin Change Problem for a visual and step-by-step explanation.

By mastering these concepts and utilizing the provided resources, you'll be well-equipped to tackle the coin change problem. Your task involves deciding whether a greedy algorithm suffices for your coin denominations or if a more comprehensive dynamic programming approach is necessary for correctness and efficiency.

## Additional Resources
- Mock Technical Interview

## Requirements
### General
- **Allowed Editors**: vi, vim, emacs
- **Environment**: All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Standards**:
  - All files should end with a new line.
  - The first line of all files should be exactly `#!/usr/bin/python3`.
- **Mandatory Files**:
  - A `README.md` file at the root of the project folder.
- **Coding Style**: Adherence to the PEP 8 style (version 1.7.x).
- **Execution**: All files must be executable.

## Tasks
### 0. Change comes from within
- Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.
- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet total
- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task

### Example
```python
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37)) 
print(makeChange([1256, 54, 48, 16, 102], 1453))  
Repository Information
GitHub Repository: alx-interview
Directory: 0x08-making_change
File: 0-making_change.py

License
This project is licensed under the MIT License. See the LICENSE file for details.
