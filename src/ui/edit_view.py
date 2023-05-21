from tkinter import ttk, constants, StringVar, Toplevel, IntVar, Radiobutton
from services.diarys_service import diarys_service
from datetime import datetime
import pandas as pd

class EditView:

    def __init__(self, root, to_login_view ,to_adding_view, to_analytics_view):
        self._root = root
        self._frame = None
        self._to_login_view = to_login_view
        self._to_adding_view = to_adding_view
        self._to_analytics_view = to_analytics_view
        self._exercices = None
        self._radio_var =1
        self._radio_var_delete = None
        self._error_variable = None
        self._error_label = None
        self._initialize()

    def pack(self):
        """"Näyttää näkymän."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """"Tuhoaa näkymän."""
        self._frame.destroy()
        
    def _logout_handler(self):
        diarys_service.logout()
        self._to_login_view()

    def _show_error(self, message):
        self._error_variable.set(message)
        self._error_label.grid()

    def _hide_error(self):
        self._error_label.grid_remove()

    def _data_summary(self):
        try:
            self._exercices = pd.DataFrame(diarys_service.find_all_routines())
            column_names = ["Id","Username", "Date", "Exercise", "Sets", "Reps", "Kilos"]
            self._exercices.columns = column_names
            self._exercices.drop(["Username"], axis=1, inplace=True)
            radio_var = self._radio_var.get()
            if radio_var ==1 and self._exercices.shape[0] >=10:
                self._exercices =self._exercices.iloc[-10:]
                self._initialize_other()
            elif radio_var ==1 and self._exercices.shape[0] >=2:
                rows = self._exercices.shape[0]
                self._exercices =self._exercices.iloc[-rows:]
                self._initialize_other()
            elif radio_var ==2 and self._exercices.shape[0] >=10:
                self._initialize_other()
            elif radio_var ==2 and self._exercices.shape[0] >=2:
                rows = self._exercices.shape[0]
                self._exercices =self._exercices.iloc[-rows:]
                self._initialize_other()
            else: 
                self._show_error("Add more!")
        except ValueError:
            self._show_error("No added!")

    def _delete(self):
        id_del = self._radio_var_delete.get()
        diarys_service.delete_routine_by_id(id_del)
        self._to_adding_view()     

    def _open_popup(self):
        top= Toplevel(self._frame)
        top.geometry("585x120")
        top.resizable(0, 0)
        top.title("Help: Edit exercise")
        ttk.Label(top, text=
        "Select one of the following:\n"
            "\t*Last 10 \n"
        "\n"
        "Then press 'Find'. You can delete routines by selecting the routine then pressing 'Delete'. \n"
        "You can also go Analytics view ('ANALYTICS?) or to other frames.\n"
        "If you want to logout then press 'LOGOUT?" 
        ).place(x=0,y=0)


    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_logout_button()
        self._initialize_help_button()
        self._initialize_adding_exercise_view_button()
        self._initialize_summary_view_button()
        self._initialize_options()

        self._error_variable = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_variable,
            foreground="red"
        )

        self._error_label.grid(padx=5, pady=5)

        self._hide_error()
    
    def _initialize_logout_button(self):
        logout_button = ttk.Button(
            master=self._frame,
            text="LOGOUT?",
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
            command = self._to_analytics_view
        )

        summary_view_button.grid(
            row=0,
            column=4,
            padx=10,
            pady=10,
            columnspan =2,
            sticky=constants.EW
        )

    def _initialize_adding_exercise_view_button(self):
        analytics_view_button = ttk.Button(
            master=self._frame,
            text="ADD?",
            command = self._to_adding_view
        )

        analytics_view_button.grid(
            row=0,
            column=2,
            columnspan=2,
            padx=10,
            pady=10,
            sticky=constants.EW
        )
        
    
    def _initialize_help_button(self):
        help_button = ttk.Button(
            master=self._frame,
            text="HELP?",
            command= lambda:self._open_popup()
        )

        help_button.grid(
            row=0,
            column=6,
            padx=10,
            pady=10,
            columnspan =2,
            sticky=constants.EW
        )
    
    def _initialize_options(self):
        days = ttk.Label(master = self._frame, text = "Select:")
        days.grid(row= 1, column =0, pady=10)

        options = [('Last 10', 1)]
        self._radio_var = IntVar()
        i =0
        for text, value in options:
            Radiobutton(master=self._frame, text=text, value=value, variable=self._radio_var).grid(row=1, column=2+i, padx=10, pady=10, sticky = constants.W)
            i+=1
        
        self._radio_var.set(1)

        bar_chart_button =ttk.Button(
            master= self._frame,
            text="Find",
            command = lambda: self._data_summary()
        )
        bar_chart_button.grid(
            row= 1,
            column =6,
            pady =10,
            sticky = constants.EW
        )

        id_label = ttk.Label(master = self._frame, text = "ID:")
        date_label = ttk.Label(master = self._frame, text = "DATE:")
        exercise_label = ttk.Label(master = self._frame, text = "EXERCISE")
        sets_label = ttk.Label(master = self._frame, text = "SETS:")
        reps_label = ttk.Label(master = self._frame, text = "REPS:")
        kilos_label = ttk.Label(master = self._frame, text = "KILOS:")
        delete_label = ttk.Label(master = self._frame, text = "SELECT:")

        id_label.grid(row=2, column=0)
        date_label.grid(row=2, column=1)
        exercise_label.grid(row=2, column=2)
        sets_label.grid(row=2, column=3)
        reps_label.grid(row=2, column=4)
        kilos_label.grid(row=2, column=5)
        delete_label.grid(row=2, column=6)

    def _initialize_other(self):
        self._radio_var_delete = IntVar()
        rows = self._exercices.shape[0]
        for x in range(rows):
            for y in range(6):
                fact = self._exercices.iloc[x,y]
                detail = ttk.Label(master=self._frame, text=str(fact))
                detail.grid(row=3+x, column=y)
            Radiobutton(master=self._frame, value = self._exercices.iloc[x,0], variable=self._radio_var_delete).grid(row=3+x, column=6, padx=5, pady=5)
        ttk.Button(master=self._frame, text="Delete", command=lambda: self._delete()).grid(row=rows+3, column=6, padx=5, pady=5)
