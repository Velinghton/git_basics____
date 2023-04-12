#!/usr/bin/env python3

from task_5 import *


if __name__ == '__main__':
    
    print("Exempel dict which we use:\n")
    
    dict1 = {"one": 1, "two": 2, "three": 3, "ten": 10}
    dict2 = {"four": 6, "five": 5, "six": 6, "ten": 10}
    
    print(f'dict1 = {dict1}')
    print(f'dict2 = {dict2}')
    print()
    

    resalt = [(update_dict(dict1, dict2)),
              (intersection_dict(dict1, dict2)),
              (differense_dict(dict1, dict2)),
              (symmetric_differense_dict(dict1, dict2)),
              (sort_dict_key(dict1)),
              (sort_dict_value(dict1)),
              (change_k_v(dict1))]
    res = ["update_dict", "intersection_dict", "differense_dict", "symmetric_differense_dict",
              "sort_dict_key", "sort_dict_value", "change_k_v"]
    for i in range(len(res)):
        print(f'Resalt of {res[i]}: {resalt[i][0]}')
        print(f'{resalt[i][1]}\n')
  
   

    
