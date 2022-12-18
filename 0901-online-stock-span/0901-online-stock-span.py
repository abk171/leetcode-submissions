from collections import namedtuple

stockPrice = namedtuple('stockPrice', ['price', 'day'])

class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        days = 1
        while self.st and self.st[-1].price <= price:
            days += self.st.pop().day
        self.st.append(stockPrice(price, days))
        return days

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)