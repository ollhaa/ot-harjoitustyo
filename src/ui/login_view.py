from tkinter import ttk, constants, StringVar
from services.diarys_service import diarys_service, InvalidCredentialsError

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
        self._root = root
        self._handle_show_create_user_view = handle_show_create_user_view
        self._handle_show_adding_excercise_view = handle_show_adding_excercise_view
        self._frame = None
        self._entry_username = None
        self._entry_password = None

        self._error_variable = None
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
            self._handle_show_adding_excercise_view()
        except ValueError:
            self._show_error("Invalid username or password")

        

    def _show_error(self, message):
        self._error_variable.set(message)
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
        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )
        self._initialize_heading()
        self._initialize_username_field()
        self._initialize_password_field()

        to_create_user_button = ttk.Button(
            master=self._frame,
            text="I do not have an account yet",
            command=self._handle_show_create_user_view
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
