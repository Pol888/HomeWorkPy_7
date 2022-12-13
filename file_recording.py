import json
import csv


def write_json(name_file, file):
    heads = ['surname', 'name', 'phone', 'comment']
    result_dict = []
    for i in file:
        result_dict.append({heads[0]: i[0], heads[1]: i[1], heads[2]: i[2], heads[3]: i[3]})

    with open(name_file, 'w', encoding='utf-8') as file_file:
        json.dump(result_dict, file_file)



def write_txt(name_file, file):
    result = ''
    for i in file:
        result += '\n\n'.join(i) + '\n\n\n'

    with open(name_file, 'w', encoding='utf-8') as file_file:
        file_file.write(result)


def write_csv(name_file, file):
    with open(name_file, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['surname', 'name', 'phone', 'comment'])
        for row in file:
            writer.writerow(row)


