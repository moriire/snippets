import sys
#Resistance Value calc
class R:
    """This class defines resistance-unit, measured in ohms"""
    def __init__(self, value, measure="ohms"):
        self.value = value # Resistance value
        self.measure = measure #resistance measured in ohms wich can be altered to Kilo Mega as desired

    def __str__(self):
        """electrical resistance value in ohms, e.g. 2-ohms"""
        return f"{self.value}-{self.measure}"

class Total(R):
    """The net resistance value based on arrangement\n series\n parallwl"""
    def __init__(self, *values:int, lap="s"):
        self.lap = lap # s for series and p for parrallel
        self.values = values #array of resistances

    def __inv(self, n) -> float:
        return 1/n

    def resistance(self, lap=None)-> str:
        if lap:
            self.lap = lap
        vals = sum(self.values)
        if self.lap == "p":
            ivals = map(self.__inv, self.values)
            vals = 1/sum(ivals)
        super().__init__(vals)
        return self.__str__()

if __name__ == "__main__":
    args = sys.argv
    if len(args)>1:
        lap, values = args[1], [float(i) for i in args[2:]]
        if lap in ("s", "p"):
            t = Total(*values, lap = lap)
            print(t.resistance())
        else:
            print("res arrangement missing")
    else:
        print("resistance net calc")
        lap = input("arrangengwment type\n")
        vals = input("values seperated with commas")
        values = [float(i) for i in vals.split(",")]
        t = Total(*values, lap = lap)
        print(t.resistance())
