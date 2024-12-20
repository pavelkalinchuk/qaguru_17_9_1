from dataclasses import dataclass
from typing import Dict


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    birthday: Dict[str, str]
    subject: str
    hobbies: Dict[str, bool]
    file: str
    address: str
    state: str
    city: str


student = User(
    first_name='Павел',
    last_name='Калинчук',
    email='pavel@kalinchuk.pk',
    gender='Male',
    mobile='8992367011',
    birthday={'day': '11', 'month': 'January', 'years': '2000'},
    subject='Computer Science',
    hobbies={'Sport': True, 'Reading': False, 'Music': True},
    file='test_file.png',
    address='г. Изумрудный, ул. 1-я Строителей, д.1, кв.1',
    state='Rajasthan',
    city='Jaiselmer'
)
