# FASTSim Homework Problem

## Background

Vehicle component (e.g. engine, battery, electric motor(s)) sizing is a multi-objective optimization problem that is subject to numerous constraints with the goal of satisfactorily achieving numerous objectives that are often in conflct.  Important considerations are annual fuel/energy usage, lifetime operating cost (including initial purchase price), vehicle weight, and acceleration performance -- this is not an exhaustive list.  To help familiarize you with the challenges involved in optimizing component sizes, this assignment will show you an [example](./example.py) and then ask you to complete an assignment with a few changes from the example.

## Assignment
Use [NREL's FASTSim](https://github.com/NREL/fastsim) to find optimum battery and motor size subject to 0-60 mph constraint of 10 s and a fixed cost + linear cost per battery energy and motor/battery power of $25/kW-hr and $5/kW, respectively, using a 2022 Tesla Model 3 RWD with the goal of minimizing 5 year operating cost 

### Hints about manipulating parameters
The parameters you'll need to manipulate are 
-`mc_max_kw` (motor peak power), https://docs.rs/fastsim-core/latest/fastsim_core/vehicle/struct.RustVehicle.html#structfield.mc_max_kw
-`ess_max_kw` (battery peak power), https://docs.rs/fastsim-core/latest/fastsim_core/vehicle/struct.RustVehicle.html?search=ess_max_kwh#structfield.ess_max_kw
-`ess_max_kwh` (battery energy capacity), https://docs.rs/fastsim-core/latest/fastsim_core/vehicle/struct.RustVehicle.html#structfield.ess_max_kwh

I encourage you to explore the documentation and ask questions!

When setting parameters, make sure that battery power is always 10% greater than motor power to ensure that the battery is not power limiting, e.g. 
```python
fsim.utils.set_attr_with_path(
    veh, # vehicle object
    "mc_max_kw", # vehicle attribute to set
    mc_max_kw, # new value
)
fsim.utils.set_attr_with_path(
    veh, # vehicle object
    "ess_max_kw", # vehicle attribute to set
    veh.mc_max_kw * 1.1, # 10% higher than `veh.mc_max_kw`
)
```

### Objectives
You'll want to construct an objective similar to `cost_5_years` in [example.py](./example.py) that accounts for initial component costs and energy costs over 5 years of operation.  

### Assumptions
You can assume the following:
- electricity costs $0.12/kW-hr
- motor/battery power is $5/kW-hr
- the vehicle is driven 15,000 miles per year


