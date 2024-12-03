def readin_data(path : str) -> list[list[int]]:
    with open(path, 'r') as f:
        return [list(map(int, line.rstrip('\n').split(' '))) for line in f]


def is_safe(reports : list[int], dampener : bool = False) -> bool:
    differ_range_min = 1
    differ_range_max = 3
    bad_levels = 0
    increasing = True if reports[0] < reports[1] else False

    for index, level in enumerate(reports[:-1]):
        next_level = reports[index+1]
        differ = next_level - level

        if differ == 0:
            bad_levels += 1
        
        differ = differ * (-1) if not increasing else differ
        
        if not (differ_range_min <= differ <= differ_range_max) or differ == 0:
            bad_levels += 1

        if dampener:
            if bad_levels > 1:
                return False
        else:
            if bad_levels > 0:
                return False

    return True

if __name__ == '__main__':
    reports = readin_data('Input/Day02.txt')
    
    safe = sum(is_safe(level) for level in reports)
    print(f'Safe reports count is {safe}.')
    safe = sum(is_safe(level, True) for level in reports)
    print(f'Safe reports (with dampener) count is {safe}.')