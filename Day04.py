def readin_data(path : str) -> list[str]:
    with open(path, 'r') as f:
        return [line.rstrip('\n') for line in f]


def search_from(input, word, row, column, dir_y, dir_x):
    rows, cols = len(input), len(input[0])

    for i, current in enumerate(word):
        new_row, new_column = row + dir_y * i, column + dir_x * i
        if not (0 <= new_row < rows and 0 <= new_column < cols) or input[new_row][new_column] != current:
            return False
    return True


def count_word_occurence(input : list[str], word : str) -> int:
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
        (-1, -1), # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1)    # down-right
    ]

    rows, cols = len(input), len(input[0])
    count = 0

    for row in range(rows):
        for column in range(cols):
            for dir_y, dir_x in directions:
                if search_from(input, word, row, column, dir_y, dir_x):
                    count += 1

    return count


def count_x_word_occurence(input : list[str], word : str) -> int:
    directions = [
        (-1, -1), # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1)    # down-right
    ]

    rows, cols = len(input), len(input[0])
    count = 0

    for row in range(rows):
        for column in range(cols):
            count_for_dir = 0
            for dir_y, dir_x in directions:
                if search_from(input, word, row, column, dir_y, dir_x):
                    count_for_dir += 1
            count += 1 if count_for_dir >= 2 else 0

    return count 

            
if __name__ == '__main__':
    wordsearch = readin_data('Input/Day04.txt')
    search_word = 'XMAS'
    count =  count_word_occurence(wordsearch, search_word)
    print(f'Wordcount for "{search_word}" is {count}');
    search_word = 'MAS'
    count =  count_x_word_occurence(wordsearch, search_word)
    print(f'X-Wordcount for "{search_word}" is {count}');
