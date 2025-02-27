class RegisterUserFactory:
    def __init__(self):
        pass
    
    @staticmethod
    def getRegisterUser(type):
        if type == "google":
            from RegisterUser.RegisterUserByGoogle import RegisterUserByGoogle
            return RegisterUserByGoogle()
        elif type == "git":
            from RegisterUser.RegisterUserByGit import RegisterUserByGit
            return RegisterUserByGit()
        else:
            return None