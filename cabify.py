def cabify(lista_strings) :
  new_lista = []

  for string in lista_strings:
    if string == 'Easy':
      new_lista.append(['Easy Economy', lista_strings.index(string)])
    elif string == 'Lite':
      new_lista.append(['Lite', lista_strings.index(string)])
    elif string == 'Executive':
      new_lista.append(['Executive', lista_strings.index(string)])

  category_cabify = [
    _get_data(new_lista[0][0], lista_strings[new_lista[0][1]:new_lista[1][1]]),
    _get_data(new_lista[1][0], lista_strings[new_lista[1][1]:new_lista[2][1]]),
    _get_data(new_lista[2][0], lista_strings[new_lista[2][1]:])
  ]
  return category_cabify

def _get_data(category, lista):
  print(lista)
  new_obj = {
      'category': category,
      'price': _get_price(lista),
      'time': _get_time(lista)
    }
  return new_obj

def _get_price(lista):
  for string in lista:
    for idx, x in enumerate(string):
      if x == 'S' or x == '$':
        return string.replace('$/', 'S/.')

def _get_time(lista):
  for string in lista:
    for i, x in enumerate(string):
      if x == 'm':
        if string[i + 1] == 'i':
          if string[i - 1] != 'n':
            if string[i - 2] != 'n' :
              return string[i - 2] + string[i - 1] + ' min'
            else :
              return string[i - 1] + ' min'
          else :
            return lista[lista.index(string) - 1] + ' min'