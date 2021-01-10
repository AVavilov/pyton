# Создать список и заполнить его элементами различных типов данных

list = (1, 1.1, 'Text', True, False, {1, 1.1, 'Text'}, [2, 2.1, 'Text'], None, set(), frozenset())
for enum, list_type in enumerate(list, 1):
    print(f'{str(enum)}: {str(list_type):} - {type(str(list_type))}')