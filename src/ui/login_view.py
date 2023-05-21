from tkinter import ttk, constants, StringVar
from services.diarys_service import diarys_service

class LoginView:
    """Käyttäjän kirjautumisnäkymä."""
    def __init__(self, root, to_create_view, to_adding_view):
        self._root = root
        self._to_create_view = to_create_view
        self._to_adding_view = to_adding_view
        self._frame = None
        self._entry_username = None
        self._entry_password = None
        self._error_message = None
        self._error_label = None
        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän"""
        self._frame.destroy()

    def _login_handler(self):
        username = self._entry_username.get()
        password = self._entry_password.get()

        try:
            diarys_service.login(username, password)
            self._to_adding_view()
        except ValueError:
            self._show_error("Invalid username or password")

    def _show_error(self, message):
        self._error_message.set(message)
        self._error_label.grid(row=8, column=0, columnspan=2)

    def _hide_error(self):
        self._error_label.grid_remove()

    def _initialize_password_field(self):
        password_label = ttk.Label(
            master=self._frame, text="Enter your password:")
        self._entry_password = ttk.Entry(master=self._frame, show="*")
        password_label.grid(padx=0, pady=5)
        self._entry_password.grid(padx=5, pady=5)

    def _initialize_username_field(self):
        username_label = ttk.Label(
            master=self._frame, text="Enter your username:")
        self._entry_username = ttk.Entry(master=self._frame)
        username_label.grid(padx=10, pady=10)
        self._entry_username.grid(padx=10, pady=10)

    def _initialize_heading(self):
        heading_label = ttk.Label(master=self._frame, text="LOG IN")
        heading_label.grid(row=0, column=0, columnspan=1, sticky=constants.EW)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)
        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="red"
        )
        self._initialize_heading()
        self._initialize_username_field()
        self._initialize_password_field()

        to_create_user_button = ttk.Button(
            master=self._frame,
            text="I do not have an account yet",
            command=self._to_create_view
        )

        login_button = ttk.Button(
            master=self._frame,
            text="Log In",
            command=self._login_handler
        )

        self._error_label.grid(padx=5, pady=5)
        login_button.grid(padx=5, pady=5, sticky=constants.EW)

        to_create_user_button.grid(padx=5, pady=5, sticky=constants.EW)

        self._hide_error()
