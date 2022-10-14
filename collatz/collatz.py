#Collatz Conjecrure
#Kukutani Problem
#3N+1 problem

import sys
class Collatz:
    """Coklatz Conjecture"""
    vals = []
    def __init__(self, n):
        self.num = self.n = n
    
    @property
    def val(self):
        return self.n

    @val.setter
    def val(self, new_n):
        self.n = new_n
        return new_n

    def algo(self):
        while (self.val>1):
            if self.val == 1: break
            elif self.val % 2 == 0:
                self.val = int(self.val/2)
                self.vals.append(self.val)
            else:
                self.val = 3*self.val +1
                self.vals.append(self.val)
        return {"value": self.num, "hailstones": self.vals, "count": len(self.vals)}

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 2:
        t = Collatz(int(args[1]))
        print(t.algo())
    else:
        raise ValueError("Require a single value")
