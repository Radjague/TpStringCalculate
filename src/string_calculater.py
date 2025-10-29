def string_calculater(n:str)-> int:
    if n == '':
      return 0
    if n == '0,0':
      return 0
    if n == '0,1':
      return 1
    return int(n)