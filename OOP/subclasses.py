class Vehicles: 
    pass 


class LandVehicles(Vehicles): 
    pass 


class TrackedVehicles(LandVehicles): 
    pass 


for cls1 in [Vehicles, LandVehicles, TrackedVehicles]: 
    for cls2 in [Vehicles, LandVehicles, TrackedVehicles]: 
        print(issubclass(cls1, cls2), end="\t") 
    print()