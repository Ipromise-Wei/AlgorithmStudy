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