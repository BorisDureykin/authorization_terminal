import re
from database.sqlite import *


# функция ввода
def inputEmptyString(invite):
    return input(invite)


# проверка наличия введенного значения в БД
def isUserInDb(variable, inputString):
    records = getUser(variable, inputString)
    for user in records:
        if user[1] == inputString or user[3] == inputString:
            return records
        return False


# Ввод значения по приглашению (invite) + проверка введенного значения(choice) с передаваемым набором допустимых
# значений (whichCheck) и возврат (choice)
def checkingCorrectnessSelection(whichCheck, invite):
    while True:
        choice = inputEmptyString(invite)
        if choice not in whichCheck:
            print(f'\nChoice is not valid!')
            choice = ''
            continue
        break
    return choice


# ввод и проверка введенного значения "login" на валидность ввода и на отсутствие в БД
def loginVerification(promptString):
    while True:
        login = inputEmptyString(promptString)

        if re.match("[a-zA-Z0-9а-яА-Я]+", login) is None:
            print(f'\nLogin is not valid')
            continue

        if isUserInDb('login', login):
            print(f'\nUser {login} already is is exists. Try again.')
            continue
        return login


# ввод и проверка введенного значения "password" на валидность ввода
def passwordVerification(promptString):
    while True:
        password = inputEmptyString(promptString)

        if re.match("[a-zA-Z0-9а-яА-Я]{6}", password) is None:
            print(f'\nPassword is not valid')
            continue
        return password


# ввод и проверка введенного значения "email" на валидность ввода и на отсутствие в БД
def emailVerification(promptString):
    while True:
        email = inputEmptyString(promptString)

        if re.fullmatch("[a-zA-Z0-9]+[-]?[a-zA-Z0-9]+[.]?[a-zA-Z0-9]+[@]{1}[a-zA-Z0-9]+[-]?["
                        "a-zA-Z0-9]+[.]{1}[a-zA-Z]{2,4}", email) is None:
            print('\nE-Mail is not valid')
            continue

        if isUserInDb('eMail', email):
            print(f'\nE-Mail {email} already is is exists. Try again.')
            continue
        return email


# Проверка user на правильность ввода login или email и пароля при авторизации, возвращает введенный login.
def authorizationVerification(variable, promptString):
    while True:
        inputString = inputEmptyString(f'{promptString} ')
        password = inputEmptyString('Enter password: ')
        records = isUserInDb(variable, inputString)

        if records is None:
            print(f'\nThe user with such {variable} or password is not in the system. Try again.')
            continue

        for user in records:
            if user[2] != password:
                print(f'\nThe user with such {variable} or password is not in the system. Try again.')
                continue
            login = user[1]
            return login
        continue
