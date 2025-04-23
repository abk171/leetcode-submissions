class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        merge = [0 for _ in range(m + n)]

        i, j, ptr = 0, 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merge[ptr], i = nums1[i], i + 1
            else:
                merge[ptr], j = nums2[j], j + 1
            ptr += 1
        
        while i < m:
            merge[ptr], i = nums1[i], i + 1
            ptr += 1
        
        while j < n:
            merge[ptr], j = nums2[j], j + 1
            ptr += 1
        
        mid = (m + n) // 2

        if (m + n) % 2 == 0:
            return (merge[mid] + merge[mid - 1]) / 2
        return merge[mid]
