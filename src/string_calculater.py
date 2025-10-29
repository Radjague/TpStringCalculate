def string_calculater(n:str)-> int:
    if n == '':
      return 0
    parts = n.split(',')
    total = 0
    for num in parts:
        total += int(num)
    return total
