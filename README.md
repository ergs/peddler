# peddler

Peddler is a Cyclus Package used to simulate the transport of material from one facility to another. This archetype is currently under development. If you attept to use it and have issues please add issues on the Github 

Dependencies
------------
Python3.5 or higher
Cyclus

Installation
------------
Clone this directory using the following
`git clone https://github.com/ergs/peddler`

Navigate to the directory and install peddler to the cyclus path via the following. 
`python setup.py install`

Truck Archetype
---------------
This archtype performs the behavior of moving materials from one place to another. To accomplish this it initially makes a contract with a facility that is demanding material. Once it has a contract it will pick up the requested material, and return to the same facility that it maintains a contract with. 

Inputs
++++++
- **dest_commod**: The commodity of the facility the truck is dropping off too.
- **source_commod**: This is the commodity of the facility that the truck is picking material up from.
- **total_trip_duration**: The number of timesteps it takes to go from the source facility to the destination. 
- **	return_trip_time**: The number of timesteps until the truck is ready to pick up material again. 

Reactor
-------
This is a pseudo-facility. It is built just to test functionality for the Truck

Inputs
++++++
- **request_lead_time**: The number of time steps before refueling that the reactor will request fuel.
- **commodity**: The commodity the reactor demands
- **cycle_length**: Amount of time steps between reactor refueling.
- **recipe**: The recipe required by the reactor, (string name for a cyclus recipe)
- **fuel_mass**: Amount of fuel the reactor requests.

