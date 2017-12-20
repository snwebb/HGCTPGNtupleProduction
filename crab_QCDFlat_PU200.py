import sys
sys.path.append('.')
from WMCore.Configuration import Configuration
import local

config = Configuration()

config.section_("General")
config.General.requestName = 'QCDFlat_PU200'
config.General.workArea = 'jobs'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'produce_ntuple_full_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/QCD_Flat_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIITDRFall17DR-PU200_93X_upgrade2023_realistic_v2-v1/GEN-SIM-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 5
#  config.Data.totalUnits = 100
config.Data.outLFNDirBase = local.outLFNDirBase
config.Data.publication = False
config.Data.outputDatasetTag = 'QCDFlat_PU200'

config.section_("Site")
config.Site.storageSite = local.storageSite
