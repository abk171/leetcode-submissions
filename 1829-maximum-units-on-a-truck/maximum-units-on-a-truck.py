class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse=True)
        units = 0
        ptr = 0
        while truckSize > 0 and ptr < len(boxTypes):
            n, u = boxTypes[ptr]
            b = min(truckSize, n)
            truckSize -= b
            units += b * u
            ptr += 1
        return units