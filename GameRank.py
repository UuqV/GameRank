



with open ("Month1.csv", "r") as data:
    Month1 = data.readlines()


for match in Month1:
    print match.split(',\n')