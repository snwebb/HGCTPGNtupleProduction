import sys
sys.path.append('.')
from CRABClient.UserUtilities import config
import local

config = config()

config.section_("General")
config.General.requestName = 'NuGun_PU200_MTDAutomn18_tc_rates'
config.General.workArea = 'jobs'

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'produce_ntuple_tc_rates_cfg.py'
config.JobType.maxMemoryMB = 2000

config.section_("Data")
config.Data.inputDataset = '/NeutrinoGun_E_10GeV/PhaseIIMTDTDRAutumn18DR-PU200_103X_upgrade2023_realistic_v2-v1/FEVT'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = local.outLFNDirBase
config.Data.publication = False
config.Data.outputDatasetTag = config.General.requestName

config.section_("Site")
config.Site.storageSite = local.storageSite
