import numpy as np


def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  else:
    my_array = np.array(list).reshape(3, 3)
    dict = {
      'mean': [],
      'variance': [],
      'standard deviation': [],
      'max': [],
      'min': [],
      'sum': []
    }
    dict['mean'].append(np.mean(my_array, axis=0).tolist())
    dict['mean'].append(np.mean(my_array, axis=1).tolist())
    dict['mean'].append(np.mean(my_array))
    dict['variance'].append(np.var(my_array, axis=0).tolist())
    dict['variance'].append(np.var(my_array, axis=1).tolist())
    dict['variance'].append(np.var(my_array))
    dict['standard deviation'].append(np.std(my_array, axis=0).tolist())
    dict['standard deviation'].append(np.std(my_array, axis=1).tolist())
    dict['standard deviation'].append(np.std(my_array))
    dict['max'].append(np.max(my_array, axis=0).tolist())
    dict['max'].append(np.max(my_array, axis=1).tolist())
    dict['max'].append(np.max(my_array))
    dict['min'].append(np.min(my_array, axis=0).tolist())
    dict['min'].append(np.min(my_array, axis=1).tolist())
    dict['min'].append(np.min(my_array))
    dict['sum'].append(np.sum(my_array, axis=0).tolist())
    dict['sum'].append(np.sum(my_array, axis=1).tolist())
    dict['sum'].append(np.sum(my_array))

  return dict
