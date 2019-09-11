import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(4) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/afs/cern.ch/user/m/melu/work/GEN_validation/CMSSW_9_4_9/src/temp/nomadspin_NLO.root'
    )
)

process.demo = cms.EDAnalyzer('Demo',
		# lhe =  cms.InputTag("externalLHEProducer"),
		# lhe1 =  cms.VInputTag(cms.InputTag("externalLHEProducer"), cms.InputTag("source")),
)


process.p = cms.Path(process.demo)
