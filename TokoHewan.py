import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

Barang_Terjual = ctrl.Antecedent(np.arange(0,101,1), 'Barang_Terjual')

Barang_Terjual['rendah'] = fuzz.trimf(Barang_Terjual.universe, [0,0, 40])
Barang_Terjual['sedang'] = fuzz.trimf(Barang_Terjual.universe, [30, 50, 70])
Barang_Terjual['tinggi'] = fuzz.trimf(Barang_Terjual.universe, [60,100,100])

Permintaan = ctrl.Antecedent(np.arange(0,301,1), 'Permintaan')

Permintaan['rendah'] = fuzz.trimf(Permintaan.universe, [0, 0, 100])
Permintaan['sedang'] = fuzz.trimf(Permintaan.universe, [50, 150, 250 ])
Permintaan['tinggi'] = fuzz.trimf(Permintaan.universe, [200, 300,300])

Harga_Peritem = ctrl.Antecedent(np.arange(0,100001,1), 'Harga_Peritem')

Harga_Peritem['murah'] = fuzz.trimf(Harga_Peritem.universe, [0, 0, 40000])
Harga_Peritem['sedang'] = fuzz.trimf(Harga_Peritem.universe, [30000, 50000, 80000 ])
Harga_Peritem['mahal'] = fuzz.trimf(Harga_Peritem.universe, [60000, 100001,100001])

Profit = ctrl.Antecedent(np.arange(0,4000001,1), 'Profit')

Profit['rendah'] = fuzz.trimf(Profit.universe, [0, 0, 1000000])
Profit['sedang'] = fuzz.trimf(Profit.universe, [1000000, 2000000, 2500000 ])
Profit['banyak'] = fuzz.trimf(Profit.universe, [1500000, 2500000,4000000])

Stok_Makanan = ctrl.Consequent(np.arange(0, 1001, 1), 'Stok_Makanan')

Stok_Makanan['sedang'] = fuzz.trimf(Stok_Makanan.universe, [100, 500, 900])
Stok_Makanan['banyak'] = fuzz.trimf(Stok_Makanan.universe, [600, 1000, 1000 ])

aturan_1 = ctrl.Rule(Barang_Terjual["tinggi"] & Permintaan["tinggi"]& Harga_Peritem["murah"]& Profit['banyak'], Stok_Makanan["banyak"])
aturan_2 = ctrl.Rule(Barang_Terjual["tinggi"] & Permintaan["tinggi"]& Harga_Peritem["murah"]& Profit["sedang"], Stok_Makanan["sedang"])
aturan_3 = ctrl.Rule(Barang_Terjual["tinggi"] & Permintaan["sedang"]& Harga_Peritem["murah"]& Profit["sedang"], Stok_Makanan["sedang"])
aturan_4 = ctrl.Rule(Barang_Terjual["sedang"] & Permintaan["tinggi"]& Harga_Peritem["murah"]& Profit["sedang"], Stok_Makanan["sedang"])
aturan_5 = ctrl.Rule(Barang_Terjual["sedang"] & Permintaan["tinggi"]& Harga_Peritem["murah"]& Profit["banyak"], Stok_Makanan["banyak"])
aturan_6 = ctrl.Rule(Barang_Terjual["rendah"] & Permintaan["rendah"]& Harga_Peritem["sedang"]& Profit["sedang"], Stok_Makanan["sedang"])

engine = ctrl.ControlSystem([aturan_1, aturan_2, aturan_3, aturan_4,aturan_5,aturan_6])
system = ctrl.ControlSystemSimulation(engine)

system.input["Barang_Terjual"] = 80
system.input["Permintaan"] = 255
system.input["Harga_Peritem"] = 25000  
system.input["Profit"] = 3500000
system.compute()
print(f"Hasil Stok Makanan: {system.output['Stok_Makanan']}")
Stok_Makanan.view(sim=system)
input("Tekan ENTER untuk melanjutkan")