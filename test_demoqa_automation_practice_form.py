from demoqa_tests.registration_page import RegistrationPage


def test_practice_form():
    registration_page = RegistrationPage()

    registration_page.fill_first_name('Pavel')
    registration_page.fill_last_name('Kalinchuk')
    registration_page.fill_email('pavelkalinchuk@mail.tst')
    registration_page.fill_gender('Male')
    registration_page.fill_phone('8992367011')
    registration_page.fill_birthday("2000", 'January', '11')
    registration_page.fill_subjects('computer')
    registration_page.scroll()
    registration_page.fill_hobbies('Sports')
    registration_page.attach_file('test_file.png')
    registration_page.fill_address("г. Москва, ул. 1-я Строителей, д.1, кв.1")
    registration_page.scroll()
    registration_page.fill_state('Rajasthan')
    registration_page.fill_city('Jaiselmer')
    registration_page.scroll()
    registration_page.submit()
    registration_page.should_have_registered(
        'Pavel Kalinchuk',
        'pavelkalinchuk@mail.tst',
        'Male',
        '8992367011',
        '11 January,2000',
        'Computer Science',
        'Sports',
        'test_file.png',
        'г. Москва, ул. 1-я Строителей, д.1, кв.1',
        'Rajasthan Jaiselmer'
    )


