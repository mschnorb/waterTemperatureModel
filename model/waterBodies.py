#!/usr/bin/ python
# -*- coding: utf-8 -*-

import virtualOS as vos

from pcraster.framework import *
import pcraster as pcr

import logging
logger = logging.getLogger(__name__)


class WaterBodies(object):

    def __init__(self, iniItems, landmask, minChannelWidth):
        object.__init__(self)

        # clone map file names, temporary directory and global/absolute path of input directory
        self.cloneMap = iniItems.cloneMap
        self.tmpDir = iniItems.tmpDir
        self.inputDir = iniItems.globalOptions['inputDir']
        self.landmask = landmask

        # option to activate water balance check
        self.debugWaterBalance = True
        if iniItems.routingOptions['debugWaterBalance'] == "False":
            self.debugWaterBalance = False

        # option to perform a run with only natural lakes (without reservoirs)
        self.onlyNaturalWaterBodies = False
        if "onlyNaturalWaterBodies" in iniItems.routingOptions.keys() and \
                iniItems.routingOptions['onlyNaturalWaterBodies'] == "True":
            logger.info("WARNING!! Using only natural water bodies identified at start year."
                        "All reservoirs at start year are assumed as lakes.")
            self.onlyNaturalWaterBodies = True
            # The run for a natural condition should access only the start date.
            self.dateForNaturalCondition = iniItems.globalOptions['startTime']

        # names of files containing water bodies parameters
        if iniItems.routingOptions['waterBodyInputNC'] == str(None):
            self.useNetCDF = False
            self.fracWaterInp = iniItems.routingOptions['fracWaterInp']
            self.waterBodyIdsInp = iniItems.routingOptions['waterBodyIds']
            self.waterBodyTypInp = iniItems.routingOptions['waterBodyTyp']
            self.resMaxCapInp = iniItems.routingOptions['resMaxCapInp']
            self.resSfAreaInp = iniItems.routingOptions['resSfAreaInp']
            self.waterBodyShF = iniItems.routingOptions['waterBodyShF']
        else:
            self.useNetCDF = True
            self.ncFileInp = vos.getFullPath(iniItems.routingOptions['waterBodyInputNC'], self.inputDir)

        # Parameters for weir formula
        self.minWeirWidth = minChannelWidth  # minimum width (m) used in the weir formula
        self.weirCoeff = vos.readPCRmapClone(iniItems.routingOptions['weirCoeff'],
                                             self.cloneMap, self.tmpDir, self.inputDir)

        # lower and upper limits at which reservoir release is terminated and
        # at which reservoir release is equal to long-term average outflow
        self.minResvrFrac = 0.10
        self.maxResvrFrac = 0.75

    def getParameterFiles(self, currTimeStep, cellArea, ldd,
                          cellLengthFD, cellSizeInArcDeg,
                          initial_condition_dictionary=None):

        # parameters for Water Bodies: fracWat              
        #                              waterBodyIds
        #                              waterBodyOut
        #                              waterBodyArea 
        #                              waterBodyTyp
        #                              waterBodyCap

        # cell surface area (m2) and ldd
        self.cellArea = cellArea
        ldd = pcr.ifthen(self.landmask, ldd)

        # date used for accessing/extracting water body information
        date_used = currTimeStep.fulldate
        year_used = currTimeStep.year
        if self.onlyNaturalWaterBodies:
            date_used = self.dateForNaturalCondition
            year_used = self.dateForNaturalCondition[0:4]

        # Initialise variables
        self.waterBodyIds = pcr.nominal(0)   # waterBody ids
        self.waterBodyOut = pcr.boolean(0)   # waterBody outlets
        self.waterBodyTyp = pcr.nominal(0)   # water body types
        self.fracWat = pcr.scalar(0.0)       # fraction of surface water bodies (dimensionless)
        self.waterBodyArea = pcr.scalar(0.)  # waterBody surface areas
        self.waterBodyShapeFactor = pcr.scalar(0)
        self.resMaxCap = pcr.scalar(0.0)     # reservoir maximum capacity (m3)
        self.waterBodyCap = pcr.scalar(0.0)  # lake/reservoir maximum capacity (m3)

        # water body ids
        if self.useNetCDF:
            self.waterBodyIds = vos.netcdf2PCRobjClone(self.ncFileInp, 'waterBodyIds',
                                                       date_used, useDoy='yearly',
                                                       cloneMapFileName=self.cloneMap)
        else:
            self.waterBodyIds = vos.readPCRmapClone(self.waterBodyIdsInp+str(year_used)+".map",
                                                    self.cloneMap, self.tmpDir, self.inputDir,
                                                    False, None, True)
        self.waterBodyIds = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0., pcr.nominal(self.waterBodyIds))

        # water body outlets (correcting outlet positions)
        wbCatchment = pcr.catchmenttotal(pcr.scalar(1), ldd)
        self.waterBodyOut = pcr.ifthen(wbCatchment == pcr.areamaximum(wbCatchment, self.waterBodyIds),
                                       self.waterBodyIds)     # = outlet ids
        self.waterBodyOut = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0., self.waterBodyOut)

        # - make sure that there is only one outlet for each water body
        self.waterBodyOut = pcr.ifthen(pcr.areaorder(pcr.scalar(self.waterBodyOut),
                                                     self.waterBodyOut) == 1., self.waterBodyOut)
        self.waterBodyOut = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0., self.waterBodyOut)

        # TODO: Please also consider endorheic lakes!
        # correction for multiple outlet reservoirs
        # self.waterBodyIds = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0.,
        #                    pcr.subcatchment(ldd,\
        #                    pcr.nominal(pcr.uniqueid(pcr.boolean(self.waterBodyOut)))))
        #self.waterBodyIds = pcr.ifthen(\
        #                    pcr.scalar(self.waterBodyIds) > 0.,\
        #                    pcr.subcatchment(ldd,self.waterBodyOut))

        # boolean map for water body outlets:
        self.waterBodyOut = pcr.ifthen(pcr.scalar(self.waterBodyOut) > 0., pcr.boolean(1))

        # fraction of surface water bodies
        if self.useNetCDF:
            self.fracWat = vos.netcdf2PCRobjClone(self.ncFileInp, 'fracWaterInp',
                                                  date_used, useDoy='yearly',
                                                  cloneMapFileName=self.cloneMap)
        else:
            self.fracWat = vos.readPCRmapClone(self.fracWaterInp+str(year_used)+".map",
                                               self.cloneMap,self.tmpDir,self.inputDir)
        self.fracWat = pcr.cover(self.fracWat, 0.0)
        self.fracWat = pcr.max(0.0, self.fracWat)
        self.fracWat = pcr.min(1.0, self.fracWat)
        surfAreaFromFrac = pcr.areatotal(pcr.cover(self.fracWat * self.cellArea, 0.0), self.waterBodyIds)

        # reservoir surface area (m2):
        if self.useNetCDF:
            resSfArea = 1000. * 1000. * vos.netcdf2PCRobjClone(self.ncFileInp, 'resSfAreaInp',
                                                               date_used, useDoy='yearly',
                                                               cloneMapFileName=self.cloneMap)
        else:
            resSfArea = 1000. * 1000. * vos.readPCRmapClone(self.resSfAreaInp+str(year_used)+".map",
                                                            self.cloneMap,self.tmpDir,self.inputDir)
        resSfArea = pcr.cover(pcr.areaaverage(resSfArea, self.waterBodyIds), 0.0)

        # water body surface area (m2): (lakes and reservoirs)
        self.waterBodyArea = pcr.max(surfAreaFromFrac, resSfArea)
        self.waterBodyArea = pcr.ifthen(self.waterBodyArea > 0., self.waterBodyArea)

        # Ensure fracWat consistent with waterBodyArea
        self.fracWat = self.fracWat * (self.waterBodyArea / surfAreaFromFrac)

        # relative fraction of cell to total waterbody fraction
        self.waterBodyRelativeFrac = pcr.cover(pcr.ifthen(
            pcr.scalar(self.waterBodyIds) > 0., self.fracWat/pcr.areatotal(self.fracWat, self.waterBodyIds)), 0.)
        # set in
        self.dynamicFracWat = self.fracWat

        # correcting water body ids and outlets (exclude all water bodies with surfaceArea = 0)
        self.waterBodyIds = pcr.ifthen(self.waterBodyArea > 0., self.waterBodyIds)
        self.waterBodyOut = pcr.ifthen(pcr.boolean(self.waterBodyIds), self.waterBodyOut)

        # water body types:
        # - 2 = reservoirs (regulated discharge)
        # - 1 = lakes (weirFormula)
        # - 0 = non lakes or reservoirs (e.g. wetland)
        if self.useNetCDF:
            self.waterBodyTyp = pcr.cover(vos.netcdf2PCRobjClone(self.ncFileInp, 'waterBodyTyp',
                                                                 date_used, useDoy='yearly',
                                                                 cloneMapFileName=self.cloneMap), pcr.scalar(0.0))
        else:
            self.waterBodyTyp = vos.readPCRmapClone(self.waterBodyTypInp+str(year_used)+".map",
                                                    self.cloneMap, self.tmpDir, self.inputDir, False, None, True)
        # excluding wetlands (waterBodyTyp = 0) in all functions related to lakes/reservoirs
        self.waterBodyTyp = pcr.ifthen(pcr.scalar(self.waterBodyTyp) > 0, pcr.nominal(self.waterBodyTyp))
        # choose only one type: either lake or reservoir
        self.waterBodyTyp = pcr.areamajority(self.waterBodyTyp, self.waterBodyIds)
        self.waterBodyTyp = pcr.ifthen(pcr.scalar(self.waterBodyTyp) > 0, pcr.nominal(self.waterBodyTyp))
        self.waterBodyTyp = pcr.ifthen(pcr.boolean(self.waterBodyIds), self.waterBodyTyp)
        # correcting lakes and reservoirs ids and outlets
        self.waterBodyIds = pcr.ifthen(pcr.scalar(self.waterBodyTyp) > 0, self.waterBodyIds)
        self.waterBodyOut = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0, self.waterBodyOut)

        # water body shape factor
        if self.useNetCDF:
            self.waterBodyShapeFactor = vos.netcdf2PCRobjClone(self.ncFileInp, 'waterBodyShF',
                                                               date_used, useDoy='yearly',
                                                               cloneMapFileName=self.cloneMap)
        else:
            self.waterBodyShapeFactor = vos.readPCRmapClone(self.waterBodyShF+str(year_used)+".map",
                                                            self.cloneMap, self.tmpDir, self.inputDir,
                                                            False, None, True)

        # reservoir maximum capacity (m3)
        if self.useNetCDF:
            self.resMaxCap = 1000. * 1000. * vos.netcdf2PCRobjClone(self.ncFileInp, 'resMaxCapInp',
                                                                    date_used, useDoy='yearly',
                                                                    cloneMapFileName=self.cloneMap)
        else:
            self.resMaxCap = 1000. * 1000. * vos.readPCRmapClone(self.resMaxCapInp+str(year_used)+".map",
                                                                 self.cloneMap, self.tmpDir, self.inputDir)
        self.resMaxCap = pcr.ifthen(self.resMaxCap > 0, self.resMaxCap)
        self.resMaxCap = pcr.areaaverage(self.resMaxCap, self.waterBodyIds)

        # water body capacity (m3): (lakes and reservoirs)
        self.waterBodyCap = pcr.cover(self.resMaxCap, 0.0)  # Note: Most of lakes have capacities > 0.
        self.waterBodyCap = pcr.ifthen(pcr.boolean(self.waterBodyIds), self.waterBodyCap)

        # correcting water body types: Reservoirs that have zero capacities will be assumed as lakes.
        self.waterBodyTyp = pcr.ifthen(pcr.scalar(self.waterBodyTyp) > 0., self.waterBodyTyp)
        self.waterBodyTyp = pcr.ifthenelse(
            self.waterBodyCap > 0., self.waterBodyTyp, pcr.ifthenelse(pcr.scalar(self.waterBodyTyp) == 2,
                                                                      pcr.nominal(1), self.waterBodyTyp))
        # final corrections:
        # make sure that all lakes and/or reservoirs have surface areas
        self.waterBodyTyp = pcr.ifthen(self.waterBodyArea > 0., self.waterBodyTyp)
        # make sure that only types 1 and 2 will be considered in lake/reservoir functions
        self.waterBodyTyp = pcr.ifthen(pcr.scalar(self.waterBodyTyp) > 0., self.waterBodyTyp)
        # make sure that all lakes and/or reservoirs have ids
        self.waterBodyIds = pcr.ifthen(pcr.scalar(self.waterBodyTyp) > 0., self.waterBodyIds)
        # make sure that all lakes and/or reservoirs have outlets
        self.waterBodyOut = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0., self.waterBodyOut)

        # for a natural run (self.onlyNaturalWaterBodies == True) 
        # which uses only the year 1900, assume all reservoirs are lakes
        if self.onlyNaturalWaterBodies == True and date_used == self.dateForNaturalCondition:
            logger.info("WARNING!! Using only natural water bodies identified in the year 1900. All reservoirs in 1900 are assumed as lakes.")
            self.waterBodyTyp = pcr.ifthen(pcr.scalar(self.waterBodyTyp) > 0., pcr.nominal(1))

        # check that all lakes and/or reservoirs have types, ids, surface areas and outlets:
        test = pcr.defined(self.waterBodyTyp) & \
               pcr.defined(self.waterBodyArea) & \
               pcr.defined(self.waterBodyIds) & \
               pcr.boolean(pcr.areamaximum(pcr.scalar(self.waterBodyOut), self.waterBodyIds))
        a, b, c = vos.getMinMaxMean(pcr.scalar(test) - pcr.scalar(1.0), ignoreEmptyMap=True)
        threshold = 1e-3
        if abs(a) > threshold or abs(b) > threshold:
            logger.info("WARNING !!!!! Missing information in some lakes and/or reservoirs.")

        # at the beginning of simulation period (timeStepPCR = 1)
        # - we have to define/get the initial conditions
        if currTimeStep.timeStepPCR == 1:
            self.getICs(initial_condition_dictionary)

        # For each new reservoir (introduced at the beginning of the year)
        # initiating storage, average inflow and outflow
        self.waterBodyStorage = pcr.cover(self.waterBodyStorage, 0.0)
        self.avgInflow = pcr.cover(self.avgInflow, 0.0)
        self.avgOutflow = pcr.cover(self.avgOutflow, 0.0)

        # cropping only in the landmask region:
        self.fracWat = pcr.ifthen(self.landmask, self.fracWat)
        self.waterBodyIds = pcr.ifthen(self.landmask, self.waterBodyIds)
        self.waterBodyOut = pcr.ifthen(self.landmask, self.waterBodyOut)
        self.waterBodyArea = pcr.ifthen(self.landmask, self.waterBodyArea)
        self.waterBodyTyp = pcr.ifthen(self.landmask, self.waterBodyTyp)
        self.waterBodyCap = pcr.ifthen(self.landmask, self.waterBodyCap)
        self.waterBodyStorage = pcr.ifthen(self.landmask, self.waterBodyStorage)
        self.avgInflow = pcr.ifthen(self.landmask, self.avgInflow)
        self.avgOutflow = pcr.ifthen(self.landmask, self.avgOutflow)

    def getICs(self, initial_condition):

        avgInflow = initial_condition['avgLakeReservoirInflowShort']
        avgOutflow = initial_condition['avgLakeReservoirOutflowLong']
        #
        if isinstance(initial_condition['waterBodyStorage'], pcraster.Field):
            # read directly 
            waterBodyStorage = initial_condition['waterBodyStorage']
        else:
            # calculate waterBodyStorage at cells where lakes and/or reservoirs are defined
            #
            storageAtLakeAndReservoirs = pcr.cover(
                pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0., initial_condition['channelStorage']), 0.0)
            #
            # - move only non negative values and use round down values
            storageAtLakeAndReservoirs = pcr.max(0.00, pcr.rounddown(storageAtLakeAndReservoirs))
            #
            # lake and reservoir storages = waterBodyStorage (m3);
            # values are given for the entire lake / reservoir cells
            waterBodyStorage = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0.,
                                          pcr.areatotal(storageAtLakeAndReservoirs, self.waterBodyIds))

        self.avgInflow = pcr.cover(avgInflow, 0.0)                # unit: m3/s
        self.avgOutflow = pcr.cover(avgOutflow, 0.0)              # unit: m3/s
        self.waterBodyStorage = pcr.cover(waterBodyStorage, 0.0)  # unit: m3

        self.avgInflow = pcr.ifthen(self.landmask, self.avgInflow)
        self.avgOutflow = pcr.ifthen(self.landmask, self.avgOutflow)
        self.waterBodyStorage = pcr.ifthen(self.landmask, self.waterBodyStorage)
        self.getWaterBodyDimensions()

    def update(self, newStorageAtLakeAndReservoirs,
               timestepsToAvgDischarge,
               maxTimestepsToAvgDischargeShort,
               maxTimestepsToAvgDischargeLong,
               currTimeStep,
               avgChannelDischarge,
               tau,
               phi,
               length_of_time_step=vos.secondsPerDay(),
               downstreamDemand=None):

        #if self.debugWaterBalance:
        preStorage = self.waterBodyStorage    # unit: m

        self.timestepsToAvgDischarge = timestepsToAvgDischarge   # TODO: include this one in "currTimeStep"

        # obtain inflow (and update storage)
        self.moveFromChannelToWaterBody(newStorageAtLakeAndReservoirs,
                                        timestepsToAvgDischarge,
                                        maxTimestepsToAvgDischargeShort,
                                        length_of_time_step)

        # calculate outflow (and update storage)
        self.getWaterBodyOutflow(maxTimestepsToAvgDischargeLong,
                                 avgChannelDischarge,
                                 tau, phi,
                                 length_of_time_step,
                                 downstreamDemand)

        self.getWaterBodyDimensions()

        if self.debugWaterBalance:
            vos.waterBalanceCheck([self.inflow/self.waterBodyArea],
                                  [self.waterBodyOutflow/self.waterBodyArea],
                                  [preStorage/self.waterBodyArea],
                                  [self.waterBodyStorage/self.waterBodyArea],
                                  'WaterBodyStorage',
                                  True,
                                  currTimeStep.fulldate, threshold=1e-3)

    def moveFromChannelToWaterBody(self,
                                   newStorageAtLakeAndReservoirs,
                                   timestepsToAvgDischarge,
                                   maxTimestepsToAvgDischargeShort,
                                   length_of_time_step=vos.secondsPerDay()):

        # new lake and/or reservoir storages (m3)
        newStorageAtLakeAndReservoirs = pcr.cover(
            pcr.areatotal(newStorageAtLakeAndReservoirs, self.waterBodyIds), 0.0)

        # incoming volume (m3)
        self.inflow = newStorageAtLakeAndReservoirs - self.waterBodyStorage

        # inflowInM3PerSec (m3/s)
        inflowInM3PerSec = self.inflow / length_of_time_step

        # updating (short term) average inflow (m3/s); needed to constrain lake outflow;
        # for reference see the "weighted incremental algorithm" in
        # http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
        temp = pcr.max(1.0, pcr.min(maxTimestepsToAvgDischargeShort,
                                    self.timestepsToAvgDischarge - 1.0 + length_of_time_step / vos.secondsPerDay()))
        deltaInflow = inflowInM3PerSec - self.avgInflow
        R = deltaInflow * (length_of_time_step / vos.secondsPerDay()) / temp
        self.avgInflow = self.avgInflow + R
        self.avgInflow = pcr.max(0.0, self.avgInflow)

        # updating waterBodyStorage (m3)
        self.waterBodyStorage = newStorageAtLakeAndReservoirs

    def getWaterBodyOutflow(self,
                            maxTimestepsToAvgDischargeLong,
                            avgChannelDischarge,
                            tau, phi,
                            length_of_time_step=vos.secondsPerDay(),
                            downstreamDemand=None):

        # outflow in volume from water bodies with lake type (m3): 
        lakeOutflow = self.getLakeOutflow(avgChannelDischarge, tau, phi, length_of_time_step)

        # outflow in volume from water bodies with reservoir type (m3): 
        # if isinstance(downstreamDemand, types.NoneType): downstreamDemand = pcr.scalar(0.0)
        if downstreamDemand is None:
            downstreamDemand = pcr.scalar(0.0)
        reservoirOutflow = self.getReservoirOutflow(avgChannelDischarge, length_of_time_step, downstreamDemand)

        # outgoing/release volume from lakes and/or reservoirs
        self.waterBodyOutflow = pcr.cover(reservoirOutflow, lakeOutflow)

        # make sure that all water bodies have outflow:
        self.waterBodyOutflow = pcr.max(0.,
                                        pcr.cover(self.waterBodyOutflow, 0.0))
        # use round values
        self.waterBodyOutflow = pcr.rounddown(self.waterBodyOutflow/1.)*1.  # unit: m3

        # outflow rate in m3 per sec
        waterBodyOutflowInM3PerSec = self.waterBodyOutflow / length_of_time_step  # unit: m3/s

        # updating (long term) average outflow (m3/s); needed to constrain/maintain reservoir outflow;
        # for the reference, see the "weighted incremental algorithm" in
        # http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
        temp = pcr.max(1.0, pcr.min(maxTimestepsToAvgDischargeLong,
                                    self.timestepsToAvgDischarge - 1.0 + length_of_time_step / vos.secondsPerDay()))
        deltaOutflow = waterBodyOutflowInM3PerSec - self.avgOutflow
        R = deltaOutflow * (length_of_time_step / vos.secondsPerDay()) / temp
        self.avgOutflow = self.avgOutflow + R
        self.avgOutflow = pcr.max(0.0, self.avgOutflow)

        # update waterBodyStorage (after outflow):
        self.waterBodyStorage = self.waterBodyStorage - self.waterBodyOutflow
        self.waterBodyStorage = pcr.max(0.0, self.waterBodyStorage)

    def weirFormula(self, waterHeight, weirWidth):  # output: m3/s
        sillElev = pcr.scalar(0.0)
        weirFormula = (1.7 * self.weirCoeff * pcr.max(0, waterHeight-sillElev)**1.5) * weirWidth  # m3/s
        return weirFormula

    def getLakeOutflow(self, avgChannelDischarge, tau, phi, length_of_time_step=vos.secondsPerDay()):

        # Estimate lake outflow based on the volume of live storage, where live storage is lake volume
        # located above the sill elevation (sill elevation is taken as the bottom of the outflow channel).
        # It is taken that the maximum water body capacity represents the storage volume at the sill elevation.
        # Therefore, live storage must be positive for outflow to occur.
        # Ensure that the following relationship holds: 0.0 <= lakeOutflow <= liveStorage

        # Estimate live storage (current storage minus maximum water body capacity)
        liveStorage = pcr.max(self.waterBodyStorage - pcr.cover(self.waterBodyCap, 0.0), 0.0)
        # waterHeight (m): water height above sill; a function of live storage
        waterHeight = pcr.cover(liveStorage/self.waterBodyArea)

        avgOutflow = self.avgOutflow
        # This is needed when new lakes/reservoirs introduced (its avgOutflow is still zero)
        avgOutflow = pcr.ifthenelse(avgOutflow > 0., avgOutflow, pcr.max(avgChannelDischarge, self.avgInflow, 0.001))
        avgOutflow = pcr.areamaximum(avgOutflow, self.waterBodyIds)

        # weirWidth (m) - estimated from avgOutflow (m3/s) using bankfull geometry
        weirWidthUsed = pcr.cover(tau * pow(avgOutflow, phi), 0.)
        weirWidthUsed = pcr.max(weirWidthUsed, self.minWeirWidth)
        weirWidthUsed = pcr.cover(pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0., weirWidthUsed), 0.0)

        # estimate volume of water released by lakes
        lakeOutflowInM3PerSec = self.weirFormula(waterHeight, weirWidthUsed)  # unit: m3/s
        lakeOutflow = lakeOutflowInM3PerSec * length_of_time_step  # unit: m3
        lakeOutflow = pcr.min(liveStorage, lakeOutflow)  # lake outflow can't exceed live storage
        #
        lakeOutflow = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0., lakeOutflow)
        lakeOutflow = pcr.ifthen(pcr.scalar(self.waterBodyTyp) == 1, lakeOutflow)

        # TODO: Consider endorheic lake/basin. No outflow for endorheic lake/basin!

        return lakeOutflow

    def getReservoirOutflow(self, avgChannelDischarge, length_of_time_step, downstreamDemand):

        # avgOutflow (m3/s)
        avgOutflow = self.avgOutflow
        # This is needed when new lakes/reservoirs introduced (its avgOutflow is still zero).
        avgOutflow = pcr.ifthenelse(avgOutflow > 0., avgOutflow,
                                    pcr.max(avgChannelDischarge, self.avgInflow, 0.001))
        avgOutflow = pcr.areamaximum(avgOutflow, self.waterBodyIds)

        # calculate resvOutflow (m2/s) (based on reservoir storage and avgDischarge): 
        # - using reductionFactor in such a way that:
        #   - if relativeCapacity < minResvrFrac : release is terminated
        #   - if relativeCapacity > maxResvrFrac : longterm average
        reductionFactor = pcr.cover(
            pcr.min(1.,
                    pcr.max(0., self.waterBodyStorage - self.minResvrFrac*self.waterBodyCap) /
                    (self.maxResvrFrac - self.minResvrFrac)*self.waterBodyCap), 0.0)
        #
        resvOutflow = reductionFactor * avgOutflow * length_of_time_step  # unit: m3

        # maximum release <= average inflow (especially during dry condition)
        resvOutflow = pcr.max(0, pcr.min(resvOutflow, self.avgInflow * length_of_time_step)) # unit: m3

        # downstream demand (m3/s)
        # reduce demand if storage < lower limit
        reductionFactor = vos.getValDivZero(downstreamDemand, self.minResvrFrac*self.waterBodyCap, vos.smallNumber)
        reductionFactor = pcr.cover(reductionFactor, 0.0)
        downstreamDemand = pcr.min(downstreamDemand, downstreamDemand*reductionFactor)
        # resvOutflow > downstreamDemand
        resvOutflow = pcr.max(resvOutflow, downstreamDemand * length_of_time_step)  # unit: m3

        # floodOutflow: additional release if storage > upper limit
        ratioQBankfull = 2.3
        estmStorage = pcr.max(0., self.waterBodyStorage - resvOutflow)
        floodOutflow = pcr.max(0.0, estmStorage - self.waterBodyCap) +\
                       pcr.cover(pcr.max(0.0, estmStorage - self.maxResvrFrac*self.waterBodyCap)/
                                 ((1.-self.maxResvrFrac)*self.waterBodyCap), 0.0) * \
                       pcr.max(0.0,ratioQBankfull*avgOutflow* vos.secondsPerDay()-resvOutflow)
        # maximum limit of floodOutflow: bring the reservoir storages only to 3/4 of upper limit capacities
        floodOutflow = pcr.max(0.0, pcr.min(floodOutflow,estmStorage - self.maxResvrFrac*self.waterBodyCap*0.75))

        # update resvOutflow after floodOutflow
        resvOutflow  = pcr.cover(resvOutflow , 0.0) + pcr.cover(floodOutflow, 0.0)

        # maximum release if storage > upper limit : bring the reservoir storages only to 3/4 of upper limit capacities
        resvOutflow = pcr.ifthenelse(self.waterBodyStorage > self.maxResvrFrac*self.waterBodyCap,
                                     pcr.min(resvOutflow,
                                             pcr.max(0, self.waterBodyStorage -
                                                     self.maxResvrFrac*self.waterBodyCap*0.75)), resvOutflow)

        # if storage > upper limit : resvOutflow > avgInflow
        resvOutflow = pcr.ifthenelse(self.waterBodyStorage > self.maxResvrFrac*self.waterBodyCap,
                                     pcr.max(0.0, resvOutflow, self.avgInflow), resvOutflow)

        # resvOutflow < waterBodyStorage
        resvOutflow = pcr.min(self.waterBodyStorage, resvOutflow)

        resvOutflow = pcr.ifthen(pcr.scalar(self.waterBodyIds) > 0., resvOutflow)
        resvOutflow = pcr.ifthen(pcr.scalar(self.waterBodyTyp) == 2, resvOutflow)
        return resvOutflow  # unit: m3

    def getWaterBodyDimensions(self):

        # Lake properties max depth and total lake area
        lakeMaxDepth = ((3.0 * self.waterBodyStorage)/(self.waterBodyShapeFactor ** 2))**(1./3.)
        lakeArea = (lakeMaxDepth * self.waterBodyShapeFactor) ** 2

        # reservoir properties max depth at outlet and total reservoir area
        reservoirMaxDepth = ((6.0 * self.waterBodyStorage)/(self.waterBodyShapeFactor ** 2))**(1./3.)
        reservoirArea = 0.5 * (reservoirMaxDepth * self.waterBodyShapeFactor) ** 2

        # dynamic waterbody area, cannot exceed static waterbody extent as defined by input
        self.dynamicArea = pcr.cover(pcr.ifthenelse(pcr.scalar(self.waterBodyTyp) == 1, lakeArea,
                                                    pcr.ifthen(pcr.scalar(self.waterBodyTyp) == 2, reservoirArea)), 0.)

        self.dynamicArea = pcr.min(self.dynamicArea, self.waterBodyArea)

        # dynamic water fraction in grid cell
        self.dynamicFracWat = self.dynamicArea * self.waterBodyRelativeFrac / self.cellArea
        self.dynamicFracWat = pcr.cover(pcr.min(pcr.max(self.dynamicFracWat, 0.), self.fracWat), 0.)
        self.dynamicFracWat = ifthen(self.landmask, self.dynamicFracWat)

        self.maxWaterDepth = pcr.cover(pcr.ifthenelse(pcr.scalar(self.waterBodyTyp) == 1, lakeMaxDepth,
                                                      pcr.ifthen(pcr.scalar(self.waterBodyTyp) == 2,
                                                                 reservoirMaxDepth)))

    def getThermoClineDepth(self):
        self.mixingDepth = pcr.min(pcr.max(self.dynamicArea**0.1, pcr.scalar(1.0)), self.maxWaterDepth)
        self.mixingDepth = pcr.min(pcr.scalar(3), self.maxWaterDepth)

    def getThermoClineStorage(self):
        self.hypolimnionStorage = pcr.min(
            pcr.ifthenelse(
                pcr.scalar(self.waterBodyTyp) == 1,
                (((self.maxWaterDepth - self.mixingDepth)**3.) * (self.waterBodyShapeFactor ** 2))/3.0,
                ifthen(pcr.scalar(self.waterBodyTyp) == 2,
                       (((self.maxWaterDepth - self.mixingDepth)**3.) * (self.waterBodyShapeFactor ** 2))/6.0)),
            self.waterBodyStorage)
