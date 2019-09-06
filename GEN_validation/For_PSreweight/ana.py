import ROOT
import sys
from DataFormats.FWLite import Events, Handle

from math import hypot, pi

events = Events (['./SMP-RunIIFall18wmLHEGS-00138.root'])


geninfo,geninfoLabel = Handle("GenEventInfoProduct"), "generator"
handlePruned  = Handle ("std::vector<reco::GenParticle>")
labelPruned = ("genParticles")

# loop over events
count= 0
countweighted = 0

for event in events:

    count = count+1
    if count % 100 == 0:
        print "count = " + str(count)

    count +=1

    event.getByLabel(labelPruned, handlePruned)

    pruned = handlePruned.product()

    event.getByLabel(geninfoLabel,geninfo)

    gen = geninfo.product()
    for i in range(0,gen.weights().size()):
        print gen.weights()[i]

    if gen.weight() > 0:
        countweighted += 1
    else:
        countweighted -= 1

#    for p in pruned :
#        if abs(p.pdgId()) == 11 and p.pt() > 25 and abs(p.eta()) < 2.5 and (p.statusFlags().isPrompt()) and p.status() == 1  :
#	    print p.pt()

