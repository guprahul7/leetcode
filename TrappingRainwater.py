

def trappingRainwater(elevations):

    totalVolume = 0
    length = len(elevations)

    for i in range(length):
        Lmax = max(elevations[:i+1]) #include the i-th index as well
        Rmax = max(elevations[i+1:])

        waterAndBuilding = min(Lmax,Rmax)
        water = waterAndBuilding - elevations[i]

        totalVolume += water

    return totalVolume
    

