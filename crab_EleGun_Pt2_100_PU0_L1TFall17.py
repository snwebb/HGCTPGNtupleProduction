import sys
sys.path.append('.')
from CRABClient.UserUtilities import config
import local

config = config()

config.section_("General")
config.General.requestName = 'EleGun_Pt2_100_PU0_L1TFall17'
config.General.workArea = 'jobs'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'produce_ntuple_multialgos_reduced_genmatch_v8_cfg.py'
#config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
config.Data.inputDataset = '/SingleE_FlatPt-2to100/PhaseIIFall17D-L1TnoPU_93X_upgrade2023_realistic_v5-v1/GEN-SIM-DIGI-RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 3
config.Data.outLFNDirBase = local.outLFNDirBase
config.Data.publication = False
config.Data.outputDatasetTag = config.General.requestName

config.section_("Site")
config.Site.storageSite = local.storageSite
