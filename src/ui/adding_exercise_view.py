from tkinter import ttk, constants, Listbox, OptionMenu, constants, StringVar,IntVar, Scrollbar, Toplevel
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from services.diarys_service import diarys_service

class AddingExerciseView:

    def __init__(self, root, handle_logout):
        self.root = root
        self.frame = None
        self.handle_logout = handle_logout
        self.calender = None
        self.selected_date = None
        self.new=None
        self.listbox = None
        self.clicked = None
        self.clicked2 = None
        self.kg_entry= None
        self.to_routine = {}
        self.summary_table = None

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


    def add_to_alternatives(self):
        new = self.new.get()
        if new is not None:
            alt = new.lower()
            diarys_service.add_new_exercise(alt)
        self.new = None
        self.initialize_options()


    def add_to_routine(self):
        help_ = self.listbox.curselection()
        selected = self.listbox.get(help_[0])
        date = str(self.selected_date.cget("text"))
        date = datetime.strptime(date, '%d-%M-%Y').date()
        sets = self.clicked.get()
        reps= self.clicked2.get()
        kg = self.kg_entry.get()

        if date not in self.to_routine:
            self.to_routine[date] = [[],[],[],[]]
        
        if selected is not None and date is not None and kg is not None:
            self.to_routine[date][0].append(selected)
            self.to_routine[date][1].append(sets)
            self.to_routine[date][2].append(reps)
            self.to_routine[date][3].append(kg)

            joined_facts = str(date) + ": " + str(selected) + " " + str(sets) + "*" + str(reps) +"*" + str(kg)
            self.summary_table.insert(0, joined_facts)

        #print(self.to_routine)
        self.summary_table.grid(row=3, column=12, padx=15,columnspan=8, sticky=constants.N)
        
    def delete_added(self):
        #self.selected_date = None
        self.initialize_exercise_summary()
        self.to_routine.clear()

    def save_routine(self):
        if self.to_routine:
            diarys_service.add_new_routine(self.to_routine)

        self.delete_added()



    def open_popup(self):
        top= Toplevel(self.frame)
        top.geometry("500x500")
        top.title("Help: Adding exercise")
        ttk.Label(top, text= "Hello World!").place(x=150,y=80)



    def initialize(self):
        
        self.frame = ttk.Frame(master=self.root)
        
        self.initialize_logout_button()
        self.initialize_edit_view_button()
        self.initialize_summary_view_button()
        self.initialize_options()
        self.initialize_other()
        self.initialize_exercise_summary()
        self.initialize_help_button()
        

        

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
            column=3,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

    def initialize_summary_view_button(self):
        summary_view_button = ttk.Button(
            master=self.frame,
            text="ANALYTICS?",
            #background ='#A877BA'
        )

        summary_view_button.grid(
            row=0,
            column=5,
            padx=10,
            pady=10,
            columnspan =3,
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
            column=12,
            padx=10,
            pady=10,
            columnspan =3,
            sticky=constants.EW
        )


    
        
    def initialize_options(self):
        head_label = ttk.Label(master=self.frame, text="Choose the exercise:")
        exercise_names = diarys_service.find_all_exercises()
        #print(exercise_names)
        self.listbox = Listbox(master= self.frame, selectmode='SINGLE')
        for i in range(len(exercise_names)):
            #listbox.insert(i,"Maastaveto") 
            self.listbox.insert(i, exercise_names[i].get_name())


        head_label.grid(row=2, column=0, columnspan=2, sticky=constants.W)

        self.listbox.grid(
            row=3,
            column=0,
            padx=8,
            pady=6
        )

        add_exercise_button = ttk.Button(
            master=self.frame,
            text="Add to routine",
            command = lambda:self.add_to_routine()
        )

        save_routine_button = ttk.Button(
            master=self.frame,
            text="Save the routine",
            command= lambda:self.save_routine()
        )

        delete_selected_excercise_button = ttk.Button(
            master=self.frame,
            text="Delete added",
            command = lambda:self.delete_added()    
        )

        new_exercise_label = ttk.Label(
            master=self.frame, text="Add new exercise:")
        
        self.new = ttk.Entry(master=self.frame)
        new_exercise_label.grid(row=4, column=0, columnspan=2)
        self.new.grid(row=5, column=0, columnspan=2)

        add_new_exercise_button = ttk.Button(
            master=self.frame,
            text="Add to alternatives",
            command=lambda: self.add_to_alternatives()
        )

        add_new_exercise_button.grid(row=6, column=0, columnspan=2)
        delete_selected_excercise_button.grid(row=6, column=12, columnspan=6, sticky= constants.E)
        save_routine_button.grid(row=6, column=18, columnspan=6, padx=4, sticky=constants.W)

        add_exercise_button.grid(
            row=6,
            column=5,
            padx=4,
            pady=4,
            sticky=constants.EW
        )



    def initialize_other(self):
        date_label = ttk.Label(master= self.frame, text = "Choose the day:")
        self.calender = Calendar(master = self.frame,date_pattern="dd-mm-yyyy", selectmode = 'day',
               year = 2023, month = 1,
               day = 1)
        selected_date_label = ttk.Label(master= self.frame, text = "Press 'Confirm date':")
        self.selected_date = ttk.Label(master=self.frame)
        date_button= ttk.Button(
            master=self.frame,
            text="Confirm date",
            command = lambda:self.get_date()
            
        )

        select_label = ttk.Label(master=self.frame, text="Select options:")

        set_label = ttk.Label(master=self.frame, text="Sets:")
        self.clicked =IntVar(self.frame)
        self.clicked.set(3)
        alt_sets = [number for number in range(1,9)]
        self.set_menu = OptionMenu(self.frame, self.clicked, *alt_sets)

        rep_label = ttk.Label(master=self.frame, text="Reps:")
        self.clicked2 =IntVar(self.frame)
        self.clicked2.set(8)
        alt_reps = [number for number in range(1,13)]
        self.rep_menu = OptionMenu(self.frame, self.clicked2, *alt_reps)
        kg_label = ttk.Label(master=self.frame, text="Kilos:")
        clicked3 = IntVar(self.frame)
        clicked3.set(6)
        
        self.kg_entry = ttk.Combobox(master=self.frame, textvariable= clicked3, width=4)
        self.kg_entry['values'] = [number for number in range(50,150)]
        

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

        select_label.grid(row=2, column=5, pady=4)
        set_label.grid(row=3, column=5, columnspan=3, padx=4,sticky=constants.NW)
        self.set_menu.grid(row=3, column=5, columnspan=3, padx= 4, sticky=constants.NE) 

        rep_label.grid(row=3, column=5, columnspan=3,padx=4,  sticky=constants.W)
        self.rep_menu.grid(row=3, column=5, columnspan=3, padx= 4, sticky=constants.E)

        kg_label.grid(row=3, column=5, columnspan=3,padx=4, sticky=constants.SW)
        self.kg_entry.grid(row=3, column=5, columnspan=3, padx= 4, sticky=constants.SE)

    def initialize_exercise_summary(self):
        summary_label = ttk.Label(master=self.frame,
            text= "You are adding:"
            #command=self.add_to_routine
        )
        self.summary_table = Listbox(master=self.frame, width=40)
        summary_label.grid(row= 2, column= 12, padx= 15, columnspan=8, sticky=constants.N)
        self.summary_table.grid(row=3, column=12, padx=15,columnspan=8, sticky=constants.N)


