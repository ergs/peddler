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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        time = 0;
    
    def tick(self):
        if time < 

    def tock(self):

    def get_matl_bids(self):

    def get_matl_requests(self):

    def get_matl_trades(self):

    def accept_matl_trades(self):
