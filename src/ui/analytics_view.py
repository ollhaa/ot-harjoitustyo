from tkinter import ttk, constants, StringVar, Toplevel, IntVar, Radiobutton
from services.diarys_service import diarys_service#, UsernameExistsError
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class AnalyticsView:

    def __init__(self, root, to_login_view, to_adding_view, to_edit_view):
        self._root = root
        self._frame = None
        self._to_login_view = to_login_view
        self._to_adding_view = to_adding_view
        self._to_edit_view = to_edit_view
        self._radio_var = 1
        self._summary_days =0
        self._summary_exercises =0
        self._summary_total =0
        self._error_message = None
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
        self._error_message.set(message)
        self._error_label.grid(row=8, column=0, columnspan=2)

    def _hide_error(self):
        self._error_label.grid_remove()

    def _clean_data_summary(self):
        self._hide_error()
        try:
            routines = pd.DataFrame(diarys_service.find_all_routines())
            column_names = ["Id","Username", "Date", "Exercise", "Sets", "Reps", "Kilos"]
            routines.columns = column_names
            routines.drop(["Username"], axis=1, inplace=True)
            routines = routines.assign(Total = lambda x: x.Sets * x.Reps * x.Kilos)
            
            routines["Year"] = routines.Date.str[:4]
            routines["Month"] = routines.Date.str[6:7]

            cur_day= datetime.today().date()
            cur_month = cur_day.month
            cur_year = cur_day.year

            radio_var = self._radio_var.get()

            if radio_var ==1:
                routines_summary = routines[routines["Date"] == str(cur_day)]
            elif radio_var ==2:
                routines_summary = routines[routines["Month"] == str(cur_month)]
                routines_summary = routines_summary[routines_summary["Year"] == str(cur_year)]
            elif radio_var == 3:
                routines_summary = routines[routines["Year"] == str(cur_year)]
            else:
                routines_summary = routines.copy()

            self._summary_days = len(routines_summary.Date.unique())
            self._summary_exercises = len(routines_summary.Exercise.unique())
            self._summary_total = routines_summary.Total.sum()

            labels = routines_summary.Exercise.unique().tolist()
            sizes = routines_summary.groupby(['Exercise']).sum()
            sizes = sizes.Total.tolist()

            figure = plt.Figure(figsize=(3,3), dpi=100)
            plt.pie(sizes, labels=labels)
            
            self._initialize_other()
            plt.show()

        except ValueError:
            self._show_error("Did u add any?")
            
        except IndexError:
            self._show_error("Did u add any?")
            
    def _open_popup(self):
        top= Toplevel(self._frame)
        top.geometry("550x155")
        top.resizable(0, 0)
        top.title("Help: See stats")
        ttk.Label(top, text= 
        "Select from leftside one of the following:\n"
            "\t*Today \n"
            "\t*This Month \n"
            "\t*This Year \n"
            "\t*All \n"
        "\n"
        "Then press 'Get stats'. You can also go Adding exercices ('ADD?) or to other frames. \n"
        "\n"
        "If you want to logout then press 'LOGOUT?" 
        ).place(x=0,y=0)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._error_message = StringVar(self._frame)
        self._error_label = ttk.Label(
            master=self._frame,
            textvariable=self._error_message,
            foreground="red"
        )
        self._initialize_logout_button()
        self._initialize_edit_view_button()
        self._initialize_help_button()
        self._initialize_adding_exercise_view_button()
        self._initialize_options()
        self._initialize_other()
        
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

    def _initialize_edit_view_button(self):
        edit_view_button = ttk.Button(
            master=self._frame,
            text="EDIT?",
            #bg ="red"
            command=self._to_edit_view
        )

        edit_view_button.grid(
            row=0,
            column=6,
            padx=10,
            pady=10,
            columnspan =3,
            sticky=constants.EW
        )

    def _initialize_adding_exercise_view_button(self):
        summary_view_button = ttk.Button(
            master=self._frame,
            text="ADD?",
            command = self._to_adding_view
        )

        summary_view_button.grid(
            row=0,
            column=3,
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
            column=9,
            padx=10,
            pady=10,
            columnspan =3,
            sticky=constants.EW
        )

    def _initialize_options(self):
        days = ttk.Label(master = self._frame, text = "Select one")
        days.grid(row= 1, column =0, pady=10)

        options = [('Today',1), ('This Month', 2),('This Year', 3), ('All', 4)]
        self._radio_var = IntVar()
        i =0
        for text, value in options:
            Radiobutton(master=self._frame, text=text, value=value, variable=self._radio_var).grid(row=2+i, column=0, padx=10, pady=10, sticky = constants.W)
            i+=1
        
        self._radio_var.set(1)

        bar_chart_button =ttk.Button(
            master= self._frame,
            text="Get stats",
            command = lambda:self._clean_data_summary()
        )
        bar_chart_button.grid(
            row= 6,
            column =0,
            pady =10,
            sticky = constants.EW
        )

    def _initialize_other(self):
        label_routines_days = ttk.Label(
            master=self._frame,
            text = str(self._summary_days)
        )  

        label_routines_exercises = ttk.Label(
            master=self._frame,
            text = str(self._summary_exercises)
        )    

        label_routines_total = ttk.Label(
            master=self._frame,
            text= str(self._summary_total)
        )

        label_routines_days_label = ttk.Label(
            master=self._frame,
            text = "No. of training days"
        )  

        label_routines_exercises_label = ttk.Label(
            master=self._frame,
            text = "No. of different exercises"
        )    

        label_routines_total_label = ttk.Label(
            master=self._frame,
            text= "Total lifted weighs"
        )

        label_routines_days.grid(row=2, column= 3, columnspan=3, padx=10, pady=10, sticky=constants.EW)
        label_routines_exercises.grid(row=2, column = 6, columnspan=3, padx=10, pady=10, sticky=constants.EW)
        label_routines_total.grid(row=2, column =9, columnspan=3, padx=10, pady=10, sticky=constants.EW)

        label_routines_days_label.grid(row=1, column= 3, columnspan=3, padx=10, pady=10, sticky=constants.EW)
        label_routines_exercises_label.grid(row=1, column = 6, columnspan=3, padx=10, pady=10, sticky=constants.EW)
        label_routines_total_label.grid(row=1, column =9, columnspan=3, padx=10, pady=10, sticky=constants.EW)
