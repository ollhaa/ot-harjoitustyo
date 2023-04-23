from tkinter import ttk, constants, StringVar
from services.diarys_service import diarys_service, UsernameExistsError


class CreateUserView:

    def __init__(self, root, handle_show_login_view):
        self.root = root
        #self.handle_create_user = handle_create_user
        self.handle_show_login_view = handle_show_login_view
        self.frame = None
        self.entry_username = None
        self.entry_password = None
        self.second_password = None

        self.initialize()

    def pack(self):
        # if self.frame is not None:
        self.frame.pack(fill=constants.X)

    def destroy(self):
        # if self.frame is not None:
        self.frame.destroy()

    def create_user_handler(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        second_password = self.second_password.get()

        diarys_service.create_user(username, password)
        # self.handle_create_user()

    def initialize_password_fields(self):
        password_label = ttk.Label(
            master=self.frame, text="Your new password:")
        self.entry_password = ttk.Entry(master=self.frame, show="*")
        password_label.grid(padx=0, pady=5)
        self.entry_password.grid(padx=5, pady=5)

        second_password_label = ttk.Label(
            master=self.frame, text="Again your new password:")
        self.second_password = ttk.Entry(master=self.frame, show="*")
        second_password_label.grid(padx=0, pady=5)
        self.second_password.grid(padx=5, pady=5)

    def initialize_username_field(self):
        username_label = ttk.Label(
            master=self.frame, text="Your new username:")
        self.entry_username = ttk.Entry(master=self.frame)
        username_label.grid(padx=0, pady=5)
        self.entry_username.grid(padx=5, pady=5)

    def initialize_heading(self):
        heading_label = ttk.Label(master=self.frame, text="CREATE A NEW USER")
        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        self.initialize_heading()
        self.initialize_username_field()
        self.initialize_password_fields()

        create_button = ttk.Button(
            master=self.frame,
            text="Register",
            command=self.create_user_handler
        )

        login_view_button = ttk.Button(
            master=self.frame,
            text="I already have an account",
            command=self.handle_show_login_view
        )

        create_button.grid(padx=5, pady=5, sticky=constants.EW)

        login_view_button.grid(padx=5, pady=5, sticky=constants.EW)
