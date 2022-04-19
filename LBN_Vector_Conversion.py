import ROOT
import csv


with open('PtEtaPhiE.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

PtEtaPhiE = [[float(item) for item in line[1:]] for line in data[1:]]

print(len(PtEtaPhiE))

EPxPyPz = []

for i in range(len(PtEtaPhiE)):

    print("Event: {}".format(i))
    print('PtEtaPhiE[i][0]: {}'.format((PtEtaPhiE[i][0])))

    tau_0 = ROOT.TLorentzVector() 
    lep_0 = ROOT.TLorentzVector() 
    bjet_0 = ROOT.TLorentzVector() 
    met = ROOT.TLorentzVector() 
    jet_0 = ROOT.TLorentzVector() 
    jet_1 = ROOT.TLorentzVector() 

    tau_0.SetPtEtaPhiE(PtEtaPhiE[i][0],PtEtaPhiE[i][1],PtEtaPhiE[i][2],PtEtaPhiE[i][3])
    lep_0.SetPtEtaPhiE(PtEtaPhiE[i][4],PtEtaPhiE[i][5],PtEtaPhiE[i][6],PtEtaPhiE[i][7])
    bjet_0.SetPtEtaPhiE(PtEtaPhiE[i][8],PtEtaPhiE[i][9],PtEtaPhiE[i][10],PtEtaPhiE[i][11])
    met.SetPtEtaPhiE(PtEtaPhiE[i][12],PtEtaPhiE[i][13],PtEtaPhiE[i][14],PtEtaPhiE[i][15])
    jet_0.SetPtEtaPhiE(PtEtaPhiE[i][16],PtEtaPhiE[i][17],PtEtaPhiE[i][18],PtEtaPhiE[i][19])
    jet_1.SetPtEtaPhiE(PtEtaPhiE[i][20],PtEtaPhiE[i][21],PtEtaPhiE[i][22],PtEtaPhiE[i][23])

    EPxPyPz.append([tau_0.E(),tau_0.Px(),tau_0.Py(),tau_0.Pz(),lep_0.E(),lep_0.Px(),lep_0.Py(),lep_0.Pz(),bjet_0.E(),bjet_0.Px(),bjet_0.Py(),bjet_0.Pz(),met.E(),met.Px(),met.Py(),met.Pz(),jet_0.E(),jet_0.Px(),jet_0.Py(),jet_0.Pz(),jet_1.E(),jet_1.Px(),jet_1.Py(),jet_1.Pz(),PtEtaPhiE[i][24]])


with open('EPxPyPz.csv', "w") as s:
    w = csv.writer(s)
    for row in EPxPyPz:
        w.writerow(row)

print("saved")