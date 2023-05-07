from tkinter import ttk, constants, StringVar, Toplevel, IntVar, Radiobutton
from services.diarys_service import diarys_service, UsernameExistsError
from datetime import datetime
#import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd


class AnalyticsView:

    def __init__(self, root, handle_logout ,handle_show_adding_excercise_view):
        self.root = root
        self.frame = None
        self.handle_logout = handle_logout
        self.handle_show_adding_excercise_view = handle_show_adding_excercise_view
        #self.handle_show_login_view = handle_show_login_view
        self.radio_var = 1
       
        self.summary_days =0
        self.summary_exercises =0
        self.summary_total =0
        
        
        self.initialize()

    def pack(self):
        # if self.frame is not None:
        self.frame.pack(fill=constants.X)

    def destroy(self):
        # if self.frame is not None:
        self.frame.destroy()

    def logout_handler(self):
        diarys_service.logout()
        self.handle_logout()

    def clean_data_summary(self):
        routines = pd.DataFrame(diarys_service.find_all_routines())
        column_names = ["Id", "Date", "Exercise", "Sets", "Reps", "Kilos"]
        routines.columns = column_names
        routines = routines.assign(Total = lambda x: x.Sets * x.Reps * x.Kilos)
        
        #year, month, week = str(routines["Date"].datetime.isocalendar())
        
        routines["Year"] = routines.Date.str[:4]
        routines["Month"] = routines.Date.str[6:7]
        #print(routines)

        cur_day= datetime.today().date()
        cur_month = cur_day.month
        cur_year = cur_day.year

        #print(str(cur_month))
        #print(str(cur_year))

        radio_var = self.radio_var.get()
        #print(radio_var)

        if radio_var ==1:
            routines_summary = routines[routines["Date"] == str(cur_day)]
        elif radio_var ==2:
            routines_summary = routines[routines["Month"] == str(cur_month)]
            routines_summary = routines_summary[routines_summary["Year"] == str(cur_year)]
        elif radio_var == 3:
            routines_summary = routines[routines["Year"] == str(cur_year)]
        else:
            routines_summary = routines.copy()

        self.summary_days = len(routines_summary.Date.unique())
        self.summary_exercises = len(routines_summary.Exercise.unique())
        self.summary_total = routines_summary.Total.sum()


        #print(today)
        
        #print(routines.dtypes)
        #print(routines)
        #print(reenit)

        labels = routines_summary.Exercise.unique().tolist()

        print(labels)
        print(len(labels))
        sizes = routines_summary.groupby(['Exercise']).sum()
        sizes = sizes.Total.tolist()
        print(sizes)

        #labels= ['a','v','c','t']
        #sizes = [15, 30, 45, 10]

        figure = plt.Figure(figsize=(3,3), dpi=100)
        plt.pie(sizes, labels=labels)
        plt.show()

        self.initialize_other()

    def open_popup(self):
        top= Toplevel(self.frame)
        top.geometry("500x500")
        top.title("Help: Adding exercise")
        ttk.Label(top, text= "Hello World!").place(x=150,y=80)

    def adding_view_handler(self):
        self.handle_show_adding_excercise_view()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)
        self.initialize_logout_button()
        self.initialize_edit_view_button()
        self.initialize_help_button()
        self.initialize_adding_exercise_view_button()
        self.initialize_options()

        self.initialize_other()
        



    def initialize_logout_button(self):
        logout_button = ttk.Button(
            master=self.frame,
            text="LOGOUT?",
            #bg ="red",
            command = self.logout_handler
        )

        logout_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

    def initialize_edit_view_button(self):
        edit_view_button = ttk.Button(
            master=self.frame,
            text="EDIT?",
            #bg ="red"
        )

        edit_view_button.grid(
            row=0,
            column=6,
            padx=10,
            pady=10,
            columnspan =3,
            sticky=constants.EW
        )

    def initialize_adding_exercise_view_button(self):
        summary_view_button = ttk.Button(
            master=self.frame,
            text="ADD?",
            #background ='#A877BA'
            command = lambda:self.adding_view_handler()
        )

        summary_view_button.grid(
            row=0,
            column=3,
            padx=10,
            pady=10,
            
            sticky=constants.EW
        )
    
    def initialize_help_button(self):
        help_button = ttk.Button(
            master=self.frame,
            text="HELP?",
            command= lambda:self.open_popup()
            #background ='#A877BA'
        )

        help_button.grid(
            row=0,
            column=9,
            padx=10,
            pady=10,
            columnspan =3,
            sticky=constants.EW
        )

    def initialize_options(self):
        days = ttk.Label(master = self.frame, text = "Select one")
        days.grid(row= 1, column =0, pady=10)

        options = [('Today',1), ('This Month', 2),('This Year', 3), ('All', 4)]
        self.radio_var = IntVar()
        i =0
        for text, value in options:
            Radiobutton(master=self.frame, text=text, value=value, variable=self.radio_var).grid(row=2+i, column=0, padx=10, pady=10, sticky = constants.W)
            i+=1
        
        #self.radio_var.set(1)

        bar_chart_button =ttk.Button(
            master= self.frame,
            text="Get stats",
            command = lambda:self.clean_data_summary()
        )
        bar_chart_button.grid(
            row= 6,
            column =0,
            pady =10,
            sticky = constants.EW
        )

    def initialize_other(self):
        label_routines_days = ttk.Label(
            master=self.frame,
            text = str(self.summary_days)
        )  

        label_routines_exercises = ttk.Label(
            master=self.frame,
            text = str(self.summary_exercises)
        )    

        label_routines_total = ttk.Label(
            master=self.frame,
            text= str(self.summary_total)
        )

        label_routines_days_label = ttk.Label(
            master=self.frame,
            text = "No. of training days"
        )  

        label_routines_exercises_label = ttk.Label(
            master=self.frame,
            text = "No. of different exercises"
        )    

        label_routines_total_label = ttk.Label(
            master=self.frame,
            text= "Total lifted weighs"
        )

        label_routines_days.grid(row=2, column= 3, columnspan=3, padx=10, pady=10, sticky=constants.EW)
        label_routines_exercises.grid(row=2, column = 6, columnspan=3, padx=10, pady=10, sticky=constants.EW)
        label_routines_total.grid(row=2, column =9, columnspan=3, padx=10, pady=10, sticky=constants.EW)

        label_routines_days_label.grid(row=1, column= 3, columnspan=3, padx=10, pady=10, sticky=constants.EW)
        label_routines_exercises_label.grid(row=1, column = 6, columnspan=3, padx=10, pady=10, sticky=constants.EW)
        label_routines_total_label.grid(row=1, column =9, columnspan=3, padx=10, pady=10, sticky=constants.EW)

        


        