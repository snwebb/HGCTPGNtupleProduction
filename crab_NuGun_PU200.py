import sys
sys.path.append('.')
from WMCore.Configuration import Configuration
import local

config = Configuration()

config.section_("General")
config.General.requestName = 'NuGun_PU200'
config.General.workArea = 'jobs'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'produce_ntuple_reduced_cfg.py'
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/DoubleNuE1Eta14_31/PhaseIITDRSpring17DR-PU200_NoSmear_91X_upgrade2023_realistic_v3-v2/GEN-SIM-RECO'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 4
#  config.Data.totalUnits = 1973
config.Data.outLFNDirBase = local.outLFNDirBase
config.Data.publication = False
config.Data.outputDatasetTag = 'NuGun_PU200'

config.section_("Site")
config.Site.storageSite = local.storageSite
