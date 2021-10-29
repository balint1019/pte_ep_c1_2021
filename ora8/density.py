mercury = 18
copper = 23
mercury_density = 11.34
copper_density = 8.69
mercury_weight = mercury*mercury_density
copper_weight = copper*copper_density
if mercury_weight <= copper_weight:
    print("A réz a nehezebb")
else:
    print("Az ólom a nehezebb")
