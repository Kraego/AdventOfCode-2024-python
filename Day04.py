SEARCH_WORD = 'XMAS'

def readin_data(path : str) -> list[str]:
    with open(path, 'r') as f:
        return [line.rstrip('\n') for line in f]


def horizontal_count(input : list[str]) -> int:
    count = 0

    for line in input:
        count += line.count(SEARCH_WORD)
        count += line[::-1].count(SEARCH_WORD)
    return count


def vertical_count(input : list[str]) -> int:
    transposed = [''.join(x) for x in tuple(zip(*input))]
    return horizontal_count(transposed)


def _reduce_input(input : list[str]) -> list[str]:
    return [[x for x in row[1:]] for row in input[1:]]


def _unfold_diagonal(input : list[str]) -> str:
    if len(input[0]) == 0:
        return ''
    
    unfold = ''
    current = str(input[0][0])

    if len(input) == 1 or len(input[0]) == 1:
        return current
    else:
        unfold += current + _unfold_diagonal(_reduce_input(input))

    return unfold


def _unfold_diagonals(input : list[str]) -> list[str]:
    unfolds = list()

    for r in range(len(input)):
        for c in range(len(input[0])):
            cutoff = len(input[0]) if r == 0 else r
            shifted_input = [[x for x in row[c:cutoff:1]] for row in input[r:]]
            unfolds.append(_unfold_diagonal(shifted_input))

    return unfolds

def dioganal_count(input : list[str]) -> int:
    return horizontal_count(_unfold_diagonals(input))

            
if __name__ == '__main__':
    wordsearch = readin_data('Input/Day04.txt')
    count = horizontal_count(wordsearch)
    count += vertical_count(wordsearch)
    count += dioganal_count(wordsearch)

    print(f'Wordcount for "{SEARCH_WORD}" is {count}');