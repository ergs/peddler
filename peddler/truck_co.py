"""
An institution model that is used to manage a fleet of transport
trucks.
"""

import random
import numpy as np
import scipy as sp

from cyclus.agents import Institution
from cyclus import lib
import cyclus.typesystem as ts


class TruckCompany(Institution):
    """
    An institution used to manage a fleet of transport trucks used to
    carry a specific commodity.
    """

    commodity = ts.String(
        doc="This is the commodity carried by the trucks in the company",
        tooltip="Managed Commodity",
        uilabel="Commodity"
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def tick(self):
        pass

    def tock(self):
        pass

