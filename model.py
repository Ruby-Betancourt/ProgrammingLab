class Model():
    def fit(self, data):
        #Fit non implementato
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #Predict non implementato
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        #Controllo che passimo una lista
        if type(data)!=list:
            raise TypeError ('L\'argomento non è una lista')
        
        #controllo se tutti gli elementi della lista siano interi
        for item in data:
            if not isinstance(item, int) and not isinstance(item, float):
                raise TypeError ('I dati non sono numeri')

        #controllo che sia sufficienti
        if len(data)<=2:
            raise Exception ('I dati non sono sufficienti')

        #controllo sia stato passato qualcosa
        if data == None:
            raise Exception ('Non mi hai passato nessun dato')
        
        incr_med = 0
        prediction = 0
        prec=data[0]
        for item in data:
            #Logica per la predizione
            incr_med += item-prec
            prec = item
        #incr_med/=len(data)-1    
        prediction = incr_med/(len(data)-1) + data[-1]   
        return prediction 

class FitIncrementModel(IncrementModel):
    def fit(self, data):
        incr_prec = 0
        prec = data[0]
        predict_prec = 0
        for item in data:
            incr_prec += item-prec
            prec = item
        predict_prec = incr_prec/(len(data)-1)
        #print('Incremento mesi passati: {}'.format(predict_prec))
        self.global_avg_incr = predict_prec

    def predict(self, data):
        predict_3 = super().predict(data)
        predict_3 -= data[-1]
        #print('Incremento ultimi tre mesi: {}'.format(predict_3))
        
        try:
            prediction = (predict_3 + self.global_avg_incr)/2 + data[-1]
            #print('Try: {}'.format(prediction))
        except:
            print('Non hai effettuato il fit, la vecchia prediction era: ')
            prediction = predict_3 + data[-1]
            #print('Except: {}'. format(prediction))

        return prediction
     

Increment_Model = IncrementModel()
dati_sold = [50,52,60]
#print(Increment_Model.predict(dati_sold))

Fit_Increment_Model = FitIncrementModel()    
fit_dati_sold = [8,19,31,41] 
Fit_Increment_Model.fit(fit_dati_sold)
print(Fit_Increment_Model.predict(dati_sold))


from csvfile import NumericalCSVFile

file_p2 = NumericalCSVFile('sales.txt')
only_sales = file_p2.get_data()
dati_pre = []
dati_dop = []
for item in only_sales[:24]:
    dati_pre.append(item)
for item in only_sales[24:]:
    dati_dop.append(item)

#print(dati_pre)
#print(dati_dop)

    

