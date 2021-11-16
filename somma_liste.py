
def somma_liste(the_list):
  som=0
  for number in the_list:
    som = som + number  
  print('Risultato: {}'. format(som))  
  return som  


the_list = [1,2,3,4]
somma_liste (the_list)       
           