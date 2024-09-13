#!/usr/bin/env python
# llh_to_ecef_.py
#
# Converts LLH reference frame components to ECEF
#
# Usage: python3 llh_to_ecef_.py lat_deg lon_deg _hae_km
#
# Written by Blake Batchelor, batchelorbh@vt.edu
# Other contributors: None
#
# Parameters:
#    lat_deg             Latitude in degrees
#    lon_deg             Longitude in degrees
#    hae_km              Height above reference ellipsoid in km
#
# Output:
#    Prints ECEF x, y, and z position vector components in km
#
# Revision history:
#    09/13/2024          Script created
#
###############################################################################

#Import relevant modules
import sys
from math import pi, sqrt, sin, cos

#Define constants
R_E_KM = 6378.1363 #[km]
E_E = 0.081819221456
DEG_TO_RAD = pi / 180.0

#Calculate denominator for SE and CE equations
def calc_denom(ecc, lat_rad):
   return sqrt(1 - ecc**2 * sin(lat_rad)**2)

#Pre-initialize input parameters
lat_deg = float('nan') #Input latitude [deg]
lon_deg = float('nan') #Input longitude [deg]
hae_km = float('nan') #Input height above ellipsoid [km]

#Arguments are strings by default
if len(sys.argv) == 4:
   lat_deg = float(sys.argv[1])
   lon_deg = float(sys.argv[2])
   hae_km = float(sys.argv[3])
else:
   print('Usage: python3 llh_to_ecef_.py lat_deg lon_deg _hae_km')
   sys.exit()

#Main body of script

#Convert lat and lon to radians
lat_rad = lat_deg * DEG_TO_RAD
lon_rad = lon_deg * DEG_TO_RAD

#Calculate denominator for C_E and S_E equations
denom = calc_denom(E_E, lat_rad)

C_E = R_E_KM / denom
S_E = R_E_KM * (1 - E_E**2) / denom

#Find ECEF vector components
r_x_km = (C_E + hae_km) * cos(lat_rad) * cos(lon_rad)
r_y_km = (C_E + hae_km) * cos(lat_rad) * sin(lon_rad)
r_z_km = (S_E + hae_km) * sin(lat_rad)

#Print to screen
print(r_x_km)
print(r_y_km)
print(r_z_km)
