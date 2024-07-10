import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

array =[[0.4620458432198492, 0.14250122195500903, 0.15782151848528975, 0.237631416339852], [0.02549083896875498, 0.7275707919944575, 0.19916998635876879, 0.04776838267801884], [0.04612890681452937, 0.24368878794084198, 0.5620581239119545, 0.14812418133267424], [0.10961295569214215, 0.16850990445518238, 0.2858386816236504, 0.4360384582290252]]# array_new = array.split()

# array_float = [float(x) for x in array_new]
# print(array_float)

plt.figure(figsize=(10, 10))
df_cm = pd.DataFrame(array, range(4), range(4))
# df_cm = pd.DataFrame(array, columns= ["4B2Tau","2B2Tau","4B","TTToSemi","TTToHad","TTTo2L2Nu","WJetsToLNu_0J","WJetsToLNu_1J","WJetsToLNu_2J","ZJetsToQQ","WJetsToQQ","DYJetsToLL","ZZTo4Q","WWTo4Q"  ,"QCD","6B" ],index = ['HHH6b' ,'QCD','TT' ,'VJets','VV'])
# df_cm = pd.DataFrame(array, index= ["HHHTo4B2Tau","HHTo2B2Tau","HHTo4B","TTToSemiLeptonic","TTToHadronic","TTTo2L2Nu","WJetsToLNu_0J","WJetsToLNu_1J","WJetsToLNu_2J","ZJetsToQQ","WJetsToQQ","DYJetsToLL","ZZTo4Q","WWTo4Q"  ,"QCD","HHHTo6B" ],columns = ['ProbHHH6b' ,'ProbHH4b','Probrest'])
df_cm = pd.DataFrame(array, index= ["0Higgs","3Higgs","2Higgs","1Higgs"],columns = ['Prob0Higgs' ,'Prob3Higgs','Prob2Higgs','Prob1Higgs'])


# sn.set(font_scale=0.4) # for label size
sn.heatmap(df_cm,cmap='Blues',xticklabels='auto',yticklabels='auto',square=True,annot= True) # font size

plt.savefig('condused_matrix_Higgs.png')
plt.savefig('condused_matrix_Higgs.pdf')
# plt.show()


