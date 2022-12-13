import json
import csv

def read_txt(name_file):
    with open(name_file, 'r', encoding='utf-8') as file_file:
        file = file_file.read().split('\n\n\n')
        end_version = []
        for i in range(len(file)):
            end_version.append(file[i].split('\n\n'))

        return end_version


def read_json(name_file):
    with open(name_file, 'r', encoding='utf-8') as file_file:
        file = json.load(file_file)
        result = list(map(lambda x: list(map(lambda a: a, x.values())), file))
        return result


def read_csv(name_file):
    with open(name_file, 'r', encoding='utf-8') as csv_file:
        r = csv.reader(csv_file)
        r = list(r)[1:]
        return r
