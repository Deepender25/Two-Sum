# 🧮 Two Sum - LeetCode Problem #1

This repository contains a Python solution for the popular LeetCode problem: **Two Sum**.

## 🔗 Problem Link

[Two Sum – LeetCode #1](https://leetcode.com/problems/two-sum/)

## 💡 Problem Statement

> Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.
>
> You may assume that each input would have exactly one solution, and you may not use the same element twice.
>
> You can return the answer in any order.

## 🧠 Approach

We use a **hash map** (dictionary in Python) to store previously seen numbers and their indices.  
This allows us to find the required complement in constant time — giving us an efficient **O(n)** solution.

## ✅ Python Code

```python
class Solution:
    def twoSum(self, nums, target):
        prevMap = {}  # num -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []
