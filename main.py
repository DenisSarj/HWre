import re
from pprint import pprint
import csv

with open("readfile.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    pprint(contacts_list)
    pattern = re.compile(
        r'([аА-яЯ]+)[\s,]([аА-яЯ]+)[\s,]*([аА-яЯ]+)?[,\s]*([аА-яЯ]+)?[,\s]*([аА-яЯ\s–c]+)?[,\s]*(\+7|8)?\s*\(*(\d{3})?\)*[-\s]*(\d{3})?-*(\d{2})?-*(\d{2})?[,\s]*\(*([а-я.]+)?\s*(\d*)\)*[,\s]*([^аА-яЯ\s]+)?')

    formatted_row_list = []

    for item in contacts_list:
        formatted_data = re.sub(pattern, r'\1, \2, \3, \4, \5, +7(\7)\8-\9-\10 доб.\12, \13', ', '.join(item))
        formatted_row_list.append(formatted_data)

    formatted_row_dict = {}

    for item in formatted_row_list:

        if item.split(' ')[0] not in formatted_row_dict.keys():
            formatted_row_dict[item.split(' ')[0]] = item.split(' ')[1:]

        for item2 in formatted_row_dict[item.split(' ')[0]]:
            if item2 not in formatted_row_dict[item.split(' ')[0]]:
                formatted_row_dict[item.split(' ')[0]].extend(item2)

    union_list = []

    for key, val in formatted_row_dict.items():
        b = [key, *val]
        k = ', '.join(b).replace(', ', ' ')
        c = k.split(',')
        union_list.append(c)
        # union_list.extend(val)
    a = union_list
    # pprint(a)
    # pprint(', '.join(l))
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')

    datawriter.writerows(a)
