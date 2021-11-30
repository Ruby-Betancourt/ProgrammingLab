class CSVFile():
    #inizializzo la classe
    def __init__(self, name):
        self.name = name
        #alzare un'eccezione
        if not isinstance(self.name, str):
            raise Exception('il nome "{}" non è una stringa'. format(self.name))


    def get_data(self, start=None, end=None):
        #inizializzo futura la lista di liste
        finish_list = []

        

        #sanificazione
        if type(start)==str:
            if start.isdigit()==True:
                start=int(start)
        if type(start)==float:
            start=int(start)        


        #controllo errori
        if not isinstance(start, int):
            raise Exception('start = "{}" non è un intero ma è di tipo {}'. format(start, type(start)))

        if start<0 or end<0:
            start = abs(start)
            end = abs(end) 

        if start>end:
            temp = start
            start = end 
            end = temp
            print('Forse hai invertito start e end start non può essere maggiore di end')

           
        

        #apro il file txt
        my_file = open('sales.txt', 'r')

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
print(my_file.get_data(10,5))

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



            