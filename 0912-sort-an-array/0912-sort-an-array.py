class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergesort(a):
            if len(a) > 1:
                mid = len(a) // 2
                l = a[:mid]
                r = a[mid:]
                mergesort(l)
                mergesort(r)
                
                lptr = 0
                rptr = 0
                aptr = 0
                
                while lptr < len(l) or rptr < len(r):
                    if lptr > len(l) - 1:
                        a[aptr] = r[rptr]
                        aptr += 1
                        rptr += 1
                    
                    elif rptr > len(r) - 1:
                        a[aptr] = l[lptr]
                        aptr += 1
                        lptr += 1
                    
                    else:
                        if l[lptr] < r[rptr]:
                            a[aptr] = l[lptr]
                            aptr += 1
                            lptr += 1
                        else:
                            a[aptr] = r[rptr]
                            rptr += 1
                            aptr += 1
                return a
            else:
                return a
        
        return mergesort(nums)