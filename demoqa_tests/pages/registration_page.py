import os
from selene import browser, be, have, by
from demoqa_tests.data.user import User


class RegistrationPage:

    @staticmethod
    def filling_registration_form(value: User):
        browser.element('#firstName').click().type(value.first_name)
        browser.element('#lastName').click().type(value.last_name)
        browser.element('#userEmail').click().type(value.email)
        browser.element(by.text(value.gender)).click()
        browser.element('#userNumber').click().type(value.mobile)
        browser.element('#dateOfBirthInput').click()
        year = value.birthday.get('years')
        if year:
            browser.element('.react-datepicker__year-select').click()
            browser.element(by.text(year)).click()
        month = value.birthday.get('month')
        if month:
            browser.element('.react-datepicker__month-select').click()
            browser.element(by.text(month)).click()
        browser.element(by.text(value.birthday.get('day'))).click()
        browser.element('#subjectsInput').click().type(value.subject)
        browser.element('#react-select-2-option-0').click()
        browser.driver.execute_script("window.scrollBy(0,400)", "")
        if value.hobbies.get('Sport'):
            browser.element('label[for="hobbies-checkbox-1"]').click()
        if value.hobbies.get('Reading'):
            browser.element('label[for="hobbies-checkbox-2"]').click()
        if value.hobbies.get('Music'):
            browser.element('label[for="hobbies-checkbox-3"]').click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(value.file))
        browser.element('#currentAddress').should(be.visible).click().send_keys(value.address)
        browser.driver.execute_script("window.scrollBy(0,400)", "")
        browser.element('#state').click().element(by.text(value.state)).click()
        browser.element('#city').click().element(by.text(value.city)).click()
        browser.driver.execute_script("window.scrollBy(0,400)", "")
        browser.element("#submit").click()

    @staticmethod
    def should_registration_form():
        browser.element('.table').all('td').even.should(have.exact_texts(
            'Павел Калинчук',
            'pavel@kalinchuk.pk',
            'Male',
            '8992367011',
            '11 January,2000',
            'Computer Science',
            'Sports, Music',
            'test_file.png',
            'г. Изумрудный, ул. 1-я Строителей, д.1, кв.1',
            'Rajasthan Jaiselmer'
        ))
        browser.element('.modal-footer').click()