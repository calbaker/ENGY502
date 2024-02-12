# %%
# imports
import numpy as np
import matplotlib.pyplot as plt

# import fastsim
import fastsim as fsim
from fastsim import fsr

# build SimDriveLabel object for conventional vehicle
veh_base = fsim.vehicle.Vehicle.from_vehdb(1).to_rust()

# find optimum engine size subject to 0-60 mph constraint of 10 s and a fixed cost + linear cost per power 
## Via plotting

### create an array of possible engine (aka fuel converter (fc)) peak power
fc_max_kw_arr = np.linspace(0.8, 10.0, 20) * veh_base.fc_max_kw
### Initialize arrays for storing results
mpg_hwy_arr = [] # highway
mpg_udds_arr = [] # city (udds = urban dynamometer driving schedule)
mpg_comb_arr = [] # combined


# i is a loop counter and `fc_max_kw` is the value at the index for that iteration
for i, fc_max_kw in enumerate(fc_max_kw_arr):
    print(f"Solving for fc_max_kw: {fc_max_kw:.3g}")
    veh = veh_base.copy()
    fsim.utils.set_attr_with_path(
        veh, # vehicle object
        "fc_max_kw", # vehicle attribute to set
        fc_max_kw, # new value
    )
    sdl: fsr.LabelFe = fsr.get_label_fe(veh)[0]
    mpg_comb_arr.append(sdl.adj_comb_mpgge)
    mpg_udds_arr.append(sdl.adj_udds_mpgge)
    mpg_hwy_arr.append(sdl.adj_hwy_mpgge)

fig, ax = plt.subplots()
ax.plot(
    fc_max_kw_arr,
    mpg_comb_arr,
    label='combined',
)
ax.plot(
    fc_max_kw_arr,
    mpg_udds_arr,
    label='udds',
)
ax.plot(
    fc_max_kw_arr,
    mpg_hwy_arr,
    label='hwy',
)
ax.legend()
plt.show()

## Via scipy optimize with 0-60 mph time constraint

# Plot time traces of selected design
# %%
