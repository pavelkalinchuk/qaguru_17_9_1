import os
from selene import browser, be, have, by


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
    def fill_gender(param):
        browser.element(by.text(param)).click()

    @staticmethod
    def fill_phone(param):
        browser.element('#userNumber').click().type(param)

    @staticmethod
    def fill_birthday(year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(by.text(year)).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(by.text(month)).click()
        browser.element(by.text(day)).click()

    @staticmethod
    def fill_subjects(param):
        browser.element('#subjectsInput').click().type(param)
        browser.element('#react-select-2-option-0').click()

    @staticmethod
    def scroll(param):
        browser.driver.execute_script(f"window.scrollBy(0,{param});")

    @staticmethod
    def fill_hobbies(param):
        browser.element(by.xpath(f"//label[contains(text(), '{param}')]")).click()

    @staticmethod
    def attach_file(param):
        browser.element('#uploadPicture').send_keys(os.path.abspath('resources/' + param))

    @staticmethod
    def fill_address(param):
        browser.element('#currentAddress').should(be.visible).click().send_keys(param)

    @staticmethod
    def fill_state(param):
        browser.element('#state').click().element(by.text(param)).click()

    @staticmethod
    def fill_city(param):
        browser.element('#city').click().element(by.text(param)).click()

    @staticmethod
    def submit():
        browser.element("#submit").click()

    @staticmethod
    def should_have_registered(name, email, gender, phone, birthday, subjects, hobbies, file, address,
                               state_city):
        browser.element('.table').all('td').even.should(have.exact_texts(name, email, gender, phone, birthday,
                                                                         subjects, hobbies, file, address, state_city))
        browser.element('.modal-footer').click()
