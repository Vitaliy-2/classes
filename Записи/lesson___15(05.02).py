from typing import List
from typing import Dict
from typing import Union
# some_int: str = 5
# some_list: List = [1, 2, 3]

# print(some_list)

# TODO Практика
person_dict: Dict[str, Union[str, int, list[str]]] = {
    'name': 'Сергей',
    'age': 35,
    'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
}
person_list: List[Dict[str, Union[str, int, list[str]]]] = [{
    'name': 'Сергей',
    'age': 35,
    'skills': ['JS', 'Python', 'C++', 'C#', 'Java']
}]

