f_dict ={}
with open(r'F:\fileopen homework\1.txt', 'rt') as f1:
    file1 = f1.readlines()
    f_dict['1.txt'] = file1
with open(r'F:\fileopen homework\2.txt', 'rt') as f2:
    file2 = f2.readlines()
    f_dict['2.txt'] = file2
with open(r'F:\fileopen homework\3.txt', 'rt') as f3:
    file3 = f3.readlines()
    f_dict['3.txt'] = file3

sorted_dict = {}
sorted_keys = sorted(f_dict, key=f_dict.get)
for z in sorted_keys:
    sorted_dict[z] = f_dict[z]
key_list = []
for key in sorted_dict.keys():
    key_list.append(key)



