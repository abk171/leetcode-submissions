class Solution:
    def fib(self, n: int) -> int:
        store = [0, 1]
        if n <= 1:
            return store[n]
        for i in range(1, n):
            temp = store[1]
            store[1] = store[1] + store[0]
            store[0] = temp
        
        return store[1]
        
        