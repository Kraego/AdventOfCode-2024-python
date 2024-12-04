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


def _unfold_dioganals(input : list[str]) -> list[str]:
    # (0,0) (1,1) (2,2) (3,3)
    # (0,1) (2,2) (3,3)
    # (0,2) (1,3)
    # (0,3) 

    # (1,0) (2,1) (3,2)
    # (1,1) (2,2) (3,3)
    # (1,2) (2,3)
    # (1,3)
    unfold = list()
    for y in range(len(input)):
        y_idx = y
        for x in range(len(input[y])):
            print((y_idx,x))
            y_idx += 1
            if y_idx == len(input):
                break
        print()
        #unfold.append(line)
    return unfold


def dioganal_count(input : list[str]) -> int:
    unfolded = _unfold_dioganals(input)
    return horizontal_count(unfolded)
            
    
if __name__ == '__main__':
    wordsearch = readin_data('Input/Day04.txt')
    # count = horizontal_count(wordsearch)
    # count += vertical_count(wordsearch)
    count = dioganal_count(wordsearch)

    print(f'Wordcount for "{SEARCH_WORD}" is {count}');