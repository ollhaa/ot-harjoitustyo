from tkinter import ttk, constants, StringVar, Toplevel, IntVar, Radiobutton
from services.diarys_service import diarys_service, UsernameExistsError
from datetime import datetime

class EditView:

    def __init__(self, root, handle_logout ,handle_show_adding_excercise_view, handle_analytics_view):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_show_adding_excercise_view = handle_show_adding_excercise_view
        self._handle_analytics_view = handle_analytics_view
        
        
        
        self._initialize()

    def pack(self):
        # if self.frame is not None:
        self._frame.pack(fill=constants.X)

    def destroy(self):
        # if self.frame is not None:
        self._frame.destroy()

    def _logout_handler(self):
        diarys_service.logout()
        self._handle_logout()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_logout_button()
        self._initialize_help_button()
        #self._initialize_adding_exercise_view_button()
        #self._initialize_options()

        #self._initialize_other()
    
    def _initialize_logout_button(self):
        logout_button = ttk.Button(
            master=self._frame,
            text="LOGOUT?",
            #bg ="red",
            command = self._logout_handler
        )

        logout_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky=constants.EW
        )



    def _initialize_summary_view_button(self):
        summary_view_button = ttk.Button(
            master=self._frame,
            text="ANALYTICS?",
            #background ='#A877BA'
            #command = lambda:self._analytics_handler()
        )

        summary_view_button.grid(
            row=0,
            column=5,
            padx=10,
            pady=10,
            columnspan =3,
            sticky=constants.EW
        )
    
    def _initialize_help_button(self):
        help_button = ttk.Button(
            master=self._frame,
            text="HELP?",
            command= lambda:self._open_popup()
            #background ='#A877BA'
        )

        help_button.grid(
            row=0,
            column=12,
            padx=10,
            pady=10,
            columnspan =3,
            sticky=constants.EW
        )
