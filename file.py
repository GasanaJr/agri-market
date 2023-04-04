import signUp
import login


def main_file():
    start = int(input('''
    Welcome to the Market Place
    Enter 1 for Signup
    Enter 2 for Login
**************************************************************
'''))
    if (start == 1):
        signUp.signUp()
    else:
        login.login()
