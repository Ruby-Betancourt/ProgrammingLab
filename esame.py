from datetime import datetime

class ExamException(Exception):
    pass                  

class CSVFile():
    #inizializzo la classe
    def __init__(self, name):
        self.name = name
        
        #controllo che sia una stringa
        if not isinstance(self.name, str):
            raise ExamException('TypeError, "{}" non è una stringa'. format(self.name))
    

    def get_data(self):
        #inizializzo la lista finale che conterrà le altre minori
        finish_list = []

        #provo ad aprire il file
        try:
            my_file = open(self.name, 'r')
        except:
            #in caso non riesca ad aprire il file
            raise ExamException('NotFoundError, file non esiste o non è legibile')

        for line in my_file:
            #separo la stringa sulla virgola
            elements = line.split(',')

            #elimino tutti caratteri '\n' per amdare a capo
            elements[-1] = elements[-1].strip()

            #aggiungo le liste minori nella lista finale
            if elements[0] != 'date':
                finish_list.append(elements)  
        
        #chiudo il file e return la lista finale completa
        my_file.close()
        return finish_list


#sottoclasse di CSVFile che eredita l'init
class CSVTimeSeriesFile(CSVFile):

    def get_data(self):
        #richiamo il metodo della classe madre
        data = super().get_data()
        new_list = []
        
        #ciclo per controllare i dati passeggero
        for item in data:
            #controllo che ci siano
            if len(item)<2:
                #controllo che non sia una lista vuota
                if item == []:
                    raise ExamException('Error, lista vuota')
                #controllo se l'unico elemento presente è una data
                try:
                    date1=datetime.strptime(item[0], '%Y-%m')
                    #allora aggiungo i dati passeggeri come None
                    item.append(None)
                except:
                    #altrimenti salto la riga
                    continue
                
            #controllo che non siano una stringa vuota
            elif item[1]=='':
                item[1]= None 
                
            #controllo che si possano trasformare in intero
            elif not item[1].isdigit():
                item[1]=None

            #trasformo i dati dei passeggeri in intero
            else:
                item[1] = int(item[1])
            
            #controllo le date
            #controllo se il primo elemento è una data
            try:
                date1=datetime.strptime(item[0], '%Y-%m')
            except:
                #altrimenti salto la riga
                continue    


            #aggiungo ogni lista nella nuova lista corretta 
            new_list.append(item[:2])  


        #prima data dell'intero file come termine di paragone
        date1=data[0][0]
        #ciclo per controllare che le date siano strettamente crescenti
        for item in new_list[1:]:
            #date_=datetime.strptime(item[0], '%Y-%m')
            #controllo siano crescenti e non si ripetano
            if date1>=item[0]:
                raise ExamException('Error, le date nel fine non sono in ordine, {} va dopo {}'. format(date1, item[0]))
            date1 = item[0]   
        

        #ritorno la lista corretta
        return new_list 



def compute_avg_monthly_difference(lista, start, end):
    #controlli sull'anno iniziale (start) e finale (end)

    #controllo che siano una stringa
    if not isinstance(start, str):
        raise ExamException('TypeError, l\'anno iniziale non è una stringa')

    if not isinstance(end, str):
        raise ExamException('TypeError, l\'anno finale non è una stringa')

    #controllo che non siano una stringa vuota
    if start == '':
        raise ExamException('Error, l\'anno iniziale è una stringa vuota')

    if end == '':
        raise ExamException('Error, l\'anno finale è una stringa vuota')

    #controllo che siano una stringa di solo numeri
    if not start.isdigit():
        raise ExamException('Error, l\'anno iniziale non è un numero intero')

    if not end.isdigit():
        raise ExamException('Error, l\'anno finale non è un numero intero')    


    #trasformo le date in interi
    start=int(start)
    end=int(end)


    #controllo che siano compresi nel file 
    #if start<1949:
     #   raise ExamException('Error, l\'anno iniziale non compare nel file')

    #if end>1960:
     #   raise ExamException('Error, l\'anno finale non compare nel file')

    #controllo che l'ordine delle date sia giusto
    if start>end:
        raise ExamException('Error, forse hai invertito l\'anno iniziale e finale, start non può essere maggiore di end')


    #inizio funzione
    lista_finale = []
    tot_anni = end-start
    passengers = []
    somma=0
    m=0

    #creo una lista per ogni anno che devo considerare    
    for i in range (tot_anni+1):
        lista_anno = [None,None,None,None,None,None,None,None,None,None,None,None]
        #l'ultimo elemento di ogni lista è l'anno di cui fanno riferimento i dati
        lista_anno.append(start+i)
        passengers.append(lista_anno)

    #riempo le liste con i dati dei passeggeri     
    for data in passengers:
        for item in lista:
            elem = item[0].split('-')
            #solo se l'anno corrisponde all'anno nella lista i dati vengono aggiunti
            if int(elem[0]) == data[-1]:
                data[int(elem[1])-1] = item[1]  
            

    #calcolo la media per ogni mese
    while m<=11:
    #for m in range(11):
        for y in range(tot_anni):
            #gestisco i casi particolari
            if passengers[y+1][m]==None or passengers[y][m]==None:
                diff = 0
            else:
                diff = passengers[y+1][m]-passengers[y][m]
            somma+=diff
        lista_finale.append(somma/tot_anni)
        somma=0 
        m+=1  

    return lista_finale