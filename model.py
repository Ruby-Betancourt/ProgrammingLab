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
        for item in data[:-3]:
            incr_prec += item-prec
            prec = item
        predict_prec = incr_prec/(len(data)-4)
        print(predict_prec)
        self.global_avg_incrementi = predict_prec

    def predict(self, data):
        predict_3 = super().predict(data)
        predict_3 -= data[-1]
        #predict_prec = fit(self.data)
        print(predict_3)
       
        prediction = (predict_3 + self.global_avg_incrementi)/2 + data[-1]
        return prediction
     


Increment_Model = IncrementModel()
dati_sold = [50,52,60]
#print(Increment_Model.predict(dati_sold))
Fit_Increment_Model = FitIncrementModel()    
more_dati_sold = [8,19,31,41,50,52,60] 
Fit_Increment_Model.fit(more_dati_sold)
print(Fit_Increment_Model.predict(dati_sold))
