import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
# ki = keamananan informasi
# kp = kepuasan pelayaan
# kps= kemempuan petugas
# ks = ketersedian sapras
ki   = ctrl.Antecedent(np.arange(0,101,1), 'ki')
kp   = ctrl.Antecedent(np.arange(0,101,1), 'kp')
kps  = ctrl.Antecedent(np.arange(0,101,1), 'kps')
ks   = ctrl.Antecedent(np.arange(0,101,1), 'ks')
#kpn = kepuasan pelayanan
kpn  = ctrl.Consequent(np.arange(0,401,1), 'kpn')

#tm = tidak_memuaskan
#km = kurang_memuaskan
#cm = cukup memuaskan
#m  = memuaskan
#sm = sangat memuaskan
ki['tm']        = fuzz.trimf(ki.universe, [0,60,75  ])
ki['cm']        = fuzz.trimf(ki.universe, [60,75,90 ])
ki['m']         = fuzz.trimf(ki.universe, [75,90,100])

kp['tm']        = fuzz.trimf(kp.universe, [0,60,75  ])
kp['cm']        = fuzz.trimf(kp.universe, [60,75,90 ])
kp['m']         = fuzz.trimf(kp.universe, [75,90,100])

kps['tm']       = fuzz.trimf(kps.universe, [0,60,75  ])
kps['cm']       = fuzz.trimf(kps.universe, [60,75,90 ])
kps['m']        = fuzz.trimf(kps.universe, [75,90,100])

ks['tm']        = fuzz.trimf(ks.universe, [0,60,75  ])
ks['cm']        = fuzz.trimf(ks.universe, [60,75,90 ])
ks['m']         = fuzz.trimf(ks.universe, [75,90,100])

kpn['tm']       = fuzz.trimf(kpn.universe, [0,50,75])
kpn['km']       = fuzz.trapmf(kpn.universe, [50,75,100,150])
kpn['cm']       = fuzz.trapmf(kpn.universe, [100,150,250,275])
kpn['m']        = fuzz.trimf(kpn.universe, [250,275,325])
kpn['sm']       = fuzz.trimf(kpn.universe, [325,350,400])

aturan_1  = ctrl.Rule(ki['tm']& kp['tm']& kps['tm']& ks['tm'], kpn['tm'])
aturan_2  = ctrl.Rule(ki['tm']& kp['tm']& kps['tm']& ks['cm'], kpn['tm'])
aturan_3  = ctrl.Rule(ki['tm']& kp['tm']& kps['tm']& ks['m'],  kpn['tm'])
aturan_4  = ctrl.Rule(ki['tm']& kp['tm']& kps['cm']& ks['tm'], kpn['tm'])
aturan_5  = ctrl.Rule(ki['tm']& kp['tm']& kps['cm']& ks['cm'], kpn['tm'])
aturan_6  = ctrl.Rule(ki['tm']& kp['tm']& kps['cm']& ks['m'],  kpn['cm'])
aturan_7  = ctrl.Rule(ki['tm']& kp['tm']& kps['m']&  ks['tm'], kpn['tm'])
aturan_8  = ctrl.Rule(ki['tm']& kp['tm']& kps['m']&  ks['cm'], kpn['cm'])
aturan_9  = ctrl.Rule(ki['tm']& kp['tm']& kps['m']&  ks['m'],  kpn['cm'])
aturan_10 = ctrl.Rule(ki['cm']& kp['cm']& kps['cm']& ks['m'],  kpn['m'] )
aturan_11 = ctrl.Rule(ki['cm']& kp['m']&  kps['m']&  ks['m'],  kpn['m'] )
aturan_12 = ctrl.Rule(ki['m']&  kp['m']&  kps['m']&  ks['m'],  kpn['sm'])
aturan_13 = ctrl.Rule(ki['cm']& kp['tm']& kps['tm']& ks['m'],  kpn['km'])
aturan_14 = ctrl.Rule(ki['m']&  kp['tm']& kps['tm']& ks['m'],  kpn['cm'])


engine = ctrl.ControlSystem([aturan_1, aturan_2, aturan_3, aturan_4,aturan_5,aturan_6,aturan_7,aturan_8,aturan_9,aturan_10,aturan_11,aturan_12,aturan_13])
system = ctrl.ControlSystemSimulation(engine)

system.input["ki"] = 80
system.input["kp"] = 60
system.input["kps"] = 50  
system.input["ks"] = 90
system.compute()

print(f"Hasil kepuasan pelayanan: {system.output['kpn']:.2f}")
kpn.view(sim=system)
input("Tekan ENTER untuk melanjutkan")