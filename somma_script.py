def somma_valori(input_file):
  #inizializzo una variabile per salvare il risultato
  somma=0.0

  #apro e leggo il file, linea per linea
  my_file = open('sales.txt', 'r')
  for line in my_file:

    #faccio lo split di ogni riga sulla virgola
    elements = line.split(',')

    #se non sto processando l'intestazione
    if elements[0] != 'Date':

        #setto il valore
        value = elements[1]

        #sommo tutti i value
        somma+=(float(value))

  my_file.close()
  #stampo il risultato finale 
  print('Risultato:{}'. format(somma)) 
  return somma

somma_valori('sales.txt')