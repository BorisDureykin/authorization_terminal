from action.checks import *
from database.sqlite import *


# выбор регистрация, авторизация выход и создание базы
def chooseAction():
    choice = checkingCorrectnessSelection({'L', 'l', 'R', 'r', 'Q', 'q', 'DB'},
                                          f'\nHi! Please enter \n"L" - Log in,\n"R" - Register,\n"Q"- Quit\n"DB"- '
                                          f'ClearDatabase: ')

    if choice in {'L', 'l'}:
        authorization()

    if choice in {'R', 'r'}:
        registration()

    if choice in {'DB'}:
        clearDatabase()
    users = getUserAll()
    print(users)
    exit()


# Регистрация user и вывод на экран сообщения об успешной регистрации и учетных данных
def registration():
    login = loginVerification("Please enter Login: ")
    password = passwordVerification("Please enter Password: ")
    email = emailVerification("Please enter E-Mail: ")
    userData = {'login': login, 'password': password, 'eMail': email}
    print(f'\nCongratulations {login}, you have registered,\nyour registration details: {userData}')
    putUser(userData)
    chooseAction()


# авторизация, выбор авторизации по логину или eMail, возвращает login
def authorization():
    choice = checkingCorrectnessSelection({'L', 'l', 'E', 'e'},
                                          f'\nRegistration selection, '
                                          f'\nenter "L" - by login,'
                                          f'\nenter "E" - by email: ')
    login = ''
    if choice in {'L', 'l'}:
        login = authorizationVerification('login', 'Enter your login: ')

    if choice in {'E', 'e'}:
        login = authorizationVerification('eMail', 'Enter your eMail: ')
    changeSelection(login)


# Предложение об изменении учетных данных,
# при согласии на изменение выбор:куда вносить изменения(login,password,email)
def changeSelection(login):
    choiceY = inputEmptyString(f"\nHi {login}! Do you want to change your account details?\nPlease enter 'Y' to change"
                               f"\notherwise exit: ")
    if choiceY in {'Y', 'y'}:
        print(f'{login} what do you want to change? ')
        choice = checkingCorrectnessSelection({'L', 'l', 'P', 'p', 'E', 'e'},
                                              "\nMake a choice: \n'L' - login,\n'P' - password,\n'E' - email: ")

        if choice in {'L', 'l'}:
            changeUser(login, 'login')

        if choice in {'P', 'p'}:
            changeUser(login, 'password')

        changeUser(login, 'email')

    chooseAction()


# изменение учетных данных и внесение изменений в БД и вывод новых учетных данных
def changeUser(login, variable):
    if variable == 'login':
        values = loginVerification('Please enter New login: ')

    if variable == 'password':
        values = passwordVerification('Please enter New password: ')

    if variable == 'email':
        values = emailVerification('Please enter New E-Mail: ')

    updateUser(login, variable, values)
    print(f'Your new credentials: {values}')
    chooseAction()
