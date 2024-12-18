import os
from selene import browser, be, have


class RegistrationPage:

    @staticmethod
    def fill_first_name(param):
        browser.element('[id="firstName"]').click().type(param)

    @staticmethod
    def fill_last_name(param):
        browser.element('[id="lastName"]').click().type(param)

    @staticmethod
    def fill_email(param):
        browser.element('[id="userEmail"]').click().type(param)

    @staticmethod
    def fill_gender():
        browser.element('label[for="gender-radio-1"]').click()

    @staticmethod
    def fill_phone(param):
        browser.element('#userNumber').click().type(param)

    @staticmethod
    def fill_birthday():
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker-popper').should(be.visible)
        browser.element('.react-datepicker__month-select').should(be.visible).element('[value="0"]').click()
        browser.element('.react-datepicker__year-select').should(be.visible).element('[value="2000"]').click()
        browser.element('.react-datepicker__week').should(be.visible).element('.react-datepicker__day.react'
                                                                              '-datepicker__day--001').click()

    @staticmethod
    def fill_subjects(param):
        browser.element('#subjectsInput').click().type(param)
        browser.element('#react-select-2-option-0').click()

    @staticmethod
    def scroll():
        browser.driver.execute_script("window.scrollBy(0,400)", "")

    @staticmethod
    def fill_hobbies():
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-3"]').click()

    @staticmethod
    def attach_file(param):
        browser.element('#uploadPicture').send_keys(os.path.abspath('resources/' + param))

    @staticmethod
    def fill_address(param):
        browser.element('#currentAddress').should(be.visible).click().send_keys(param)

    @staticmethod
    def fill_state():
        browser.element('#state').should(be.visible).click().element('#react-select-3-option-3').click()

    @staticmethod
    def fill_city():
        browser.element('#city').should(be.visible).click().element('#react-select-4-option-1').click()

    @staticmethod
    def submit():
        browser.element("#submit").click()

    @staticmethod
    def should_have_registered(name, email, gender, phone, birthday, subjects, hobbies, file, address,
                               state_city):
        browser.element('.table').all('td').even.should(have.exact_texts(name, email, gender, phone, birthday,
                                                                         subjects, hobbies, file, address, state_city))
        browser.element('.modal-footer').click()
