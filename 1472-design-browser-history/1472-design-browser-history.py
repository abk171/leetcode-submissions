class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0
        self.last = 0
        

    def visit(self, url: str) -> None:
        self.current += 1
        
        if self.current < len(self.history):
            self.history[self.current] = url

        else:
            self.history.append(url)
        
        self.last = self.current
        

    def back(self, steps: int) -> str:
        self.current = max(0, self.current - steps)
        return self.history[self.current]
        

    def forward(self, steps: int) -> str:
        self.current = min(self.last, self.current + steps)
        return self.history[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)