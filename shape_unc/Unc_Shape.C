#include <iostream>
#include <TStyle.h>
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TF1.h"
#include "TROOT.h"
#include "TProfile.h"
#include "TProfile2D.h"
#include "TFile.h"
#include "TLine.h"
#include "TMath.h"
#include "TLatex.h"
#include "TAttText.h"
#include <TLegend.h>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
#include "TChain.h"
#include "TTree.h"
#include "TCut.h"
#include "TLorentzVector.h"
#include "TCanvas.h"


void Unc_Shape(){

  gROOT->ProcessLine(".x ./lhcbStyle.C");
    
  // -------------------------------------------------------------- //
  // calculate corrected eff: 1D
  // -------------------------------------------------------------- //
  
  TFile* file_1Higgs    = new TFile("ProbMultiH_1Higgs.root");
  TFile* file_2Higgs    = new TFile("ProbMultiH_2Higgs.root");

  // ==== Readin original distributions
  TH1D* Hist_Data_1Higgs = (TH1D*)(file_1Higgs->Get("data_obs"));;
  TH1D* Hist_Data_2Higgs = (TH1D*)(file_2Higgs->Get("data_obs"));;

  TH1D* Hist_BKG_1Higgs = (TH1D*)(file_1Higgs->Get("QCD_datadriven_data"));;
  TH1D* Hist_BKG_2Higgs = (TH1D*)(file_2Higgs->Get("QCD_datadriven_data"));;

  Hist_Data_1Higgs->Sumw2();
  Hist_Data_2Higgs->Sumw2();
  Hist_BKG_1Higgs->Sumw2();
  Hist_BKG_2Higgs->Sumw2();

  Hist_Data_1Higgs->Scale(1./Hist_Data_1Higgs->Integral());
  Hist_Data_2Higgs->Scale(1./Hist_Data_2Higgs->Integral());
  Hist_BKG_1Higgs->Scale(1./Hist_BKG_1Higgs->Integral());
  Hist_BKG_2Higgs->Scale(1./Hist_BKG_2Higgs->Integral());
  
  
  // ==== Correction, Sigma_M (no correction), Sigma_P ( MC_2Higgs \times ratio^2 ) 
  TFile* file_save = new TFile("Corr_Shape.root", "recreate");
  TH1D* Hist_Corr_2Higgs = (TH1D*)Hist_Data_2Higgs->Clone();
  TH1D* Hist_Sigma_M_2Higgs = (TH1D*)Hist_Data_2Higgs->Clone();
  TH1D* Hist_Sigma_P_2Higgs = (TH1D*)Hist_Data_2Higgs->Clone();
  
  //==== Fill hist
  for(int i = 1; i < Hist_Data_1Higgs->GetNbinsX()+1; i++){
    // read value and error
    double  data_1Higgs =  Hist_Data_1Higgs->GetBinContent(i);
    double  data_2Higgs =  Hist_Data_2Higgs->GetBinContent(i);
    double  qcd_1Higgs  =  Hist_BKG_1Higgs->GetBinContent(i);
    double  qcd_2Higgs  =  Hist_BKG_2Higgs->GetBinContent(i);

    double  e_data_1Higgs =  Hist_Data_1Higgs->GetBinError(i);
    double  e_data_2Higgs =  Hist_Data_2Higgs->GetBinError(i);
    double  e_qcd_1Higgs  =  Hist_BKG_1Higgs->GetBinError(i);
    double  e_qcd_2Higgs  =  Hist_BKG_2Higgs->GetBinError(i);

    // Correction : Hist_BKG_2Higgs * (Hist_Data_1Higgs / Hist_BKG_1Higgs)
    double Corr_2Higgs;
    double Corr_err_2Higgs;
    Corr_2Higgs     = qcd_2Higgs * (data_1Higgs / qcd_1Higgs);
    Corr_err_2Higgs = Corr_2Higgs * sqrt( 
                            pow(e_qcd_1Higgs / qcd_1Higgs, 2) +
                            pow(e_qcd_2Higgs / qcd_2Higgs, 2) +
                            pow(e_data_1Higgs / data_1Higgs, 2)
                          );
    Hist_Corr_2Higgs->SetBinContent(i, Corr_2Higgs);
    Hist_Corr_2Higgs->SetBinError(i, Corr_err_2Higgs);

    // Sigma_M : abs(Hist_Data_2Higgs - Hist_BKG_2Higgs) 
    double sigma_M = -1. * abs(data_2Higgs - qcd_2Higgs);
    double sigma_M_err = 0.;
    Hist_Sigma_M_2Higgs->SetBinContent(i, sigma_M);
    Hist_Sigma_M_2Higgs->SetBinError(i, sigma_M_err);
    
    // Sigma_P : Hist_BKG_2Higgs * ((Hist_Data_1Higgs / Hist_BKG_1Higgs))^2 
    double sigma_P = 1. * Corr_2Higgs * (data_1Higgs / qcd_1Higgs);
    double sigma_P_err = 0.;
    Hist_Sigma_P_2Higgs->SetBinContent(i, sigma_P);
    Hist_Sigma_P_2Higgs->SetBinError(i, sigma_P_err);

    // debug
    cout << i << "\t"<< Hist_Data_2Higgs->GetBinContent(i) << endl;
  }


  //==== Draw and save    
  string ytitle   = "Arbitray scale";
  string xtitle   = "ProbMultiH";
  double y_min = 0.0;
  double y_max = 0.35;
  double y_M_min = -0.05;
  double y_M_max = 0.25;

  TCanvas* cc = new TCanvas("cc", "cc", 1000, 800);
  cc->Divide(1,2,0,0,0) ;


  cc->cd(1);
  gPad->SetTopMargin(0.1);
  gPad->SetBottomMargin(0.1);
  gPad->SetLeftMargin(0.12);
  gPad->SetRightMargin(0.07);
  gPad->SetPad(0.0,0.25,0.98,0.98);
  gPad->SetGrid();
  Hist_Data_2Higgs->SetLineColor(1);
  Hist_Data_2Higgs->SetLineWidth(2);
  Hist_Data_2Higgs->SetMarkerColor(1);
  Hist_Data_2Higgs->SetMarkerStyle(23);
  Hist_Data_2Higgs->SetXTitle(xtitle.c_str());
  Hist_Data_2Higgs->GetXaxis()->SetLabelSize(0.04);    
  Hist_Data_2Higgs->GetXaxis()->SetTitleOffset(0.9);
  Hist_Data_2Higgs->SetYTitle(ytitle.c_str());
  Hist_Data_2Higgs->SetAxisRange(y_min, y_max, "Y");
  Hist_Data_2Higgs->GetYaxis()->SetLabelSize(0.04);

  Hist_BKG_2Higgs->SetLineColor(2);
  Hist_BKG_2Higgs->SetLineWidth(2);
  Hist_BKG_2Higgs->SetMarkerColor(2);
  Hist_BKG_2Higgs->SetMarkerStyle(23);

  Hist_Corr_2Higgs->SetLineColor(4);
  Hist_Corr_2Higgs->SetLineWidth(2);
  Hist_Corr_2Higgs->SetMarkerColor(4);
  Hist_Corr_2Higgs->SetMarkerStyle(23);

  TLegend* leg = new TLegend(0.65, 0.67, 0.92, 0.87);
  leg->AddEntry(Hist_Data_2Higgs , "Data - 2 Higgs", "epl");
  leg->AddEntry(Hist_BKG_2Higgs , "BKG - 2 Higgs", "epl");    
  leg->AddEntry(Hist_Corr_2Higgs , "BKG_Corrected - 2 Higgs", "epl");    
  Hist_Data_2Higgs ->Draw();
  Hist_BKG_2Higgs->Draw("same");    
  Hist_Corr_2Higgs->Draw("same");    
  leg->Draw("same");

  TPaveText* ptext = new TPaveText(0.13, 0.58, 0.64, 0.86,"NDC");
  ptext->SetTextFont(132);
  ptext->AddText("#color[1]{Ratio (1 Higgs) = Data/BKG (1 Higgs) }");
  ptext->AddText("#color[4]{H_{Corr} (2 Higgs) = BKG (2 Higgs) #times Ratio (1 Higgs)}");
  ptext->AddText("#color[46]{Sigma_M (2 Higgs) = - | H_{Data} - H_{BKG} | (2 Higgs)}");
  ptext->AddText("#color[9]{Sigma_P (2 Higgs) = + H_{Corr} (2 Higgs) #times Ratio^{2} (1 Higgs)}");
  // ptext->SetShadowColor(kWhite);
  ptext->SetFillColor(kWhite);
  ptext->SetTextAlign(11);
  ptext->Draw("same");

  cc->cd(2);
  gPad->SetTopMargin(0.05);
  gPad->SetBottomMargin(0.3);
  gPad->SetLeftMargin(0.12);
  gPad->SetRightMargin(0.07);
  gPad->SetPad(0.0,0.06,0.98,0.25);
  
  Hist_Sigma_P_2Higgs->SetXTitle("#scale[3.5]{#color[46]{Minus} / #color[9]{Plus} 1 Sigma}");
  Hist_Sigma_P_2Higgs->GetXaxis()->SetTitleOffset(2.8);
  Hist_Sigma_P_2Higgs->SetLineColor(4);
  Hist_Sigma_P_2Higgs->SetFillColor(9);
  Hist_Sigma_P_2Higgs->SetLineWidth(2);
  Hist_Sigma_P_2Higgs->SetMarkerColor(4);
  Hist_Sigma_P_2Higgs->SetMarkerStyle(23);
  Hist_Sigma_P_2Higgs->SetAxisRange(y_M_min, y_M_max, "Y");
  Hist_Sigma_P_2Higgs->SetLabelSize(0.15,"X");
  Hist_Sigma_P_2Higgs->SetLabelSize(0.15,"Y");
  Hist_Sigma_M_2Higgs->SetLineColor(2);
  Hist_Sigma_M_2Higgs->SetFillColor(46);
  Hist_Sigma_M_2Higgs->SetLineWidth(2);
  Hist_Sigma_M_2Higgs->SetMarkerColor(2);
  Hist_Sigma_M_2Higgs->SetMarkerStyle(23);
  Hist_Sigma_P_2Higgs->Draw("hist");
  Hist_Sigma_M_2Higgs->Draw("hist && same");
  cc->SaveAs("Comp_2Higgs.pdf");

  file_save->Write();
  file_save->Close();

}

