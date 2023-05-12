'''
List of variables.

Created on July 7, 2014

@author: Edwin H. Sutanudjaja
'''

netcdf_short_name = {}
netcdf_unit       = {}
netcdf_monthly_total_unit = {} 
netcdf_yearly_total_unit  = {}
netcdf_long_name  = {}
description       = {}
comment           = {}
latex_symbol      = {}

# precipitation
pcrglobwb_variable_name = 'precipitation'
netcdf_short_name[pcrglobwb_variable_name] = 'lwe_thickness_of_precipitation_amount'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'precipitation'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# air temperature
pcrglobwb_variable_name = 'temperature'
netcdf_short_name[pcrglobwb_variable_name] = 'air_temperature'
netcdf_unit[pcrglobwb_variable_name]       = 'degrees Celsius'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'air temperature'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Short-term average sir temperature
pcrglobwb_variable_name = 'avgTemperatureShort'
netcdf_short_name[pcrglobwb_variable_name] = 'air_temperature'
netcdf_unit[pcrglobwb_variable_name]       = 'degrees Celsius'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'short-term average air temperature'
description[pcrglobwb_variable_name]       = 'Running average of air temperature'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# referencePotET
pcrglobwb_variable_name = 'referencePotET'
netcdf_short_name[pcrglobwb_variable_name] = 'reference_potential_evaporation'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'reference potential evaporation'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# directRunoff                    
pcrglobwb_variable_name = 'directRunoff'
netcdf_short_name[pcrglobwb_variable_name] = 'thickness_of_surface_runoff_amount'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'surface runoff'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# interflowTotal                  
pcrglobwb_variable_name = 'interflowTotal'
netcdf_short_name[pcrglobwb_variable_name] = 'thickness_of_interflow_amount'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'interflow'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# baseflow                  
pcrglobwb_variable_name = 'baseflow'
netcdf_short_name[pcrglobwb_variable_name] = 'thickness_of_baseflow_amount'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'baseflow'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# waterBodyActEvaporation
pcrglobwb_variable_name = 'waterBodyActEvaporation'
netcdf_short_name[pcrglobwb_variable_name] = 'lwe_thickness_of_water_evaporation_amount'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'actual evaporation from water bodies'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Flux values given are over the entire cell area (not only over surface water body fraction).'
latex_symbol[pcrglobwb_variable_name]      = None

# waterBodyPotEvaporation
pcrglobwb_variable_name = 'waterBodyPotEvaporation'
netcdf_short_name[pcrglobwb_variable_name] = 'lwe_thickness_of_potential_water_evaporation_amount'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'potential evaporation from water bodies'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Flux values given are over the entire cell area (not only over surface water body fraction).'
latex_symbol[pcrglobwb_variable_name]      = None

# totalEvaporation
#pcrglobwb_variable_name = 'totalEvaporation'
#netcdf_short_name[pcrglobwb_variable_name] = 'total_evaporation'
#netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
#netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1'
#netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
#netcdf_long_name[pcrglobwb_variable_name]  = 'surface_water_evaporation_flux'
#description[pcrglobwb_variable_name]       = None
#comment[pcrglobwb_variable_name]           = 'Including from water bodies.'
#latex_symbol[pcrglobwb_variable_name]      = None

# runoff
pcrglobwb_variable_name = 'runoff'
netcdf_short_name[pcrglobwb_variable_name] = 'lwe_thickness_of_runoff_amount'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'runoff from land'
description[pcrglobwb_variable_name]       = 'direct_runoff + interflow + baseflow, but not including local runoff from water bodies.'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# accuRunoff
pcrglobwb_variable_name = 'accuRunoff'
netcdf_short_name[pcrglobwb_variable_name] = 'accumulated_runoff_flux'
netcdf_unit[pcrglobwb_variable_name]       = 'm3.s-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'accumulated runoff'
description[pcrglobwb_variable_name]       = 'Accumulated runoff along the drainage network,not including local changes in water bodies'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# accuBaseflow
pcrglobwb_variable_name = 'accuBaseflow'
netcdf_short_name[pcrglobwb_variable_name] = 'accumulated_baseflow_amount'
netcdf_unit[pcrglobwb_variable_name]       = 'm3.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = "m3.month-1" 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = "m3.year-1"
netcdf_long_name[pcrglobwb_variable_name]  = 'accumulated baseflow'
description[pcrglobwb_variable_name]       = 'accumulated baseflow along the drainage network'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# discharge
pcrglobwb_variable_name = 'discharge'
netcdf_short_name[pcrglobwb_variable_name] = 'discharge'
netcdf_unit[pcrglobwb_variable_name]       = 'm3.s-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'discharge'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# totalRunoff
pcrglobwb_variable_name = 'totalRunoff'
netcdf_short_name[pcrglobwb_variable_name] = 'total_runoff'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = 'total runoff'
description[pcrglobwb_variable_name]       = 'Total runoff from local land surface runoff and local changes in water bodies'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# local_water_body_flux
pcrglobwb_variable_name = 'local_water_body_flux'
netcdf_short_name[pcrglobwb_variable_name] = 'local_water_body_flux'
netcdf_unit[pcrglobwb_variable_name]       = 'm.day-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = 'm.month-1' 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = 'm.year-1'
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# accuTotalRunoff
pcrglobwb_variable_name = 'accuTotalRunoff'
netcdf_short_name[pcrglobwb_variable_name] = 'accumulated_total_surface_runoff'
netcdf_unit[pcrglobwb_variable_name]       = 'm3.s-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = "Including runoff from water bodies."
latex_symbol[pcrglobwb_variable_name]      = None

