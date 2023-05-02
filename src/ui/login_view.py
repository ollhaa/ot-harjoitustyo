from tkinter import ttk, constants


class LoginView:
    """Käyttäjän kirjautumisnäkymä."""
    def __init__(self, root, handle_show_create_user_view, handle_show_adding_excercise_view):
        """Luokan konstruktori. Luo uuden kirjautumisnäkymän.
        Args:
            root:
                TKinter, jonka sisään näkymä alustetaan.
            handle_show_create_user_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään rekisteröitymisnäkymään.
            handle_show_adding_exercise_view:
                Kutsuttava-arvo, jota kutsutaan kun siirrytään harjoituksenlisäämisnäkymään.
        """
        self.root = root
        self.handle_show_create_user_view = handle_show_create_user_view
        self.handle_show_adding_excercise_view = handle_show_adding_excercise_view
        self.frame = None
        self.entry_username = None
        self.entry_password = None

        self.initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self.frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän"""
        self.frame.destroy()

    def login_handler(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        self.handle_show_adding_excercise_view()

    def initialize_password_field(self):
        password_label = ttk.Label(
            master=self.frame, text="Enter your password:")
        self.entry_password = ttk.Entry(master=self.frame, show="*")
        password_label.grid(padx=0, pady=5)
        self.entry_password.grid(padx=5, pady=5)

    def initialize_username_field(self):
        username_label = ttk.Label(
            master=self.frame, text="Enter your username:")
        self.entry_username = ttk.Entry(master=self.frame)
        username_label.grid(padx=10, pady=10)
        self.entry_username.grid(padx=10, pady=10)

    def initialize_heading(self):
        heading_label = ttk.Label(master=self.frame, text="LOG IN")
        heading_label.grid(row=0, column=0, columnspan=1, sticky=constants.EW)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.initialize_heading()
        self.initialize_username_field()
        self.initialize_password_field()

        to_create_user_button = ttk.Button(
            master=self.frame,
            text="I do not have an account yet",
            command=self.handle_show_create_user_view
        )

        login_button = ttk.Button(
            master=self.frame,
            text="Log In",
            command=self.login_handler
        )

        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        to_create_user_button.grid(padx=5, pady=5, sticky=constants.EW)
