from tkinter import ttk, constants, Listbox, OptionMenu, constants, StringVar
from tkcalendar import Calendar, DateEntry
from services.diarys_service import diarys_service


class AddingExerciseView:

    def __init__(self, root, handle_logout):
        self.root = root
        self.frame = None
        self.handle_logout = handle_logout
        self.calender = None
        self.selected_date = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def logout_handler(self):
        diarys_service.logout()
        self.handle_logout()

    def get_date(self):
        self.selected_date.config(text= self.calender.get_date())

    #def add_to_alternatives(self, alternative):
    #    listbox.insert(5, alternative)


    def initialize(self):
        
        self.frame = ttk.Frame(master=self.root)
        
        self.initialize_logout_button()
        self.initialize_edit_view_button()
        self.initialize_summary_view_button()
        self.initialize_options()

        

    def initialize_logout_button(self):
        logout_button = ttk.Button(
            master=self.frame,
            text="Logout?",
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
            text="Edit exercices?"
        )

        edit_view_button.grid(
            row=0,
            column=3,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

    def initialize_summary_view_button(self):
        summary_view_button = ttk.Button(
            master=self.frame,
            text="See overview?"
        )

        summary_view_button.grid(
            row=0,
            column=5,
            padx=10,
            pady=10,
            sticky=constants.EW
        )


    
        
    def initialize_options(self):
        head_label = ttk.Label(master=self.frame, text="Choose exercise:")
        
        listbox = Listbox(master= self.frame)  
        listbox.insert(1,"Maastaveto")  
        listbox.insert(2, "Penkkipunnerrus")  
        listbox.insert(3, "Jalkakyykky")  
        listbox.insert(4, "Leuanveto")

        date_label = ttk.Label(master= self.frame, text = "Choose the day:")
        self.calender = Calendar(master = self.frame, selectmode = 'day',
               year = 2023, month = 1,
               day = 1)
        selected_date_label = ttk.Label(master= self.frame, text = "Press 'Confirm date':")
        self.selected_date = ttk.Label(master=self.frame)
        date_button= ttk.Button(
            master=self.frame,
            text="Confirm date",
            command = lambda:self.get_date()
            
        )


        set_label = ttk.Label(master=self.frame, text="Choose the number of sets:")
        clicked =StringVar(self.frame)
        clicked.set('3')
        alt_sets = ['1', '2', '3', '4','5','6','7','8','9','10']
        set_menu = OptionMenu(self.frame, clicked, *alt_sets)

        rep_label = ttk.Label(master=self.frame, text="Choose the number of reps:")
        clicked2 =StringVar(self.frame)
        clicked2.set('8')
        alt_reps = ['1', '2', '3', '4','5','6','7','8','9','10']
        rep_menu = OptionMenu(self.frame, clicked2, *alt_reps)
        
        add_exercise_button = ttk.Button(
            master=self.frame,
            text="Add to routine"
            
            
        )

        new_exercise_label = ttk.Label(
            master=self.frame, text="Add new exercise:")
        
        new_excercise = ttk.Entry(master=self.frame)
       
        head_label.grid(row=2, column=0, columnspan=2, sticky=constants.W)

        listbox.grid(
            row=3,
            column=0,
            padx=8,
            pady=6
        )

        new_exercise_label.grid(row=4, column=0, columnspan=2)
        new_excercise.grid(row=5, column=0, columnspan=2)
        
        add_new_exercise_button = ttk.Button(
            master=self.frame,
            text="Add to alternatives"
            #command=lambda: self.add_to_alternatives("dippi")
        )

        add_new_exercise_button.grid(row=6, column=0, columnspan=2)

        add_exercise_button.grid(
            row=6,
            column=5,
            padx=4,
            pady=4,
            sticky=constants.EW
        )
        
        date_label.grid(row=2, column=3)
        self.calender.grid(row = 3, column= 3)
        selected_date_label.grid(row=4, column=3)
        self.selected_date.grid(row=5, column=3, columnspan=2)
        date_button.grid(
            row=6,
            column=3,
            padx=4,
            pady=4,
            sticky=constants.EW
        )

        set_label.grid(row=2, column=5, columnspan=2)
        set_menu.grid(row=3, column=5, columnspan=2)

        rep_label.grid(row=4, column=5, columnspan=2)
        rep_menu.grid(row=5, column=5, columnspan=2)


