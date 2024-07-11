## \file
## \ingroup tutorial_pyroot
## \notebook -js
## A Simple Graph with error bars
##
## \macro_image
## \macro_code
##
## \author Wim Lavrijsen
 
from ROOT import TCanvas, TGraphErrors,TGraphAsymmErrors
from ROOT import gROOT
from array import array
 
c1 = TCanvas( 'c1', 'A Simple Graph with error bars', 200, 10, 700, 500 )
 
c1.SetGrid()
c1.GetFrame().SetFillColor( 21 )
c1.GetFrame().SetBorderSize( 12 )
 
n = 10
x  = array( 'f', [ -0.22, 0.05, 0.25, 0.35,  0.5, 0.61,  0.7, 0.85, 0.89, 0.95 ] )
exl = array( 'f', [  0.05,  0.1, 0.07, 0.07, 0.04, 0.05, 0.06, 0.07, 0.08, 0.05 ] )
exh = array( 'f', [  0.01,  0.01, 0.7, 0.7, 0.4, 0.5, 0.6, 0.7, 0.8, 0.5 ] )
y  = array( 'f', [     1,  2.9,  5.6,  7.4,  9.0,  9.6,  8.7,  6.3,  4.5,    1 ] )
eyl = array( 'f', [  0.8,  0.7,  0.6,  0.5,  0.4,  0.4,  0.5,  0.6,  0.7,  0.8  ] )
eyh = array( 'f', [  0.8,  0.7,  0.6,  0.5,  0.4,  0.4,  0.5,  0.6,  0.7,  0.8  ] )
 
gr = TGraphAsymmErrors( n, x, y, exl, exh, eyl, eyh )
gr.SetTitle( 'TGraphErrors Example' )
gr.SetMarkerColor( 4 )
gr.SetMarkerStyle( 21 )
gr.Draw( 'ALP' )


c1.SaveAs("output.pdf")



# ###########GPT
# import ROOT
# import numpy as np

# # Create NumPy arrays for x, y, and asymmetric errors
# x_values = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
# y_values = np.array([2.0, 3.0, 5.0, 7.0, 11.0])
# x_err_low = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
# x_err_high = np.array([0.2, 0.3, 0.4, 0.5, 0.6])
# y_err_low = np.array([0.2, 0.3, 0.1, 0.4, 0.5])
# y_err_high = np.array([0.4, 0.1, 0.2, 0.3, 0.6])

# # Create a TGraphAsymmErrors
# graph = ROOT.TGraphAsymmErrors(len(x_values))

# # Fill TGraphAsymmErrors with data
# for i in range(len(x_values)):
#     graph.SetPoint(i, x_values[i], y_values[i])
#     graph.SetPointError(
#         i,
#         x_err_low[i],
#         x_err_high[i],
#         y_err_low[i],
#         y_err_high[i]
#     )

# # Print the content of the TGraphAsymmErrors
# graph.Print()

# # Draw the TGraphAsymmErrors
# canvas = ROOT.TCanvas("canvas", "TGraphAsymmErrors Example", 800, 600)
# graph.Draw("AP")
# canvas.Update()
# canvas.SaveAs("output.pdf")

# # Keep the program running to view the canvas
# ROOT.gApplication.Run()
