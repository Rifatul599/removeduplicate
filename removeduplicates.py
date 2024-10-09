def remove_duplicate(duplist):
    noduplist = []

    for element in duplist:
        if element not in noduplist:
            noduplist.append(element)

    return noduplist

data=[12,13,45,56,56,78,79,79,80]

print(remove_duplicate(data))