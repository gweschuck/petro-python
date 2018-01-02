#!/usr/bin/env python

"""bubble-point-pressure-black-oil-2.py: from William D. McCain, Jr.
This is for finding the bubble-point pressure-solution gas-oil ratio
from Appendix B-39 Equation, temperature is in R, Separator solution
gas oil (Rsp) is in standard cubic feet per stock tank barrel scf/STB
, SGg is the specific gravity of the separator gas SGst is the specific
gravity of the stock tank oil, bubble point pressure is in psia."""

__author__ = "Wesley C. Williams"
__copyright__ = "Copyright 2007, Wesley C. Williams"
__credits__ = ["Wesley C. Williams"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wesley C. Williams"
__email__ = "wcwmit@gmail.com"
__status__ = "Production"

Rsp = input("Input Separator Solution Gas Oil Ratio (Rsp) in SCF/STB: ")
SGg = input("Input Specific Gravity of Seperator Gas: ")
T = input("Input Reservoir Temperature in R: ")
SGst = input("Input Specific gravity of Stock Tank Oil: ")

A1 = 5.38033 * 10**-3
A2 = 0.715082
A3 = -1.877840
A4 = 3.143700
A5 = 1.326570

pb = A1*Rsp**A2*SGg**A3*SGst**A4*T**A5

print 'The Bubble Point Pressure is', pb, 'psia'

