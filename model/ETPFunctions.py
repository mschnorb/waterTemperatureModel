#! /usr/bin/python

import pcraster as pcr
import math
#  LET OP!! PCR Pythong computes trigonometric function in degres by default. UNLIKE C, UNLIKE PYTON!
# Convert all arguments to deg using * 180 / pi

def HargreavesPotET(Tmax, Tmin, doy, lat):
    avgT = (Tmax + Tmin)/2 + 17.8
    cloudFrac = pcr.sqrt(Tmax - Tmin) * Ra(doy,lat)
    pet = pcr.cover(0.0023 * avgT *cloudFrac / 1000, 0.0)
    return pet

def Ra(doy,lat):
    constant = (24*60.)/math.pi * 0.082 * invRelSolarDistance(doy)
    variable = (sunsetAngle(doy,lat)*pcr.scalar(pcr.sin(lat)*math.sin(solarDistance(doy))) + pcr.sin(sunsetAngle(doy,lat)*180/math.pi)*pcr.cos(lat)*math.cos(solarDistance(doy)))
    radiation = constant * variable
    return radiation * 0.408

def solarDistance(doy):
    dis = 0.409*math.sin((2*math.pi*doy)/365 - 1.39)
    return dis

def invRelSolarDistance(doy):
    invDis = 1+ 0.033*math.cos((2*math.pi*doy)/365)
    return invDis

def sunsetAngle(doy,lat):
    sunAngle = pcr.scalar(pcr.acos(-pcr.tan(lat) * math.tan(solarDistance(doy))))/180.*math.pi
    return sunAngle

def HamonPotET(airT,doy,lat):
    rhoSat =  2.167 * satPressure (airT) / (airT + 273.15)
    dayLen = dayLength(doy,lat)
    pet     = 165.1 * 2.0 * dayLen * rhoSat # // 2 * DAYLEN = daylength as frac
    pet = pet / 1000 # in meters!
    return pet

def dayLength(doy,lat):
    """ daylength fraction of day  """
    lat = lat * pcr.scalar(math.pi) /  180.0
    M_PI_2 = pcr.spatial(pcr.scalar(math.pi / 2))
    dec = pcr.sin( (6.224111 + 0.017202  * doy) *  180 / math.pi)
    dec = pcr.scalar(0.39785 * pcr.sin ((4.868961 + .017203 *  doy + 0.033446 * pcr.sin (dec*   180 / math.pi)) *  180 / math.pi))
    dec = pcr.scalar(pcr.asin(dec))
    lat = pcr.ifthenelse(pcr.abs(lat) > M_PI_2, (M_PI_2 - pcr.scalar(0.01)) * pcr.ifthenelse(lat > 0,  pcr.scalar(1.0), pcr.scalar(-1.0))  ,lat )
    arg = pcr.tan(dec ) *  pcr.tan(lat * 180.0 / math.pi  ) * -1
    h = pcr.scalar( pcr.acos(arg ) )
    h = h / 180 * math.pi
    h = pcr.ifthenelse(arg > 1.0, 0.0,h) # /* sun stays below horizon */
    h = pcr.ifthenelse(arg <  -1.0 ,math.pi,h) # /* sun stays above horizon */
    return (h /  math.pi)

def satPressure ( airT):
    """ calculates saturated vp from airt temperature Murray (1967) """
    # airT      - air temperature [degree C] */
    satPressure = pcr.ifthenelse(airT >= 0.0 , 0.61078 * pcr.exp (17.26939 * airT / (airT + 237.3)),
                                 0.61078 * pcr.exp (21.87456 * airT / (airT + 265.5)))
    return satPressure

