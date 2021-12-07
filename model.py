class Model():
    def fit(self, data):
        #Fit non implementato
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        #Predict non implementato
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        incr_med = 0
        prediction = 0
        prec=data[0]
        for item in data[1:]:
            #Logica per la predizione
            incr_med += item-prec
            prec = item
        #incr_med/=len(data)-1    
        prediction = incr_med/(len(data)-1) + data[-1]   
        return prediction 

Increment_Model = IncrementModel()
dati_sold = [50,52,60]
print(Increment_Model.predict(dati_sold))                      