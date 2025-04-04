'''
Takes care of reporting (writing) output to netcdf files. Aggregates totals and averages for various time periods.
@author: Edwin H. Sutanudjaja

Created on Jul 28, 2014. 
This "reporting.py" module is not the same as the one module initiated by Niels Drost.
'''

import os
import logging
logger = logging.getLogger(__name__)
import pcraster as pcr
from ncConverter import *

import variable_list as varDicts


class Reporting(object):

    # list of all output variables
    
    def __init__(self, configuration, model, modelTime, sampleNumber=None):
        self._model = model
        self._modelTime = modelTime

        # output directory storing netcdf files:
        self.outNCDir = str(configuration.outNCDir)
        if sampleNumber is not None:
            self.outNCDir = self.outNCDir+str(sampleNumber) + "/"
            os.mkdir(self.outNCDir)
            logger.info("Creating folder " + str(sampleNumber) + " in netcdf output directory")
        print(self.outNCDir)
        # object for reporting:
        self.netcdfObj = PCR2netCDF(configuration)

        # initiating netcdf files for reporting
        #
        # - daily output in netCDF files:
        self.outDailyTotNC = ["None"]
        try:
            self.outDailyTotNC = configuration.reportingOptions['outDailyTotNC'].split(",")
        except:
            pass
        #
        if self.outDailyTotNC[0] != "None":
            for var in self.outDailyTotNC:
                
                logger.info("Creating the netcdf file for daily reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name
                
                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + str(var) + "_dailyTot_output.nc",
                                            short_name, unit, long_name)

        #
        # - SubSeasonal output in netCDF files:
        # -- cumulative
        self.outSeasoTotNC = ["None"]
        try:
            self.outSeasoTotNC = configuration.reportingOptions['outSeasoTotNC'].split(",")
        except:
            pass
        if self.outSeasoTotNC[0] != "None":
            for var in self.outSeasoTotNC:

                # initiating SubSeasonVarTot (accumulator variable):
                vars(self)[var+'SeasoTot'] = None

                logger.info("Creating the netcdf file for sub-season accumulation reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_monthly_total_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + "/" + str(var) + "_seasoTot_output.nc",
                                            short_name, unit, long_name)
        #
        # -- average
        self.outSeasoAvgNC = ["None"]
        try:
            self.outSeasoAvgNC = configuration.reportingOptions['outSeasoAvgNC'].split(",")
        except:
            pass
        if self.outSeasoAvgNC[0] != "None":

            for var in self.outSeasoAvgNC:

                # initiating SubSeasonTotAvg (accumulator variable)
                vars(self)[var+'SeasoTot'] = None

                # initiating monthlyVarAvg:
                vars(self)[var+'SeasoAvg'] = None

                logger.info("Creating the netcdf file for sub-season average reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + "/" + str(var) + "_seasoAvg_output.nc",
                                            short_name, unit, long_name)
        #
        # -- last day of the month
        self.outSeasoEndNC = ["None"]
        try:
            self.outSeasoEndNC = configuration.reportingOptions['outSeasoEndNC'].split(",")
        except:
            pass
        if self.outSeasoEndNC[0] != "None":

            for var in self.outSeasoEndNC:

                logger.info("Creating the netcdf file for sub-season end reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + "/" + str(var) + "_seasoEnd_output.nc",
                                            short_name, unit, long_name)
        #
        # - MONTHly output in netCDF files:
        # -- cumulative
        self.outMonthTotNC = ["None"]
        try:
            self.outMonthTotNC = configuration.reportingOptions['outMonthTotNC'].split(",")
        except:
            pass
        if self.outMonthTotNC[0] != "None":
            for var in self.outMonthTotNC:

                # initiating monthlyVarTot (accumulator variable):
                vars(self)[var+'MonthTot'] = None

                logger.info("Creating the netcdf file for monthly accumulation reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_monthly_total_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + "/" + str(var) + "_monthTot_output.nc",
                                            short_name, unit, long_name)
        #
        # -- average
        self.outMonthAvgNC = ["None"]
        try:
            self.outMonthAvgNC = configuration.reportingOptions['outMonthAvgNC'].split(",")
        except:
            pass
        if self.outMonthAvgNC[0] != "None":

            for var in self.outMonthAvgNC:

                # initiating monthlyTotAvg (accumulator variable)
                vars(self)[var+'MonthTot'] = None

                # initiating monthlyVarAvg:
                vars(self)[var+'MonthAvg'] = None

                logger.info("Creating the netcdf file for monthly average reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + "/" + str(var) + "_monthAvg_output.nc",
                                            short_name, unit, long_name)
        #
        # -- last day of the month
        self.outMonthEndNC = ["None"]
        try:
            self.outMonthEndNC = configuration.reportingOptions['outMonthEndNC'].split(",")
        except:
            pass
        if self.outMonthEndNC[0] != "None":

            for var in self.outMonthEndNC:

                logger.info("Creating the netcdf file for monthly end reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + "/" + str(var) + "_monthEnd_output.nc",
                                            short_name, unit, long_name)
        #
        # - YEARly output in netCDF files:
        # -- cumulative
        self.outAnnuaTotNC = ["None"]
        try:
            self.outAnnuaTotNC = configuration.reportingOptions['outAnnuaTotNC'].split(",")
        except:
            pass
        if self.outAnnuaTotNC[0] != "None":

            for var in self.outAnnuaTotNC:

                # initiating yearly accumulator variable:
                vars(self)[var+'AnnuaTot'] = None

                logger.info("Creating the netcdf file for annual accumulation reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_yearly_total_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir+"/" + str(var) + "_annuaTot_output.nc",
                                            short_name, unit, long_name)
        #
        # -- average
        self.outAnnuaAvgNC = ["None"]
        try:
            self.outAnnuaAvgNC = configuration.reportingOptions['outAnnuaAvgNC'].split(",")
        except:
            pass
        if self.outAnnuaAvgNC[0] != "None":

            for var in self.outAnnuaAvgNC:

                # initiating annualyVarAvg:
                vars(self)[var+'AnnuaAvg'] = None

                # initiating annualyTotAvg (accumulator variable)
                vars(self)[var+'AnnuaTot'] = None

                logger.info("Creating the netcdf file for annual average reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + "/" + str(var) + "_annuaAvg_output.nc",
                                            short_name, unit, long_name)
        #
        # -- last day of the year
        self.outAnnuaEndNC = ["None"]
        try:
            self.outAnnuaEndNC = configuration.reportingOptions['outAnnuaEndNC'].split(",")
        except:
            pass
        if self.outAnnuaEndNC[0] != "None":

            for var in self.outAnnuaEndNC:

                logger.info("Creating the netcdf file for annual end reporting for variable %s.", str(var))

                short_name = varDicts.netcdf_short_name[var]
                unit = varDicts.netcdf_unit[var]
                long_name = varDicts.netcdf_long_name[var]
                if long_name is None:
                    long_name = short_name

                # creating netCDF files:
                self.netcdfObj.createNetCDF(self.outNCDir + "/" + str(var) + "_annuaEnd_output.nc",
                                            short_name, unit, long_name)
        
        # list of variables that will be reported:
        self.variables_for_report = self.outDailyTotNC +\
                                    self.outSeasoTotNC +\
                                    self.outSeasoAvgNC +\
                                    self.outSeasoEndNC +\
                                    self.outMonthTotNC +\
                                    self.outMonthAvgNC +\
                                    self.outMonthEndNC +\
                                    self.outAnnuaTotNC +\
                                    self.outAnnuaAvgNC +\
                                    self.outAnnuaEndNC

    def post_processing(self):

        self.basic_post_processing() 
        self.additional_post_processing() 

    def basic_post_processing(self):

        self.precipitation = self._model.meteo.precipitation
        self.temperature = self._model.meteo.temperature
        self.referencePotET = self._model.meteo.referencePotET 

        # water body evaporation (m) - from surface water fractions only
        self.waterBodyActEvaporation = self._model.routing.waterBodyEvaporation
        self.waterBodyPotEvaporation = self._model.routing.waterBodyPotEvap
        #
        self.fractionWaterBodyEvaporation = vos.getValDivZero(self.waterBodyActEvaporation,
                                                              self.waterBodyPotEvaporation,
                                                              vos.smallNumber)
        
        # runoff (m) from land surface - not including local changes in water bodies
        self.runoff = self._model.routing.runoff
        
        # discharge (unit: m3/s)
        self.discharge = self._model.routing.disChanWaterBody
        
        # dynamic flooded fraction (-)
        self.dynamicFracWat = self._model.routing.dynamicFracWat
 
        # channel storage (K)
        self.channelStorage = self._model.routing.channelStorage

        # water height (K)
        self.waterHeight = self._model.routing.water_height

    def additional_post_processing(self):
        # In this method/function, users can add their own post-processing.

        # water temperature (K)
        if "waterTemp" in self.variables_for_report:
            self.waterTemp = self._model.routing.waterTemp

        # surface water temperature (K)
        if "surfaceWaterTemp" in self.variables_for_report:
            self.surfaceWaterTemp = self._model.routing.surfaceWaterTemp

        if "hypolimnionWaterTemp" in self.variables_for_report:
            self.hypolimnionWaterTemp = self._model.routing.hypolimnionWaterTemp

        # water velocity (m/s)
        if "waterVelocity" in self.variables_for_report:
            self.waterVelocity = self._model.routing.waterVelocity

        # ice thickness (K)
        if "iceThickness" in self.variables_for_report:
            self.iceThickness = self._model.routing.iceThickness

        # accumulated runoff (m3/s) along the drainage network - not including local changes in water bodies
        if "accuRunoff" in self.variables_for_report:
            self.accuRunoff =\
                pcr.catchmenttotal(self.runoff * self._model.routing.cellArea, self._model.routing.lddMap) /\
                vos.secondsPerDay()

        # accumulated baseflow (m3) along the drainage network
        if "accuBaseflow" in self.variables_for_report:
            self.accuBaseflow = pcr.catchmenttotal(self._model.baseflow * self._model.routing.cellArea,
                                                   self._model.routing.lddMap)

        # local changes in water bodies (i.e. abstraction, return flow, evaporation, bed exchange), excluding runoff
        self.local_water_body_flux = self._model.routing.local_input_to_surface_water /\
                                     self._model.routing.cellArea - self.runoff

        # total runoff (m) from local land surface runoff and local changes in water bodies
        # actually this is equal to self._model.routing.local_input_to_surface_water / self._model.routing.cellArea
        self.totalRunoff = self.runoff + self.local_water_body_flux

        # accumulated total runoff (m3) along the drainage network - not including local changes in water bodies
        if "accuTotalRunoff" in self.variables_for_report:
            self.accuTotalRunoff = pcr.catchmenttotal(self.totalRunoff * self._model.routing.cellArea,
                                                      self._model.routing.lddMap) / vos.secondsPerDay()

        # surfaceWaterStorage (unit: m) - negative values may be reported
        self.surfaceWaterStorage = self._model.routing.channelStorage / self._model.routing.cellArea

        # Stefanie's post processing: reporting lake and reservoir storage (unit: m3)
        # Note: This value is after lake/reservoir outflow.
        self.waterBodyStorage = pcr.ifthen(self._model.routing.landmask,
                                           pcr.ifthen(
                                               pcr.scalar(self._model.routing.WaterBodies.waterBodyIds) > 0.,
                                               self._model.routing.WaterBodies.waterBodyStorage))
        #
        # Water body variables
        if "waterBodyOutflow" in self.variables_for_report:
            self.waterBodyOutflow = self._model.routing.waterBodyOutflow

        # Flow statistics
        if "avgDischarge" in self.variables_for_report:
            self.avgDischarge = self._model.routing.avgDischarge

        if "avgOutflow" in self.variables_for_report:
            self.avgOutflow = self._model.routing.avgOutflow

        # Channel geometry
        if "wMean" in self.variables_for_report:
            self.wMean = self._model.routing.wMean

        if "tempWaterHeight" in self.variables_for_report:
            self.tempWaterHeight = self._model.routing.temp_water_height

        # Kinematic wave parameters
        if "alpha" in self.variables_for_report:
            self.alpha = self._model.routing.alpha

        # Energy balance terms
        #if "waterHeatTransfer" in self.variables_for_report:
        #    self.waterHeatTransfer = self._model.routing.waterHeatTransfer

        if "soilTemp" in self.variables_for_report:
            self.soilTemp = self._model.routing.soilTemperatureKelvin

        if "surfaceHeatTransfer" in self.variables_for_report:
            self.surfaceHeatTransfer = self._model.routing.surfaceHeatTransfer

        if "iceHeatTransfer" in self.variables_for_report:
            self.iceHeatTransfer = self._model.routing.iceHeatTransfer

        if "radiativeHeatTransfer" in self.variables_for_report:
            self.radiativeHeatTransfer = self._model.routing.radiativeHeatTransfer

        if "latentHeatTransfer" in self.variables_for_report:
            self.latentHeatTransfer = self._model.routing.latentHeatTransfer

        if "sensibleHeatTransfer" in self.variables_for_report:
            self.sensibleHeatTransfer = self._model.routing.sensibleHeatTransfer

        if "advectedEnergyInflow" in self.variables_for_report:
            self.advectedEnergyInflow = self._model.routing.advectedEnergyInflow

        if "advectedEnergyPrecip" in self.variables_for_report:
            self.advectedEnergyPrecip = self._model.routing.advectedEnergyPrecip

        if "dtotEWLoc" in self.variables_for_report:
            self.dtotEWLoc = self._model.routing.dtotEWLoc

        if "dtotEWAdv" in self.variables_for_report:
            self.dtotEWAdv = self._model.routing.dtotEWAdv

        if "totEW" in self.variables_for_report:
            self.totEW = self._model.routing.totEW

        if "totVolEW" in self.variables_for_report:
            self.totVolEW = self._model.routing.totalVolumeEW

        if "volEW" in self.variables_for_report:
            self.volEW = self._model.routing.volumeEW

        if "remVolEW" in self.variables_for_report:
            self.remVolEW = self._model.routing.remainingVolumeEW

        if "surfaceTemp" in self.variables_for_report:
            self.surfaceTemp = self._model.routing.surfaceTemp

        if "avgTempShort" in self.variables_for_report:
            self.avgTempShort = self._model.routing.avgTemperatureShort

        # Water quality
        if "O2" in self.variables_for_report:
            self.O2 = self._model.routing.O2

    def report(self):

        self.post_processing()

        # time stamp for reporting
        timeStamp = datetime.datetime(self._modelTime.year,
                                      self._modelTime.month,
                                      self._modelTime.day,
                                      0)

        # writing daily output to netcdf files
        if self.outDailyTotNC[0] != "None":
            for var in self.outDailyTotNC:
                short_name = varDicts.netcdf_short_name[var]
                self.netcdfObj.data2NetCDF(self.outNCDir + "/" + str(var) + "_dailyTot_output.nc",
                                           short_name,
                                           pcr2numpy(self.__getattribute__(var), vos.MV),
                                           timeStamp)

        # writing sub-season output to netcdf files
        # - cumulative
        if self.outSeasoTotNC[0] != "None":
            for var in self.outSeasoTotNC:
                # introduce variables at the beginning of simulation or
                #     reset variables at the beginning of the month
                if self._modelTime.timeStepPCR == 1 or self._modelTime.day == 1 or self._modelTime.day == 16:
                    vars(self)[var + 'SeasoTot'] = pcr.scalar(0.0)
                # accumulating
                vars(self)[var + 'SeasoTot'] += vars(self)[var]
                # reporting at the end of the month:
                if self._modelTime.endSubSeason == True:
                    short_name = varDicts.netcdf_short_name[var]
                    self.netcdfObj.data2NetCDF(self.outNCDir + "/" +str(var) + "_seasoTot_output.nc",
                                               short_name,
                                               pcr2numpy(self.__getattribute__(var + 'SeasoTot'), vos.MV),
                                               timeStamp)
        #
        # - average
        if self.outSeasoAvgNC[0] != "None":
            for var in self.outSeasoAvgNC:
                # only if a accumulator variable has not been defined: 
                if var not in self.outSeasoTotNC:
                    # introduce accumulator at the beginning of simulation or
                    #     reset accumulator at the beginning of the month
                    if self._modelTime.timeStepPCR == 1 or self._modelTime.day == 1 or self._modelTime.day == 16:\
                        vars(self)[var+'SeasoTot'] = pcr.scalar(0.0)
                    # accumulating
                    vars(self)[var+'SeasoTot'] += vars(self)[var]

                # calculating average & reporting at the end of the month:
                if self._modelTime.endSubSeason:
                    vars(self)[var+'SeasoAvg'] = vars(self)[var+'SeasoTot'] / self._modelTime.seasonLength
                    short_name = varDicts.netcdf_short_name[var]
                    self.netcdfObj.data2NetCDF(self.outNCDir + "/" + str(var) + "_seasoAvg_output.nc",
                                               short_name,
                                               pcr2numpy(self.__getattribute__(var + 'SeasoAvg'), vos.MV),
                                               timeStamp)
        #
        # - last day of the month
        if self.outSeasoEndNC[0] != "None":
            for var in self.outSeasoEndNC:
                # reporting at the end of the month:
                if self._modelTime.endSubSeason == True:
                    short_name = varDicts.netcdf_short_name[var]
                    self.netcdfObj.data2NetCDF(self.outNCDir + "/" + str(var) + "_seasoEnd_output.nc",
                                               short_name,
                                               pcr2numpy(self.__getattribute__(var), vos.MV),
                                               timeStamp)

        # writing monthly output to netcdf files
        # - cumulative
        if self.outMonthTotNC[0] != "None":
            for var in self.outMonthTotNC:
                # introduce variables at the beginning of simulation or
                #     reset variables at the beginning of the month
                if self._modelTime.timeStepPCR == 1 or self._modelTime.day == 1:
                    vars(self)[var + 'MonthTot'] = pcr.scalar(0.0)
                # accumulating
                vars(self)[var + 'MonthTot'] += vars(self)[var]
                # reporting at the end of the month:
                if self._modelTime.endMonth:
                    short_name = varDicts.netcdf_short_name[var]
                    self.netcdfObj.data2NetCDF(self.outNCDir + "/" + str(var) + "_monthTot_output.nc",
                                               short_name,
                                               pcr2numpy(self.__getattribute__(var + 'MonthTot'), vos.MV),
                                               timeStamp)
        #
        # - average
        if self.outMonthAvgNC[0] != "None":
            for var in self.outMonthAvgNC:
                # only if a accumulator variable has not been defined: 
                if var not in self.outMonthTotNC:
                    # introduce accumulator at the beginning of simulation or
                    #     reset accumulator at the beginning of the month
                    if self._modelTime.timeStepPCR == 1 or self._modelTime.day == 1:
                        vars(self)[var + 'MonthTot'] = pcr.scalar(0.0)
                    # accumulating
                    vars(self)[var + 'MonthTot'] += vars(self)[var]

                # calculating average & reporting at the end of the month:
                if self._modelTime.endMonth:
                    vars(self)[var + 'MonthAvg'] = vars(self)[var + 'MonthTot']/self._modelTime.day
                    short_name = varDicts.netcdf_short_name[var]
                    self.netcdfObj.data2NetCDF(self.outNCDir + "/"+ str(var) + "_monthAvg_output.nc",
                                               short_name,
                                               pcr2numpy(self.__getattribute__(var + 'MonthAvg'), vos.MV),
                                               timeStamp)
        #
        # - last day of the month
        if self.outMonthEndNC[0] != "None":
            for var in self.outMonthEndNC:
                # reporting at the end of the month:
                if self._modelTime.endMonth:
                    short_name = varDicts.netcdf_short_name[var]
                    self.netcdfObj.data2NetCDF(self.outNCDir + "/" + str(var) + "_monthEnd_output.nc",
                                               short_name,
                                               pcr2numpy(self.__getattribute__(var), vos.MV),
                                               timeStamp)

        # writing yearly output to netcdf files
        # - cumulative
        if self.outAnnuaTotNC[0] != "None":
            for var in self.outAnnuaTotNC:
                # introduce variables at the beginning of simulation or
                #     reset variables at the beginning of the month
                if self._modelTime.timeStepPCR == 1 or self._modelTime.doy == 1:
                    vars(self)[var + 'AnnuaTot'] = pcr.scalar(0.0)
                # accumulating
                vars(self)[var + 'AnnuaTot'] += vars(self)[var]
                # reporting at the end of the year:
                if self._modelTime.endYear:
                    short_name = varDicts.netcdf_short_name[var]
                    self.netcdfObj.data2NetCDF(self.outNCDir + "/" + str(var) + "_annuaTot_output.nc",
                                               short_name,
                                               pcr2numpy(self.__getattribute__(var+'AnnuaTot'), vos.MV),
                                               timeStamp)

        # - average
        if self.outAnnuaAvgNC[0] != "None":
            for var in self.outAnnuaAvgNC:
                # only if a accumulator variable has not been defined: 
                if var not in self.outAnnuaTotNC:
                    # introduce accumulator at the beginning of simulation or
                    #     reset accumulator at the beginning of the year
                    if self._modelTime.timeStepPCR == 1 or self._modelTime.doy == 1:
                        vars(self)[var + 'AnnuaTot'] = pcr.scalar(0.0)
                    # accumulating
                    vars(self)[var + 'AnnuaTot'] += vars(self)[var]

                # calculating average & reporting at the end of the year:
                if self._modelTime.endYear:
                    vars(self)[var + 'AnnuaAvg'] = vars(self)[var+'AnnuaTot']/self._modelTime.doy
                    short_name = varDicts.netcdf_short_name[var]
                    self.netcdfObj.data2NetCDF(self.outNCDir + "/" + str(var) + "_annuaAvg_output.nc",
                                               short_name,
                                               pcr2numpy(self.__getattribute__(var+'AnnuaAvg'), vos.MV),
                                               timeStamp)
        #
        # -last day of the year
        if self.outAnnuaEndNC[0] != "None":
            for var in self.outAnnuaEndNC:
                short_name = varDicts.netcdf_short_name[var]
                self.netcdfObj.data2NetCDF(self.outNCDir + "/" + str(var) + "_annuaEnd_output.nc",
                                           short_name,
                                           pcr2numpy(self.__getattribute__(var), vos.MV),
                                           timeStamp)

        logger.info("reporting for time %s", self._modelTime.currTime)
