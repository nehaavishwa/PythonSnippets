__author__ = 'nvishwakarma'

import Quandl as q

# Data from http://www.quandl.com/SIDC/SUNSPOTS_A-Sunspot-Numbers-Annual
# PyPi url https://pypi.python.org/pypi/Quandl
sunspots = q.get("SIDC/SUNSPOTS_A")
print("Head 2", sunspots.head(2))
print("Tail 2", sunspots.tail(2))


