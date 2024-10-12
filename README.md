# Python Challenges

This repository contains a set of small programming challenges that I've solved in Python. The challenges are:

1. [Two Sum](#two-sum)
2. [Valid Parentheses](#valid-parentheses)
3. [Merge Two Sorted Lists](#merge-two-sorted-lists)

## Two Sum

Given an array of integers `nums` and an integer `target`, the goal of this challenge is to find two numbers in `nums` that add up to `target`. The function `twoSum` in `challenge1.py` solves this problem.

### Usage

To use `twoSum`, pass in the array `nums` and the target integer `target` as arguments. The function will return a list of two indices that correspond to the numbers in `nums` that add up to `target`.

For example:

```python
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]