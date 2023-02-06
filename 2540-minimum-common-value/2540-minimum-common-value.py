class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        n1ptr = 0
        n2ptr = 0
        
        while n1ptr < len(nums1) and n2ptr < len(nums2):
            if nums1[n1ptr] == nums2[n2ptr]:
                return nums1[n1ptr]
            elif nums1[n1ptr] < nums2[n2ptr]:
                n1ptr += 1
            else:
                n2ptr += 1
        
        return -1
        