"""
A simple reactor model that focuses on the fuel request
operations. 
"""

import random
import numpy as np
import scipy as sp

from cyclus.agents import Facility
from cyclus import lib
import cyclus.typesystem as ts


class Reactor(Facility):
    """
    A reactor model that requests fuel early such that it will recieve fuel in time for
    operation.  
    """

    request_lead_time = ts.Double(
        doc="The number of time steps before refuel that the reactor will request fuel.", 
        tooltip="The number of time steps before refuel that the reactor will request fuel.",
        uilabel="Request Lead Time"
    )

    commodity = ts.String(
        doc="The commodity that the reactor desires", 
        tooltip="Reactor Commodity",
        uilabel="Commodity"
    )

    cyclus_length = ts.Double(
        doc="The amount of time steps between reactor refuels", 
        tooltip="Cycle length of the reactor.",
        uilabel="Cycle Length"
    )
    
    recipe = ts.String(
        doc="Recipe", 
        tooltip="Recipe",
        uilabel="Recipe"
    )

    fuel_mass = ts.Double(
        doc="Mass of requested fuel", 
        tooltip="Mass of Batch",
        uilabel="Fuel Mass"
    )


    fresh_fuel = ts.ResBufMaterialInv()
    core = ts.ResBufMaterialInv()
    waste = ts.ResBufMaterialInv()
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ct_time = 0;
        self.rx_time = 0;
    
    def tick(self):
        if self.rx_time == self.cycle_length:
            self.waste.push(self.core.pop)
            self.core.push(self.fresh_fuel.pop)
            self.rx_time = 0
        elif self.rx_time < self.cycle_length:
            self.rx_time += 1

    def tock(self):
        if self.rx_time == 0:
            self.ct_time = 0

    def get_material_requests(self):
        ports = []
        if self.fresh_fuel.count == 0:
            request_qty = self.fuel_mass
            recipe_a = self.context().get_recipe(self.recipe)
            target_a = ts.Material.create_untracked(request_qty, recipe_a)
            commods = {self.commodity: target_a}
            port = {"commodities": commods, "constraints": request_qty}
            ports.append(port)
        if self.ct_time == self.cycle_length-self.request_lead_time
            request_qty = self.fuel_mass
            recipe_a = self.context().get_recipe(self.recipe)
            target_a = ts.Material.create_untracked(request_qty, recipe_a)
            commods = {self.commodity+"-contract": target_a}
            port = {"commodities": commods, "constraints": request_qty}
            ports.append(port)
        return ports

    def accept_material_trades(self, responses):
        for mat in responses:
            self.fresh_fuel.push(mat)
        
