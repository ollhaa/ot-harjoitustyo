from tkinter import ttk, constants, StringVar
from services.diarys_service import diarys_service, UsernameExistsError


class CreateUserView:

    def __init__(self, root, handle_show_login_view, handle_analytics_view):
        self._root = root
        #self.handle_create_user = handle_create_user
        self._handle_show_login_view = handle_show_login_view
        self._handle_analytics_view = handle_analytics_view
        self._frame = None
        self._entry_username = None
        self._entry_password = None
        self._second_password = None
        self._error_variable = None
        self._error_label = None

        self._initialize()

    def pack(self):
        # if self.frame is not None:
        self._frame.pack(fill=constants.X)

    def destroy(self):
        # if self.frame is not None:
        self._frame.destroy()

    def _create_user_handler(self):
        username = self._entry_username.get()
        password = self._entry_password.get()
        second_password = self._second_password.get()

        if len(username) == 0 or len(username) > 12:
            self._show_error("Length of username must be 1-12")
        elif len(password) > 12 or len(password) <4:
            self._show_error("Length of password must be 4-12")
        elif password != second_password:
            self._show_error("Passwords are not same!")
        else:
            try:   
                diarys_service.create_user(username, password)
                self._handle_show_login_view()
            except ValueError:
                self._show_error("Username is not allowed")

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid(row=9, column=0, columnspan =2,  padx=0, pady=5, sticky = constants.W)

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_password_fields(self):
        password_label = ttk.Label(
            master=self._frame, text="Your new password:")
        self._entry_password = ttk.Entry(master=self._frame, show="*")
        password_label.grid(row= 3, column =0,padx=0, pady=5)
        self._entry_password.grid(row= 4, column =0,padx=5, pady=5)

        second_password_label = ttk.Label(
            master=self._frame, text="Again your new password:")
        self._second_password = ttk.Entry(master=self._frame, show="*")
        second_password_label.grid(row= 5, column =0,padx=0, pady=5)
        self._second_password.grid(padx=6, pady=5)

    def _initialize_username_field(self):
        username_label = ttk.Label(
            master=self._frame, text="Your new username:")
        self._entry_username = ttk.Entry(master=self._frame)
        username_label.grid(row= 1, column =0, padx=0, pady=5)
        self._entry_username.grid(row= 2, column =0,padx=5, pady=5)

    def _initialize_heading(self):
        heading_label = ttk.Label(master=self._frame, text="CREATE A NEW USER")
        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid_columnconfigure(2, weight=1)
        self._frame.configure(padding=15)

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._initialize_heading()
        self._initialize_username_field()
        self._initialize_password_fields()

        create_button = ttk.Button(
            master=self._frame,
            text="Register",
            command=self._create_user_handler
        )

        login_view_button = ttk.Button(
            master=self._frame,
            text="I already have an account",
            command=self._handle_show_login_view
        )

        create_button.grid(row= 7, column =0,padx=5, pady=5, sticky=constants.EW)

        login_view_button.grid(row= 8, column =0,padx=5, pady=5, sticky=constants.EW)
 
