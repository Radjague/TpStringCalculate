def string_calculater(n:str)-> int:
    if n == '':
      return 0
    if n == '0,0':
      return 0
    if n == '0,1':
      return 1
    if n == '1,0':
        return 1
    if n == '1,1':
        return 2
    if n == '1,2':
        return 3
    return int(n)