# surfaceWaterStorage
pcrglobwb_variable_name = 'surfaceWaterStorage'
netcdf_short_name[pcrglobwb_variable_name] = 'surface_water_storage'
netcdf_unit[pcrglobwb_variable_name]       = 'm'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Negative values may be reported, due to excessive demands.'
latex_symbol[pcrglobwb_variable_name]      = None

# waterBodyStorage 
pcrglobwb_variable_name = 'waterBodyStorage'
netcdf_short_name[pcrglobwb_variable_name] = 'lake_and_reservoir_storage'
netcdf_unit[pcrglobwb_variable_name]       = 'm3'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'water body storage'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'The values given are for every lake and reservoir ids (not per cells) and after lake/reservoir releases/outflows.'
latex_symbol[pcrglobwb_variable_name]      = None

# waterBodyOutflow
pcrglobwb_variable_name = 'waterBodyOutflow'
netcdf_short_name[pcrglobwb_variable_name] = 'waterbody_outflow'
netcdf_unit[pcrglobwb_variable_name]       = 'm3'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Values given at the outlet of every lake and reservoir.'
latex_symbol[pcrglobwb_variable_name]      = None

# Dynamic water fraction
pcrglobwb_variable_name = 'dynamicFracWat'
netcdf_short_name[pcrglobwb_variable_name] = 'dynamic_water_fraction'
netcdf_unit[pcrglobwb_variable_name]       = '1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'fraction of cell flooded'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Flooded fraction is a combination of channel, waterbody and floodplain'
latex_symbol[pcrglobwb_variable_name]      = None

# Water temperature
pcrglobwb_variable_name = 'waterTemp'
netcdf_short_name[pcrglobwb_variable_name] = 'waterTemperature'
netcdf_unit[pcrglobwb_variable_name]       = 'K'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None 
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'surface temperature where open water'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Surface water temperature assuming fully mixed conditions'
latex_symbol[pcrglobwb_variable_name]      = None

# Ice Thickness
pcrglobwb_variable_name = 'iceThickness'
netcdf_short_name[pcrglobwb_variable_name] = 'iceThickness'
netcdf_unit[pcrglobwb_variable_name]       = 'm'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'thickness of ice layer'
description[pcrglobwb_variable_name]       = 'Thickness of ice layer on channel network'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Channel width
pcrglobwb_variable_name = 'wMean'
netcdf_short_name[pcrglobwb_variable_name] = 'wMean'
netcdf_unit[pcrglobwb_variable_name]       = 'm'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'channel width'
description[pcrglobwb_variable_name]       = 'Mean channel width'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Channel storage
pcrglobwb_variable_name = 'channelStorage'
netcdf_short_name[pcrglobwb_variable_name] = 'channelStorage'
netcdf_unit[pcrglobwb_variable_name]       = 'm3'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'total in channel storage'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Riverine channel storage, values include reservoirs and lakes'
latex_symbol[pcrglobwb_variable_name]      = None

# Water height
pcrglobwb_variable_name = 'waterHeight'
netcdf_short_name[pcrglobwb_variable_name] = 'waterHeight'
netcdf_unit[pcrglobwb_variable_name]       = 'm'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'water height in the channle'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Water height in channel, values include reservoirs and lakes'
latex_symbol[pcrglobwb_variable_name]      = None

# Water velocity
pcrglobwb_variable_name = 'waterVelocity'
netcdf_short_name[pcrglobwb_variable_name] = 'waterVelocity'
netcdf_unit[pcrglobwb_variable_name]       = 'm.s-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'Average_water_velocity'
description[pcrglobwb_variable_name]       = 'Average water velocity in channels and lakes'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Temporary water height
pcrglobwb_variable_name = 'tempWaterHeight'
netcdf_short_name[pcrglobwb_variable_name] = 'tempWaterHeight'
netcdf_unit[pcrglobwb_variable_name]       = 'm'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = 'Temporary water height in channel for water temperature calculation'
latex_symbol[pcrglobwb_variable_name]      = None

# Long-term average discharge
pcrglobwb_variable_name = 'avgDischarge'
netcdf_short_name[pcrglobwb_variable_name] = 'avgDischarge'
netcdf_unit[pcrglobwb_variable_name]       = 'm3.s-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'long-term average discharge'
description[pcrglobwb_variable_name]       = None
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Water heat transfer to/from atmosphere
#pcrglobwb_variable_name = 'waterHeatTransfer'
#netcdf_short_name[pcrglobwb_variable_name] = 'waterHeatTransfer'
#netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
#netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
#netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
#netcdf_long_name[pcrglobwb_variable_name]  = None
#description[pcrglobwb_variable_name]       = None
#comment[pcrglobwb_variable_name]           = 'Sensible heat transfer at water surface'
#latex_symbol[pcrglobwb_variable_name]      = None

