class ContactDirectory:

    def __init__(self):

        self.contacts = {}

    def add_contact(
        self,
        username,
        public_key
    ):

        self.contacts[username] = (
            public_key
        )

    def get_public_key(
        self,
        username
    ):

        return self.contacts.get(
            username
        )

    def exists(
        self,
        username
    ):

        return username in self.contacts