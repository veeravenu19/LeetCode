class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        a=len(nums1)//2
        # s=0
        if len(nums1)%2==0:
            s=float(nums1[a])+float(nums1[a-1])
            return s/2
        else:
            return float(nums1[a])
