def readin_data():
    with open('Input/Day01.csv', 'r') as f:
        rows = [line.rstrip('\n').split(',') for line in f]
        return ([int(x[0]) for x in rows], [int(x[1]) for x in rows])


def calculate_distance(listA, listB):
    sum = 0

    for a,b in zip(listA, listB): 
        sum += abs(a-b)
    return sum


def calculate_similarity(listA, listB):
    similarity = 0

    for a in listA:
        similarity += a * listB.count(a)
    return similarity

if __name__ == '__main__':
    listA, listB = readin_data()

    print(f'Distance is {calculate_distance(sorted(listA), sorted(listB))}')
    print(f'Similarity is {calculate_similarity(listA, listB)}')