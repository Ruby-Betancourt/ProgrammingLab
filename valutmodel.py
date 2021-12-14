from model import FitIncrementModel

from csvfile import NumericalCSVFile

file_p2 = NumericalCSVFile('sales.txt')
only_sales = file_p2.get_data()
dati_pre = []
dati_dop = []
for item in only_sales[:24]:
    dati_pre.append(item)  #primi 24
for item in only_sales[24:]:
    dati_dop.append(item)  #ultimi 12

print(dati_pre)
print(dati_dop)

fit_Incr_Mod = FitIncrementModel()
fit_Incr_Mod.fit(dati_pre[:-3])
predict = fit_Incr_Mod.predict(dati_pre[-3:])
errors = []
error = 






