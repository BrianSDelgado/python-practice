"""
Two Sum - Practice Problem

Given a list of numbers `nums` and a target number `target`,
return the indices of the two numbers such that they add up to `target`.
"""


def two_sum(nums, target):
    seen = {}  # value -> index

    for i, num in enumerate(nums):
        needed = target - num
        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"nums = {nums}, target = {target}")
    print(f"Two Sum indices: {result}")
