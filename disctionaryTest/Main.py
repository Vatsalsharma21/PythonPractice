import yaml


list_programming_dictionary = []
programming_dictionary = {'Key 1':'value 1','Key 2':'value 2',
                          'Key 3':['workflow 1','workflow 2','workflow 3']}

programming_dictionary2 = {'Key 1':'value 1','Key 2':'value 2',
                          'Key 3':['workflow 1','workflow 2','workflow 3']}

programming_dictionary3 = {'Key 1':'value 1','Key 2':'value 2',
                          'Key 3':[]}

def write_to_yaml(data):
    with open('outputfile.yaml','w') as file:
        yaml.dump(data,file)

print(programming_dictionary)
print(programming_dictionary.get('Key 2'))
print(programming_dictionary.items())
print(programming_dictionary)

list_programming_dictionary.append(programming_dictionary)
list_programming_dictionary.append(programming_dictionary2)
list_programming_dictionary.append(programming_dictionary3)
print(list_programming_dictionary)

write_to_yaml(list_programming_dictionary)

