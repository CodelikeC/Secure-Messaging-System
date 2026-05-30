class ConsoleUI:

    @staticmethod
    def banner():

        print(
            """
====================================
 Secure Messaging System
====================================
"""
        )

    @staticmethod
    def menu():

        print(
            """
1. Register
2. Login
3. Connect
4. Send Message
5. Exit
"""
        )

    @staticmethod
    def input_username():

        return input(
            "Username: "
        )

    @staticmethod
    def input_password():

        return input(
            "Password: "
        )

    @staticmethod
    def input_message():

        return input(
            "Message: "
        )

    @staticmethod
    def show(text):

        print(text)