def jumpingOnClouds(clouds, k, energy=100):
    childPosition=0
    while True:
        childPosition+=k
        
        if childPosition>len(clouds)-1:
            childPosition= childPosition-len(clouds)
            
        if clouds[childPosition]==0:
            energy-=1
        else:
            energy-=3
        
        if childPosition==0:
            return energy

print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 1, 0], 2))