#!/usr/bin/env python

"""bubble-point-pressure-black-oil.py: from William D. McCain, Jr.
This is for finding the bubble-point pressure-solution gas-oil ratio of black oil
from Appendix B-37 and B-38 Equations, temperature is in F, Solution
gas oil (Rs) is in standard cubic feet per stock tank barrel scf/STB
, API is the API gravity of the stock tank oil, SGg is the specific
gravity of the seperator gas, bubble point pressure is in psia,
this equation is accurate to within 15% for temperatures up to 325F"""

__author__ = "Wesley C. Williams"
__copyright__ = "Copyright 2007, Wesley C. Williams"
__credits__ = ["Wesley C. Williams"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wesley C. Williams"
__email__ = "wcwmit@gmail.com"
__status__ = "Production"

Rs = input("Input Solution Gas Oil Ratio (Rs) in SCF/STB: ")
SGg = input("Input Specific Gravity of Seperator Gas: ")
T = input("Input Reservoir Temperature in F: ")
API = input("Input API gravity of Stock Tank Oil: ")

CNpb = (Rs/SGg)**0.83*10**(0.00091*T - 0.0125*API)
pb = 18.2*(CNpb-1.4)

print 'The Bubble Point Pressure is', pb, 'psia'

