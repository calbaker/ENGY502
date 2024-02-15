# %%
# imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from typing import Tuple

# import fastsim
import fastsim as fsim
from fastsim import fsr

# build SimDriveLabel object for conventional vehicle
veh_base = fsim.vehicle.Vehicle.from_vehdb(1).to_rust()

def get_vehicle_metrics(
    fc_max_kw: float
) -> Tuple[float, float]:
    """
    Simulates fastsim to calculate combined (mix of hwy and city) label mpg

    Args:
        fc_max_kw (float): engine max power [kW]

    Returns:
        Tuple[float, float]: combined label mpg and 0-60 mph time [s]
    """

    veh = veh_base.copy()
    fsim.utils.set_attr_with_path(
        veh,  # vehicle object
        "fc_max_kw",  # vehicle attribute to set
        fc_max_kw,  # new value
    )
    veh.set_derived()
    sdl: fsr.LabelFe = fsr.get_label_fe(veh)[0]
    return sdl.adj_comb_mpgge, sdl.net_accel

# Constants for calculations
annual_mileage = 15e3
cost_per_gallon = 3.00
cost_per_fc_kw = 5  # this number is based on engineering judgment

def obj_fun(fc_max_kw: float) -> float:
    """
    Get 5 year cost of ownership (including component costs but not overall purchase cost) as a
    function of engine power

    Args:
        fc_max_kw (float): engine peak power

    Returns:
        float: annual operating cost
    """

    mpg = get_vehicle_metrics(fc_max_kw)[0]
    annual_gallons = annual_mileage / mpg
    cost_5_years = 5. * annual_gallons * cost_per_gallon + fc_max_kw * cost_per_fc_kw

    return cost_5_years

# maximum allowable zero-to-sixty time [s]
max_zero_to_sixty = 9.0


def constraint_fun(fc_max_kw: float) -> float:
    return max_zero_to_sixty - get_vehicle_metrics(fc_max_kw)[1]

# find optimum engine size subject to 0-60 mph constraint of 10 s and a fixed cost + linear cost per power 
# Via plotting

# create an array of possible engine (aka fuel converter (fc)) peak power
fc_max_kw_arr = np.linspace(0.8, 1.5, 20) * veh_base.fc_max_kw
# Initialize arrays for storing results
mpg_hwy_arr = [] # highway
mpg_udds_arr = [] # city (udds = urban dynamometer driving schedule)
mpg_comb_arr = [] # combined
zero_to_sixty_arr = []
cost_5_year_arr = []

# i is a loop counter and `fc_max_kw` is the value at the index for that iteration
for i, fc_max_kw in enumerate(fc_max_kw_arr):
    print(f"Solving for fc_max_kw: {fc_max_kw:.3g}")
    veh = veh_base.copy()
    fsim.utils.set_attr_with_path(
        veh, # vehicle object
        "fc_max_kw", # vehicle attribute to set
        fc_max_kw, # new value
    )
    veh.set_derived()
    sdl: fsr.LabelFe = fsr.get_label_fe(veh)[0]
    mpg_comb_arr.append(sdl.adj_comb_mpgge)
    mpg_udds_arr.append(sdl.adj_udds_mpgge)
    mpg_hwy_arr.append(sdl.adj_hwy_mpgge)
    zero_to_sixty_arr.append(sdl.net_accel)
    cost_5_year_arr.append(obj_fun(fc_max_kw))

fig, ax = plt.subplots()
ax.plot(
    fc_max_kw_arr,
    mpg_comb_arr,
    linestyle="",
    marker='x',
    label='combined',
)
ax.plot(
    fc_max_kw_arr,
    mpg_udds_arr,
    linestyle="",
    marker='d',
    label='udds',
)
ax.plot(
    fc_max_kw_arr,
    mpg_hwy_arr,
    linestyle="",
    marker='s',
    label='hwy',
)
ax.set_xlabel('Engine Max Power (kW)')
ax.set_ylabel("MPG")
ax.legend()

mpg_color = 'magenta'
ax2 = ax.twinx()
ax2.plot(
    fc_max_kw_arr,
    zero_to_sixty_arr,
    linestyle="",
    marker='o',
    color=mpg_color
)
ax2.set_ylabel("0-60 mph Time [s]", color=mpg_color)

plt.show()

fig, ax = plt.subplots()
ax.plot(
    fc_max_kw_arr, 
    cost_5_year_arr, 
    linestyle="",
    marker="d",
)
ax.set_xlabel('Engine Max Power (kW)')
ax.set_ylabel('5 Year Operating Cost\nBased on Fuel and Engine')
plt.show()

# Via scipy optimize with 0-60 mph time constraint

constraints = {'type': 'ineq', 'fun': constraint_fun}
bounds = [(50, 150)]

fc_max_kw_best_mpg = minimize(
    obj_fun,
    100.0, # initial guess
    bounds=bounds,
    constraints=constraints
)

print('\n')
print("*"*25)
print(f"Engine peak power that maximizes mpg with 0-60 mph time not exceeding 9 s:\n{fc_max_kw_best_mpg.x[0]:.3g} kW")


# Plot time traces of selected design
# %%
