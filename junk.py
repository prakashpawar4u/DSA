from typing import List, Optional
from collections import deque

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True


if __name__ == "__main__":
    sobj = Solution()

    test_cases = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [0],
        [2, 0],
        [1, 1, 0, 1]
    ]

    for nums in test_cases:
        print(f"nums = {nums} -> canJump = {sobj.canJump(nums)}")


from bisect import bisect_left 
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         n = len(s)
#         word_set = set(wordDict)

#         dp = [False] * (n+1)
#         dp[n] = True

#         for i in range(n -1, -1, -1):
#             for word in word_set:
#                 length = len(word)
#                 if i + length <= n and s[i: i+length] == word:
#                     if dp[i + length]:
#                         dp[i] = True
#                         break
#         return dp[0]

# sobj = Solution()
# sobj.wordBreak(s = "leetcode", wordDict = ["leet","code"])

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf')] * (amount + 1)
#         dp[0] = 0  # base case

#         for a in range(1, amount + 1):
#             for coin in coins:
#                 if a - coin >= 0:
#                     dp[a] = min(dp[a], 1 + dp[a - coin])

#         return dp[amount] if dp[amount] != float('inf') else -1
    
# sobj = Solution()
# coins = [1,2,5]
# amount = 11
# print(sobj.coinChange(coins, amount))

# def insertionSort(nums: List[int]) -> List[int]:
#     n = len(nums)

#     for i in range(1, n):
#         x = nums[i]
#         j = i - 1
#         while j >= 0 and x < nums[j]:
#             nums[j + 1] = nums[j]
#             j = j-1
#         nums[j + 1] = x
#     return nums

# nums = [8, 3, 5, 2]
# print(insertionSort(nums))

# import heapq

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
    
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         min_heap = []
#         for i, node in enumerate(lists):
#             print(i, node)
       
#             if node:
#                 # print(min_heap, (node.val, i, node))
#                 heapq.headpush(min_heap, (node.val, i, node))
#             dummy = ListNode(0)
#             current = dummy

#             while min_heap:
#                 val, i, node = heapq.head
    


# solution = Solution()
# lists = [[1,4,5],[1,3,4],[2,6]]
# cloned = solution.mergeKLists(lists)
# def productExceptSelf(nums: List[int]) -> List[int]:
#     res = [1] * (len(nums))
#     prefix = 1
#     for i in range(len(nums)):
#         res[i] = prefix
#         prefix *= nums[i]

#     print(f"Prefix ::{res}")

#     postfix = 1
#     for i in range(len(nums) -1, -1, -1):
#         res[i] *= postfix
#         postfix *= nums[i]
#     print(f"Post ::{res}")
#     return res


# nums = [1,2,3,4]
# productExceptSelf(nums)