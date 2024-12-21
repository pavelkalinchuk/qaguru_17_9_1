from dataclasses import dataclass
from typing import Dict
from enum import Enum


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'


class Subjects(Enum):
    MATHS = 'Maths'
    COMPUTER_SCIENCE = 'Computer Science'
    SOCIAL_STUDIES = 'Social Studies'


class Hobbies(Enum):
    SPORT = 'Sports'
    READING = 'Reading'
    MUSIC = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile: str
    date_of_birth: Dict[str, str]
    subjects: Subjects
    hobbies: Hobbies
    picture: str
    current_address: str
    state: str
    city: str


student = User(
    first_name='Павел',
    last_name='Калинчук',
    email='pavel@kalinchuk.pk',
    gender=Gender.MALE,
    mobile='8992367011',
    date_of_birth={'day': '11', 'month': 'January', 'years': '2000'},
    subjects=Subjects.COMPUTER_SCIENCE,
    hobbies=Hobbies.SPORT,
    picture='test_file.png',
    current_address='г. Изумрудный, ул. 1-я Строителей, д.1, кв.1',
    state='Rajasthan',
    city='Jaiselmer'
)
