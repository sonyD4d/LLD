import RegisterUserFactory

if __name__ == "__main__":
    registerUser = RegisterUserFactory.RegisterUserFactory.getRegisterUser("git")
    registerUser.register()
    registerUser.login()