class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, window):
        self.w = window

    def compute (self, lista):
        media = []
        somma = 0

        #Casi particolari
        if not isinstance(self.w, int):
            raise ExamException('TypeError, la lunghezza della finestra non è un intero')

        if not isinstance(lista, list):
            raise ExamException('TypeError, l\'input non è una lista')

        for el in lista:
            if not isinstance(el, int) and not isinstance(el, float):
                raise ExamException('TypeError, uno o più elementi della lista non sono int o float')

        if(len(lista) == 0):
            raise ExamException('Errore, lista vuota')

        if(len(lista)< self.w):
            raise ExamException('Errore, il numero di valori della lista non sono sufficienti')
                  

        if (self.w == 1): 
            return lista

        elif (self.w == len(lista)):
            for i in range (self.w):
                somma += lista[i]
            media.append(somma/self.w)
        
        else :
            for j in range(len(lista)-self.w+1):
                for i in range(self.w):
                    somma += lista[j+i]
                media.append(somma/self.w)   
                somma = 0

        return media        


moving_averange = MovingAverage(2)
#try0 = moving_averange.compute([])
#try1 = moving_averange.compute([2,4,8,16])
#try2 = moving_averange.compute([0])
try3 = moving_averange.compute([4,8])
#try4 = moving_averange.compute([None])
try5 = moving_averange.compute([1,2,3,-1,-5])
try6 = moving_averange.compute([1.32,4.6,7,-5.5])
#try7 = moving_averange.compute([3,6,'2',10])
#try8 = moving_averange.compute([2,43,None])
#try9 = moving_averange.compute([9,[3],54,5.20])

mov0 = MovingAverage(4.5)
#try10 = mov0.compute([2,4,8,16])
mov1 = MovingAverage('43')
#try11 = mov1.compute([2,4,8,16])
mov2 = MovingAverage(1)
try12 = mov2.compute([2,4,8,16])
