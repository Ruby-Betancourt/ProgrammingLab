class CSVFile():
  #inizializzo la classe
  def __init__(self, name):
    self.name = name

  def get_data(self):
    #inizializzo futura la lista di liste
    finish_list = []
    #
    my_file = open('sales.txt', 'r')
    for line in my_file:
      elements = line.split(',')

      if elements[0] != 'Date':
        data = elements[0]
        value = elements[1]

        first_list = [elements[0], elements[1]]
        finish_list.append(float(element))    
    my_file.close()
    return finish_list

mio_file = CSVFile('sales.txt')
mio_file.get_data()

    
            