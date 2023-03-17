class User:
    """User."""

    def __init__(
        self,
        login: str,
        password: str,
        first_name: str
    ) -> None:
        self.login = login
        self.password = password
        self.first_name = first_name
    
    @staticmethod
    def create(
        login: str,
        password: str,
        password2: str,
        first_name: str,
        users: list['User']
    ) -> 'User':
        user: User = User(
            login=login,
            password=password,
            first_name=first_name
        )
        print(users)
        if len(password) < 4:
            raise ValueError(
                "Password is too short"
            )
        if password != password2:
            raise ValueError(
                "Password confirm is not correct"
            )
        user.login_valid(users=users)
        return user
    
    def login_valid(self, users: list['User']) -> bool:
        if users == []:
            return True
        for user in users:
            if user.login == self.login:
                raise ValueError(
                    "Login is not unique"
                ) 
        return True
    
    @staticmethod
    def check_auth(
        login: str,
        password: str,
        users_data: list['User']
    ) -> 'User':
        checker: int = 0
        his_acc: 'User' = None
        for user in users_data:
            if user.login == login:
                checker = 1
                his_acc = user
        if checker != 1:
            raise ValueError(
                "Login doesn't exist"
            )
        else:
            if his_acc.password == password:
                return his_acc
            else:
                raise ValueError(
                    "Password is not correct"
                )
        
