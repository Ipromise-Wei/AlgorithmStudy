# 数组是一种线性数据结构，其将相同类型的元素存储在连续的内存空间中。我们将元素在数组中的位置称为盖元素的索引。

import random

# 1.初始化数组
arr: list[int] = [0] * 5        #[0, 0, 0, 0, 0] 
nums: list[int] = [1, 2, 3, 4, 5]       #[1, 2, 3, 4, 5]
i = [11, 21, 31, 41]


# 2.访问数组元素
def random_access(nums: list[int]) -> int:
    '''随机访问元素'''
    # 在区间[0, len(nums)-1]中随机抽取一个数字
    random_index = random.randint(0, len(nums)-1)
    random_num = nums[random_index]
    return random_num

# 3.插入元素
def insert(nums: list[int], num: int , index: int):
    '''在数组的索引index处插入元素num'''
    # 把索引 index 以及之后的所有元素向后移动一位
    for i in range(len(nums)-1, index, -1):
        nums[i] = nums[i - 1]
    nums[index] = num
    
# 4.删除元素
def remove(nums: list[int], index: int):
    '''删除索引 index处的元素'''
    # 把索引index之后的元素前移一位
    for i in range(index, len(nums)-1):
        nums[i] = nums[i + 1]
        
# 5.遍历数组
def traverse(nums: list[int]):
    '''遍历数组'''
    count = 0
    # 通过索引遍历数组
    for i in range(len(nums)):
        count += nums[i]
    # 直接遍历数组元素
    for num in nums:
        count += num
    # 同时遍历数组索引和元素
    for i, num in enumerate(nums):
        count += nums[i]
        count += num
        
# 6.查找元素
def find(nums: list[int], target: int) -> int:
    '''在数组中查找target元素'''
    for i in range(len(nums)):
        if nums[i] == target:
            return 1    
    return -1

# 7.扩容数组
def extend(nums: list[int], enlarge: int) -> list[int]:
    '''扩展数组长度'''
    # 初始化一个扩展长度后的数组
    res = [0] * (len(nums) + enlarge)
    # 将原数组中的所有元素复制到新数组
    for i in range(len(nums)):
        res[i] = nums[nums]
    return res