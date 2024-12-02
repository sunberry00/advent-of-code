def is_inorder(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)

def distinct(nums):
    counts = set([nums.count(n) for n in nums])
    return counts.issubset(set([1]))

def adj(nums):
    diff = [nums[i] - nums[i-1] for i in range(1, len(nums))]
    diff = [abs(x) for x in diff]
    return set(diff).issubset(set([1, 2, 3]))

def part01():
    with open("2024/day02/input.txt", "r") as f:
        input = f.read()

    safe_reports = 0
    for line in input.split("\n"):
        nums = [int(n) for n in line.split(" ")]
        safe_reports += is_inorder(nums) and distinct(nums) and adj(nums)

    print(safe_reports)

def part02():
    with open("2024/day02/input.txt", "r") as f:
        input = f.read()

    safe_reports = 0
    for line in input.split("\n"):
        nums = [int(n) for n in line.split(" ")]
        if is_inorder(nums) and distinct(nums) and adj(nums):
            safe_reports += 1
        else:
            for i in range(len(nums)):
                nums2 = nums.copy()
                nums2 = nums2[:i] + nums2[i+1:]
                if is_inorder(nums2) and distinct(nums2) and adj(nums2):
                    safe_reports += 1
                    break
                
    print(safe_reports)


if __name__ == "__main__":
    part01()
    part02()