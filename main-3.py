string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed " \
         "thought "

def filter_by_number(num_list: (list or tuple), number: (str or int)) -> list:
    """
    Находит все числа в списке num_list, которые содержат в себе цифру number
    """
    return list(filter(lambda x: str(number) in str(x), num_list))


def find_palindromes(num_list: (list or tuple)) -> list:
    """
    Находит все числа в списке num_list, которые являются палиндромом(одинаково читающееся в обоих направлениях)
    """
    return list(filter(lambda x: str(x) == str(x)[::-1] and len(str(x)) > 1, num_list))


def count_symbols(string: str, smb: str) -> int:
    """
    Считает количество символов smb в строке string
    """
    return string.lower().count(smb.lower())


def remove_symbol(string: str, symbols: str) -> str:
    """
    Убирает символы symbols(прим. 'aeiouyAEIOUY') в строке string
    """
    return ''.join((list(filter(lambda x: x not in symbols, string))))


 
def find_words_by_lenght(string: str, lenght_of_word: int) -> list:
    """
    Находит все слова в строке string с длиной слова lenght_of_word
    """
    return list(filter(lambda x: len(x) <= lenght_of_word, string.split()))


def create_dict_count_words_lenght(string: str) -> dict:
    """
    Возвращает словарь, где в качестве ключа используются слова из разделённой по пробелам строки string,
    а в значении длина lenght_of_word слов.
    """
    return {word: len(word) for word in string.split()}


def find_unique_symbols(string: str) -> list:
    """
    На входе предложение со всеми пробельными и непробельными символами латинского алфавита.
    Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.
    """
    return list(set(string))


def square_every_number(numbers_list: list) -> list:
    """
    Возводит в квадрат все числа в списке numbers_list
    """
    return list(map(lambda x: x**2, numbers_list))


def create_dict_good_coordinates_and_distance_to_them(coordinates) -> dict:
    """
    На входе список координат, например, [(1, 1), (2, 3), (5, 3)].
    Найти все точки, которые принадлежат прямой y = 5 * x - 2.
    На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)
    """

    return {(x, y): (x * 2 + y * 2) ** 0.5 for x, y in coordinates if 5 * x - 2 == y}


def square_even_numbers_from_2_to_27() -> list:
    """
    Возводит в квадрат все четные числа от 2 до 27..
    """
    return list(map(lambda x: x ** 2, range(2, 27, 2)))


def get_distance_to_farthest_point(coordinates: list[tuple]) -> int:
    """
    Расстояние до самой удаленной точки от начала координат (0, 0) в первой четверти
    """
    return max([(x * 2 + y * 2) ** 0.5 for x, y in coordinates if x >= 0 and y >= 0])


def add_lists_to_each_other(nums_first: list, nums_second: list) -> list:
    """
    Складывает списки между собой
    На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32].
    Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]
    """
    return [(x + y, x - y) for x, y in zip(nums_first, nums_second)]


def even_square_numbers(list_of_strings: list[str]) -> list:
    """
    Находит все чётные квадраты чисел list_of_strings
    """
    return [int(elem) ** 2 for elem in list_of_strings if (int(elem) ** 2) % 2 == 0]


def convert_to_dict(string: str) -> list:
    """
    Конвертирует строку в удобночитаемый и импортируемый формат
    """
    keys = [line.split(',')[0] for line in string.split()]
    other = list(zip(*(line.split(',')[1:] for line in string.split())))
    return list(dict(zip(keys, elem)) for elem in other)


def sum_matrix_columns(nums_list) -> list:
    """
    Получить сумму по столбцам у двумерного списка nums_list
    """
    return [sum(row[i] for row in nums_list) for i in range(len(nums_list[0]))]


if __name__ == '__main__':
    list_of_nums_divided_by_seventeen = filter_by_divider(num_list=range(1, 1000), divider=17)

    list_of_nums_filtered_by_two = filter_by_number(num_list=range(1, 1000), number=2)

    list_of_palindromes = find_palindromes(num_list=range(1, 1000))

    spaces_count = count_symbols(string='Посчитать количество пробелов в строке', smb=' ')

    string_wo_vowels = remove_symbol(string='IUADSBFIAOUYHSDBDIAWEYB', symbols='aeiouyAEIOUY')

    words_with_lenght_five = find_words_by_lenght(string='На входе строка со словами, разделенными через 1 пробел.',
                                                  lenght_of_word=5)

    words_with_lenght_dict = create_dict_count_words_lenght("""В качестве ключа используется само слово,
                                                             а в значении длина этого слова.""")

    unique_symbols = find_unique_symbols(
     string='Get a dictionary of used letters in a string, the output is a list of unique letters')

    squared_numbers = square_every_number([2, 5, 10, 50])

    good_coordinates = create_dict_good_coordinates_and_distance_to_them(coordinates=[(2, 8), (3, 13), (5, 3)])

    squared_even_numbers = square_even_numbers_from_2_to_27()

    distance_to_farthest_point = get_distance_to_farthest_point([(2, 8), (3, 13), (5, 3)])

    new_list = add_lists_to_each_other(nums_first=[1, 2, 3, 5, 8], nums_second=[2, 4, 8, 16, 32])

    even_square_numbers = even_square_numbers(list_of_strings=['43141', '32441', '431', '4154', '43121'])

    ready_to_import = convert_to_dict(
            'name,Petya,Vasya,Masha,Vova grade,5,5,8,3 subject,math,language,physics,math year,1999,2000,1995,1998'
        )

    new_matrix = sum_matrix_columns(nums_list=[[11.9, 12.2, 12.9],
                                               [15.3, 15.1, 15.1],
                                               [16.3, 16.5, 16.5],
                                               [17.7, 17.5, 18.1]])


