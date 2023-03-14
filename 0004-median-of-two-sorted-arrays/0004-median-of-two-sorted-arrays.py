class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = [0] * (len(nums1) + len(nums2))
        mptr = 0
        n1ptr = 0
        n2ptr = 0
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        while n1ptr < n1 or n2ptr < n2:
            if n1ptr >= n1:
                m[mptr] = nums2[n2ptr]
                n2ptr += 1
                
            elif n2ptr >= n2:
                m[mptr] = nums1[n1ptr]
                n1ptr += 1
                
            else:
                if nums1[n1ptr] < nums2[n2ptr]:
                    m[mptr] = nums1[n1ptr]
                    n1ptr += 1
                else:
                    m[mptr] = nums2[n2ptr]
                    n2ptr += 1
            mptr += 1
        
        s = n1 + n2
        # print(m)
        if s % 2 == 0:
            return (m[(s - 1) // 2] + m[(s) // 2]) / 2
        
        else:
            return m[(s-1) //2]
        
        
        
            
        