import os
from selene import browser, be, have, by
from demoqa_tests.data.user import User


class RegistrationPage:

    @staticmethod
    def filling_registration_form(user: User):
        browser.element('#firstName').click().type(user.first_name)
        browser.element('#lastName').click().type(user.last_name)
        browser.element('#userEmail').click().type(user.email)
        browser.element(by.text(user.gender.value)).click()
        browser.element('#userNumber').click().type(user.mobile)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(by.text(str(user.date_of_birth.year))).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(by.text(user.date_of_birth.strftime('%B'))).click()
        browser.element(by.text(str(user.date_of_birth.day))).click()
        browser.element('#subjectsInput').click().type(user.subjects.value)
        browser.element('#react-select-2-option-0').click()
        browser.driver.execute_script("window.scrollBy(0,400)", "")
        browser.element(by.xpath(f"//label[contains(text(), '{user.hobbies.value}')]")).click()
        browser.element('#uploadPicture').send_keys(os.path.abspath(user.picture))
        browser.element('#currentAddress').should(be.visible).click().send_keys(user.current_address)
        browser.driver.execute_script("window.scrollBy(0,400)", "")
        browser.element('#state').click().element(by.text(user.state)).click()
        browser.element('#city').click().element(by.text(user.city)).click()
        browser.driver.execute_script("window.scrollBy(0,400)", "")
        browser.element("#submit").click()

    @staticmethod
    def should_registration_form(user: User):
        full_name = f'{user.first_name} {user.last_name}'
        email = user.email
        gender = user.gender.value
        mobile = user.mobile
        date_of_birth = f'{user.date_of_birth.day} {user.date_of_birth.strftime("%B")},{user.date_of_birth.year}'
        subjects = user.subjects.value
        hobbies = user.hobbies.value
        picture = user.picture
        current_address = user.current_address
        state_and_city = f'{user.state} {user.city}'

        browser.element('.table').all('td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            current_address,
            state_and_city
        ))
        browser.element('.modal-footer').click()
