using namespace std;

void draw_ptj(){

	double xs=236.;
	gSystem->Load("/home/Documents/MG5_aMC_v2_6_0/ExRootAnalysis/libExRootAnalysis.so");
	gSystem->Load("/usr/lib/root/libPhysics.so");
	// Create chain of root trees
	TChain chain("LHEF");


	TCanvas *c1= new TCanvas("c1","test graph 10k events",800,600);
	c1->SetLogy();

	TString IFile1 = "run01.root";
	chain.Add(IFile1);
// Create object of class ExRootTreeReader
	ExRootTreeReader *treeReader1 = new ExRootTreeReader(&chain);
	Long64_t numberOfEntries1 = treeReader1->GetEntries();
	cout<<numberOfEntries1<<"  run01"<<endl;
// Get pointers to branches used in this analysis
	TClonesArray *branchEvent1 = treeReader1->UseBranch("Event");
	TClonesArray *branchParticle1 = treeReader1->UseBranch("Particle");
	//  TClonesArray *branchJet = treeReader->UseBranch("Jet");
	TH1F *h1= new TH1F("1_ptj","test histogram",40,0,400);
	h1->SetStats(0);
	h1->GetXaxis()->SetTitle("jet_pT[GeV]");
	h1->GetYaxis()->SetTitle("a.u.");
	h1->Sumw2();
	TLorentzVector VJ1;
	int count1=0,countj1=0,num1=0;
	for(int i=0; i<=numberOfEntries1-1; i++)
	{
		double ptj1_temp=0;
		double ptj1=0;
		VJ1.SetPxPyPzE(0.,0.,0.,0.);
		treeReader1->ReadEntry(i);
		TRootLHEFEvent *event1=(TRootLHEFEvent*) branchEvent1->At(0);
		int np1=event1->Nparticles;
		double weight1=event1->Weight;
		for(int j=2;j<np1;j++){
			TRootLHEFParticle *particle1=(TRootLHEFParticle*) branchParticle1->At(j);
			if(abs(particle1->PID)<6 || abs(particle1->PID)==21 ) {
				countj1++;
				VJ1.SetPxPyPzE(particle1->Px,particle1->Py,particle1->Pz,particle1->E);
				ptj1_temp=VJ1.Pt();
			}
			if(ptj1_temp>ptj1) ptj1=ptj1_temp;
		}
			h1->Fill(ptj1,weight1);
			num1++;
	}
	cout<<"h1 integral "<<h1->Integral()<<endl;
	h1->Scale(xs/(h1->Integral()));
	cout<<"h1 "<<h1->Integral()<<endl;
	h1->SetLineColor(kRed);
	h1->Draw("h");
	cout<<"run01 jet number "<<countj1<<" fill jet number "<<num1<<endl;

	TString IFile2 = "run02.root";
	chain.Add(IFile2);
// Create object of class ExRootTreeReader
	ExRootTreeReader *treeReader2 = new ExRootTreeReader(&chain);
	Long64_t numberOfEntries2 = treeReader2->GetEntries();
	cout<<numberOfEntries2<<"  run02"<<endl;
// Get pointers to branches used in this analysis
	TClonesArray *branchEvent2 = treeReader2->UseBranch("Event");
	TClonesArray *branchParticle2 = treeReader2->UseBranch("Particle");
	//  TClonesArray *branchJet = treeReader->UseBranch("Jet");
	TH1F *h2= new TH1F("2_ptj","test histogram",40,0,400);
	h2->Sumw2();
	TLorentzVector VJ2;
	int count2=0,countj2=0,num2=0;
	for(int i=numberOfEntries1; i<=numberOfEntries2-1; i++)
	{		
		double ptj2=0,ptj2_temp=0;
		VJ2.SetPxPyPzE(0.,0.,0.,0.);
		treeReader2->ReadEntry(i);
		TRootLHEFEvent *event2=(TRootLHEFEvent*) branchEvent2->At(0);
		int np2=event2->Nparticles;
		double weight2=event2->Weight;
		for(int j=2;j<np2;j++){
			TRootLHEFParticle *particle2=(TRootLHEFParticle*) branchParticle2->At(j);
			if((abs(particle2->PID)<6 || abs(particle2->PID)==21) ) {
				countj2++;
                                VJ2.SetPxPyPzE(particle2->Px,particle2->Py,particle2->Pz,particle2->E);
                                ptj2_temp=VJ2.Pt();
			}
                       	if(ptj2_temp>ptj2) ptj2=ptj2_temp;
		}
			h2->Fill(ptj2,weight2);
			num2++;
	}
	h2->Scale(xs/(h2->Integral()));
	cout<<"OK"<<endl;
//	cout<<"h2 "<<h2->Integral()<<endl;
	h2->SetLineColor(kGreen);
	h2->Draw("h same");
	cout<<"run02 jet number "<<countj2<<" fill jet number "<<num2<<endl;

	TString IFile3 = "run03.root";
	chain.Add(IFile3);
// Create object of class ExRootTreeReader
	ExRootTreeReader *treeReader3 = new ExRootTreeReader(&chain);
	Long64_t numberOfEntries3 = treeReader3->GetEntries();
	cout<<numberOfEntries3<<"  run03"<<endl;
// Get pointers to branches used in this analysis
	TClonesArray *branchEvent3 = treeReader3->UseBranch("Event");
	TClonesArray *branchParticle3 = treeReader3->UseBranch("Particle");
	//  TClonesArray *branchJet = treeReader->UseBranch("Jet");
	TH1F *h3= new TH1F("3_ptj","test histogram",40,0,400);
	h3->Sumw2();
	TLorentzVector VJ3;
	int count3=0,countj3=0,num3=0;
	for(int i=numberOfEntries2; i<=numberOfEntries3-1; i++)
	{		
		double ptj3=0,ptj3_temp=0;
		VJ3.SetPxPyPzE(0.,0.,0.,0.);
		treeReader3->ReadEntry(i);
		TRootLHEFEvent *event3=(TRootLHEFEvent*) branchEvent3->At(0);
		int np3=event3->Nparticles;
		double weight3=event3->Weight;
		for(int j=2;j<np3;j++){
			TRootLHEFParticle *particle3=(TRootLHEFParticle*) branchParticle3->At(j);
			if((abs(particle3->PID)<6 || abs(particle3->PID)==21) ) {
				countj3++;
                                VJ3.SetPxPyPzE(particle3->Px,particle3->Py,particle3->Pz,particle3->E);
                                ptj3_temp=VJ3.Pt();
			}
                       	if(ptj3_temp>ptj3) ptj3=ptj3_temp;
		}
			h3->Fill(ptj3,weight3);
			num3++;
	}
	h3->Scale(xs/(h3->Integral()));
	cout<<"OK"<<endl;
//	cout<<"h2 "<<h2->Integral()<<endl;
	h3->SetLineColor(kBlack);
	h3->Draw("h same");
	cout<<"run03 jet number "<<countj3<<" fill jet number "<<num3<<endl;

	TLegend *l1 = new TLegend(0.7,0.75,0.9,0.9,NULL,"brNDC");
	l1->SetBorderSize(1);
	l1->SetFillColor(0);
	l1->AddEntry(h1,"without bias");
	l1->AddEntry(h3,"ptj**2 bias");
	l1->AddEntry(h2,"ptj**4 bias");
	l1->Draw();
    
	c1->Update();
	c1->SaveAs("ptj.png");

}

