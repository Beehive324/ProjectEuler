
class EvenFibNum:
    def __init__(self):
        self.even_sum = 0
        self.n_map = {}
        
    def sol(self,n):
        if n in self.n_map:
            return self.n_map[n]
        
        if n <= 1:
            return 1
        
        res = self.sol(n-1) + self.sol(n - 2)
        self.n_map[n] = res
        
        return res
    
    def under_limit(self, limit):
        n = 0
        
        while True:
            x = self.sol(n)
            if x > limit:
                break
            if x <= limit:
                if x % 2 == 0:
                    self.even_sum += x
            n += 1
    
        return self.even_sum
        
        
    
        
       
if __name__ == "__main__":
    fib = EvenFibNum()
    
    print(fib.under_limit(4000000))
    
