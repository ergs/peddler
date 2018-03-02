"""
A simple truck model that passes material from one facility to another.
"""

import random
import numpy as np
import scipy as sp

from cyclus.agents import Facility
from cyclus import lib
import cyclus.typesystem as ts


class Truck(Facility):
    """
    A truck that transports material through the fuel cycle. 
    """

    commodity = ts.String(
        doc="The commodity that the truck carries", 
        tooltip="Shipped Commodity",
        uilabel="Commodity"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def tick(self):

    def tock(self):

    def get_matl_bids(self):

    def get_matl_requests(self):

    def get_matl_trades(self):

    def accept_matl_trades(self):
