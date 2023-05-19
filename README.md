# waterTemperatureModel
Modified version of the DynWat Model (https://github.com/wande001/dynWat)

Main updates include:
1) Local energy balance
   - Updated code to read daily shortwave radiation, instead of using annual solar radiation climatology and daily cloud cover
   - replaced annual mean air temperature with 365-day running average air temperature
   - replaced constant atmospheric emissivity with estimate based on air tempearture and vapor pressure as per Idso (1981).
   - Split directRunoff to account for rain and melt sources, with different source temperatures for each (which is used to set landT). This adds additional parameter deltaTMelt.
   - Include actual precipitation amount (instead of default value of 0.0) for estimates of advected energy.
   - Uses three methods of estimating soil temperature, which is used as a proxy for the temperature of baseflow.
      - The original method uses a daily running mean of annual air temperature. The choice of annual air temperature ('annualT') requires a separate forcing file (assumed to be a daily running mean of annual air temperature).
      - The second method uses a smoothing function of daily air temperature (Tsoil(t) = (1-kappa)*Tsoil(t-1) + kappa*Tair(t)). The choice of smoothing ('smoothT') requires specification of the smoothing parameter kappa and an initial soil temperature map (or a default spatially uniform value, which is hardcoded). If choice is 'smoothT' code also dumps soil temperature to state.
      - The third method uses the Mohseni et al. 4-parameter non-linear model which was originally designed to predict stream tempearture as a fucntion of air temperature. With this method Tsoil(t) = mew + (alpha - mew)/(1 + exp(gamma*(beta - Ta))), where Ta is the running mean air temperature over the period t, t-1, t-2, ..., t-n-1, where n is the averaging period in days. If 'this method is selcted, deltaTMelt is not treated as a parameters, but is instead specified as a fraction on Tsoil, i.e. deltaTMelt(t) = f*Tsoil(t). The choice of 'mohseni' requires specification of the four regression parameters, the averaging period, n, and the deltaTMelt fraction, f. The choice of 'mohseni' requires an initial average air tempaerature map (or a default spatially uniform value, which is hardcoded), and a initial number of timesteps for estimating initial average air tempearture (or a default of n is assumed).
      - The choice of the soil temperature method and required inputs/paramters (e.g. annual air temperature input file, soil temperature initial state and kappa, or average air temperature initial state and timesteps to average tempearture initial state) are specified in the configuration file.
   - replaced empirical heat transfer to water with turbulent exchange of sensible heat (for both ice and water surfaces), including stability correction based on bulk Richardson approach
2) Adopted model of Shen and Chiang (1984) for growth and decay of river ice, plus additional refinements. Modifications include:
   - ice surface temperature determined analytically from previous surface energy balance and ice thickness (as opposed to using air temperature)
   - replaced empirical heat transfer to ice with semi-empirical approach that accounts for water velocity and depth
   - estimate water velocity from discharge and channel geometry, which is derived from channel storage and water surface area
   - separate thickness change calculations for ice surface (melt only) and ice bottom (melt or growth)
   - fraction of solar radiation assumed to penetrate through the ice based on bulk extinction coefficient
   - thermal conductivity of ice calculated as function of ice temperature
4) Moved channel geometry parameters from code to configuration file
5) Allow dynamic channel geometry
6) Waterbodies:
   - Waterbody outflow geometry now consistent with channel geometry for natural lakes.
   - Ensure that fracWat (fraction of reservoir/lake surface area in each cell) is scaled to be consistent with water body surface area provided separately.
   - When using natural lakes only, static date to read waterBody netCDF file now set to run startDate, as opposed to hard coded value of '1900-01-01'.
   - Weir coefficient specified as a parameter in the initialization file. Can be read as a *.map file or as a constant value.
   - Removed all default 'minimum' lake outflow settings. Lake outflow is now strictly a function of live storage (storage above sill elevation), where 0.0 <= lakeOutflow <= liveStorage (i.e. lake outflow can be zero and maximum outflow limited to live storage volume). 
