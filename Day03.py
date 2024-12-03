import re

mul_regex = re.compile(r'(mul\([0-9]+,[0-9]+\))')


def readin_data(path : str, with_instructions : bool = False) -> list[(str)]:
    with open(path, 'r') as f:
        content = f.read()
    
    if with_instructions:
        # clear special characters
        content = re.sub(r"([^0-9a-zA-Z,()']+)", '', content)
        # clear everything between "don't()" and do()
        content = re.sub(r"(?<=don't\(\))(.*?)((?=do\(\))|(?=don't)|$)", '',  content)

    return mul_regex.findall(content)


def mulitpy(formula : str) -> int:
    regex = re.compile(r'([0-9]+)')
    factors = regex.findall(formula)

    if len(factors) != 2:
        raise Exception(f'Invalid formula "{formula}"')
    else:
        return int(factors[0]) * int(factors[1])

    
def sum_of_multiplications(multiplications : list[(str)]) -> int:
    return sum([mulitpy(mul) for mul in multiplications])


if __name__ == '__main__':
    multiplications = readin_data('Input/Day03.txt')
    print(f'Sum of multiplications {sum_of_multiplications(multiplications)}')
    multiplications = readin_data('Input/Day03.txt', with_instructions=True)
    print(f'Sum of multiplications with instructions {sum_of_multiplications(multiplications)}')
