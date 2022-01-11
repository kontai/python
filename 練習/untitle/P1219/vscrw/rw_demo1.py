import csv

# villains = [
#     ['Doctor', 'No'],
#     ['Rosa', 'Klebb'],
#     ['Mister', 'Big'],
#     ['Auric', 'GoldFinger'],
#     ['Ernst', 'Blofeld']
# ]
#
# with open("villains","w") as fout:
#     csvout=csv.writer(fout)
#     csvout.writerow(villains)

with open("villains","r") as fin:
    csvin=csv.reader(fin)
    villains=[row for row in csvin]
print(villains)