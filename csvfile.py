class CSVFile():
    #inizializzo la classe
    def __init__(self, name):
        self.name = name
        #alzare un'eccezione
        if not isinstance(self.name, str):
            raise Exception('il nome "{}" non è una stringa'. format(self.name))


    def get_data(self, start=None, end=None):
    #check errori
        if start is not None:
            #1 sanificazione in interi
            if type(start)==str:
                if start.isdigit()==True:
                    start=int(start)
            if type(start)==float:
                start=int(start)        

            #1 controllo typo start
            if not isinstance(start, int):
                raise TypeError('start = "{}" non è un intero ma è di tipo {}'. format(start, type(start)))

            #2 controllo possibili numeri negativi
            if start<0:
                start = abs(start) 

        if end is not None:
            #1 sanificazione in interi
            if type(end)==str:
                if end.isdigit()==True:
                    end=int(end)
            if type(end)==float:
                end=int(end)        

            #1 controllo typo start
            if not isinstance(end, int):
                raise TypeError('end = "{}" non è un intero ma è di tipo {}'. format(end, type(end)))

            #2 controllo possibili numeri negativi
            if end<0:
                end = abs(end) 

        if start is not None and end is not None:
            #3 controllo ordine start e end
            if start>end:
                temp = start
                start = end 
                end = temp
                print('Forse hai invertito start e end start non può essere maggiore di end')
        


    #inizio funzione
        #inizializzo futura la lista di liste
        finish_list = []

        #apro il file txt
        my_file = open(self.name, 'r')

        #try:
        #    my_file = open('sale.txt', 'r')
        #except FileNotFoundError:
        #    print('Non esiste il file "sale.txt"') 
        #    print('il file giusto da usare si chiama "sales.txt"') 
        #    my_file = open('sales.txt', 'r')

        for line in my_file:
            #split gli element 
            elements = line.split(',')
            #aggiungo ogni lista nella lista finale
            if elements[0] != 'Date':
                finish_list.append(elements)  
            
        finish_list=finish_list[start:end]

        #chiudo il file e return la lista di liste
        my_file.close()
        return finish_list


my_file = CSVFile('sales.txt')
print(my_file.get_data(None,10))

#error_file = CSVFile(32)

class NumericalCSVFile(CSVFile):
    pass

    def get_data(self):
        data = super().get_data()  
        use = []


        for item in data:
            for x in item[1:]:
                try:
                    x = float(x)
                    use.append(x)
                except ValueError:    
                    print('il tipo dell\'item è: {}'.format(type(x)))

        return use            

file_p2 = NumericalCSVFile('sales.txt')
#print(file_p2.get_data())



            