# Soil temperature (K)
pcrglobwb_variable_name = 'soilTemp'
netcdf_short_name[pcrglobwb_variable_name] = 'soil_temperature'
netcdf_unit[pcrglobwb_variable_name]       = 'K'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'soil temperature'
description[pcrglobwb_variable_name]       = 'bulk temperature of the soil layer'
comment[pcrglobwb_variable_name]           = 'Proxy for baseflow temperature'
latex_symbol[pcrglobwb_variable_name]      = None

# Net surface heat transfer to/from atmosphere
pcrglobwb_variable_name = 'surfaceHeatTransfer'
netcdf_short_name[pcrglobwb_variable_name] = 'surfaceHeatTransfer'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'surface downward heat flux in air'
description[pcrglobwb_variable_name]       = 'Net heat transfer at water or ice surface'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Heat transfer from water to ice
pcrglobwb_variable_name = 'iceHeatTransfer'
netcdf_short_name[pcrglobwb_variable_name] = 'iceHeatTransfer'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'ice heat transfer'
description[pcrglobwb_variable_name]       = 'Heat transfer to ice form water'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Radiative heat transfer at water surface
pcrglobwb_variable_name = 'radiativeHeatTransfer'
netcdf_short_name[pcrglobwb_variable_name] = 'radiativeHeatTransfer'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'surface downward net radiation heat flux'
description[pcrglobwb_variable_name]       = 'Net radiation flux at water or ice surface'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Latent heat transfer at water surface
pcrglobwb_variable_name = 'latentHeatTransfer'
netcdf_short_name[pcrglobwb_variable_name] = 'latentHeatTransfer'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'surface downward latent heat flux'
description[pcrglobwb_variable_name]       = 'Latent heat flux at open water surfaces'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Sensible heat transfer at water surface
pcrglobwb_variable_name = 'sensibleHeatTransfer'
netcdf_short_name[pcrglobwb_variable_name] = 'sensibleHeatTransfer'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'surface downward sensible heat flux'
description[pcrglobwb_variable_name]       = 'Sensible heat flux at water or ice surface'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Advected energy from runoff
pcrglobwb_variable_name = 'advectedEnergyInflow'
netcdf_short_name[pcrglobwb_variable_name] = 'advectedEnergyInflow'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = 'Advected energy from land runoff'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Advected energy from precipitation and ice melt
pcrglobwb_variable_name = 'advectedEnergyPrecip'
netcdf_short_name[pcrglobwb_variable_name] = 'advectedEnergyPrecip'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = 'Advected energy from precipitation and ice melt'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Change in energy storage from local surface energy balance
pcrglobwb_variable_name = 'dtotEWLoc'
netcdf_short_name[pcrglobwb_variable_name] = 'dtotEWLoc'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = 'Change in energy storage from local surface energy balance'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Change in energy storage from local advected energy
pcrglobwb_variable_name = 'dtotEWAdv'
netcdf_short_name[pcrglobwb_variable_name] = 'dtotEWAdv'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = 'Change in energy storage from local advected energy'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Total energy storage
pcrglobwb_variable_name = 'totEW'
netcdf_short_name[pcrglobwb_variable_name] = 'totEW'
netcdf_unit[pcrglobwb_variable_name]       = 'W.m-2'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'total energy storage'
description[pcrglobwb_variable_name]       = 'Total energy storage'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Surface temperature
pcrglobwb_variable_name = 'surfaceTemp'
netcdf_short_name[pcrglobwb_variable_name] = 'surfaceTemp'
netcdf_unit[pcrglobwb_variable_name]       = 'K'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = 'surface temperature'
description[pcrglobwb_variable_name]       = 'Surface temperature of water or ice'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Kinematic wave parameter alpha
pcrglobwb_variable_name = 'alpha'
netcdf_short_name[pcrglobwb_variable_name] = 'alpha'
netcdf_unit[pcrglobwb_variable_name]       = '1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = 'Channel area coefficient for kinematic wave, where Area = alpha*Q**beta'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

# Saturation dissolved oxygen content
pcrglobwb_variable_name = 'O2'
netcdf_short_name[pcrglobwb_variable_name] = 'satOxygenContent'
netcdf_unit[pcrglobwb_variable_name]       = 'mg.L-1'
netcdf_monthly_total_unit[pcrglobwb_variable_name] = None
netcdf_yearly_total_unit[pcrglobwb_variable_name]  = None
netcdf_long_name[pcrglobwb_variable_name]  = None
description[pcrglobwb_variable_name]       = 'Equilibrium oxygen concentration at non-standard pressure'
comment[pcrglobwb_variable_name]           = None
latex_symbol[pcrglobwb_variable_name]      = None

#~ # remove/clear pcrglobwb_variable_name
#~ pcrglobwb_variable_name = None
#~ del pcrglobwb_variable_name
