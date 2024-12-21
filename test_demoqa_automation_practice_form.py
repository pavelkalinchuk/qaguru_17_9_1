from demoqa_tests.data.user import student
from demoqa_tests.pages.registration_page import RegistrationPage


def test_practice_form():
    registration_form = RegistrationPage()

    registration_form.filling_registration_form(student)
    registration_form.should_registration_form(student)
