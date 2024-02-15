# %%
# imports

import fastsim as fsim

# build SimDriveLabel object for battery electric vehicle (BEV)
veh = fsim.vehicle.Vehicle.from_vehdb(43).to_rust()
assert veh.scenario_name == "2022 Tesla Model 3 RWD", "Loaded the wrong vehicle."

## Via plotting

## Via scipy optimize

# Plot time traces of selected design

# Open-ended question: what are pros/cons of using plotting compared to scipy optimize?
