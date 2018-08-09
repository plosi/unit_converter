length_dic = {'m': 1, 'km': 0.001, 'cm': 100, 'mm': 1000, 'mile': 0.00062134, 'yd': 1.09361, 'ft': 3.28084, 'in': 39.3701}

volume_dic = {'l': 1, 'ml': 1000, 'm3': 0.001, 'in3': 61.0237, 'ft3': 0.0353147, 'USgal': 0.264172}


time_dic = {'sec': 1, 'min': 1/60, 'hour': 1/3600, 'day': 1/86400}

dimension = ['volume', 'length', 'time']

def convert(dim, um_in, um_out, value):
  #check if physical dimension is valid
  if dim not in dimension:
    print('invalid physical dimension')
    return
  
  if dim == 'length':
    list_um = list(length_dic.keys())
    list_value = list(length_dic.values())
  elif dim == 'volume':
    list_um = list(volume_dic.keys())
    list_value = list(volume_dic.values())
  elif dim == 'time':
    list_um = list(time_dic.keys())
    list_value = list(time_dic.values())
  
  # check if units are valid
  if um_in not in list_um or um_out not in list_um:
      print('invalid units')
      return
  um_from = list_um.index(um_in)
  um_to = list_um.index(um_out)
  result = value * list_value[um_to] / list_value[um_from]

  #print(value, um_in, 'is ', result, um_out)
  return result

# converting flow units
val = 10
a = val * convert('volume', 'l', 'l', val)/convert('time', 'min', 'hour', val)
#a = convert('volume', 'm3', 'm3', val)
print(a)
