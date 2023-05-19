from tkinter import ttk, constants, Listbox, OptionMenu, constants, StringVar,IntVar, Scrollbar, Toplevel
from datetime import datetime
from tkcalendar import Calendar, DateEntry
from services.diarys_service import diarys_service

class AddingExerciseView:

    def __init__(self, root, handle_logout, handle_analytics_view, handle_edit_view):
        self._root = root
        self._frame = None
        self._handle_logout = handle_logout
        self._handle_analytics_view = handle_analytics_view
        self._handle_edit_view = handle_edit_view
        self._calender = None
        self._selected_date = None
        self._new=None
        self._listbox = None
        self._clicked = None
        self._clicked2 = None
        self._kg_entry= None
        self._to_routine = {}
        self._summary_table = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        diarys_service.logout()
        self._handle_logout()

    def _analytics_handler(self):
        self._handle_analytics_view()

    def _get_date(self):
        self._selected_date.config(text= self._calender.get_date())


    def _add_to_alternatives(self):
        new = self._new.get()
        if new is not None:
            alt = new.lower()
            exists_alt = diarys_service.find_all_exercises()
            print(exists_alt)
            exists_alt = [x.name for x in exists_alt]
            print(exists_alt)
            if alt not in exists_alt:
                diarys_service.add_new_exercise(alt)
        self._new = None
        self._initialize_options()


    def _add_to_routine(self):
        help_ = self._listbox.curselection()
        selected = self._listbox.get(help_[0])
        date = str(self._selected_date.cget("text"))
        print("date first:", str(date))
        date = datetime.strptime(date, '%d-%m-%Y').date()
        print("date then: ", str(date))
        sets = self._clicked.get()
        reps= self._clicked2.get()
        kg = self._kg_entry.get()

        if date not in self._to_routine:
            self._to_routine[date] = [[],[],[],[]]
        
        if selected is not None and date is not None and kg is not None:
            self._to_routine[date][0].append(selected)
            self._to_routine[date][1].append(sets)
            self._to_routine[date][2].append(reps)
            self._to_routine[date][3].append(kg)

            joined_facts = str(date) + ": " + str(selected) + " " + str(sets) + "*" + str(reps) +"*" + str(kg)
            self._summary_table.insert(0, joined_facts)

        #print(self.to_routine)
        self._summary_table.grid(row=3, column=12, padx=15,columnspan=8, sticky=constants.N)
        
    def _delete_added(self):
        #self.selected_date = None
        self._initialize_exercise_summary()
        self._to_routine.clear()

    def _save_routine(self):
        if self._to_routine:
            diarys_service.add_new_routine(self._to_routine)

        self._delete_added()



    def _open_popup(self):
        top= Toplevel(self._frame)
        top.geometry("605x190")
        top.resizable(0, 0)
        top.title("Help: Adding exercise")
        ttk.Label(top, text= 
        "Select from left the exercise*..\n"
        "(note: You can add new exercise to list by writing the name and pressing 'Add to alternative)\n"
        "..then select the day and press 'Confirm date..\n"
        "..then select sets, reps and kilos..\n"
        "..now you can add this to routines by pressing 'Add to routine'..\n"
        "\n"
        "*Now you have two options:\n"
        "\t *Delete added by pressing 'Delete added' or \n"
        "\t *Save added by pressing 'Save the routine'"
        "\n"
        "You can also go Analytics view ('ANALYTICS?) or to other frames.\n"
        "If you want to logout then press 'LOGOUT?" 
        ).place(x=0,y=0)



    def _initialize(self):
        
        self._frame = ttk.Frame(master=self._root)
        
        self._initialize_logout_button()
        self._initialize_edit_view_button()
        self._initialize_summary_view_button()
        self._initialize_options()
        self._initialize_other()
        self._initialize_exercise_summary()
        self._initialize_help_button()
        

        

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

    def _initialize_edit_view_button(self):
        edit_view_button = ttk.Button(
            master=self._frame,
            text="EDIT?",
            command = self._handle_edit_view
        )

        edit_view_button.grid(
            row=0,
            column=3,
            padx=10,
            pady=10,
            sticky=constants.EW
        )

    def _initialize_summary_view_button(self):
        summary_view_button = ttk.Button(
            master=self._frame,
            text="ANALYTICS?",
            #background ='#A877BA'
            command = lambda:self._analytics_handler()
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


    
        
    def _initialize_options(self):
        head_label = ttk.Label(master=self._frame, text="Choose the exercise:")
        exercise_names = diarys_service.find_all_exercises()
        #print(exercise_names)
        self._listbox = Listbox(master= self._frame, selectmode='SINGLE')
        for i in range(len(exercise_names)):
            #listbox.insert(i,"Maastaveto") 
            self._listbox.insert(i, exercise_names[i].get_name())


        head_label.grid(row=2, column=0, columnspan=2, sticky=constants.W)

        self._listbox.grid(
            row=3,
            column=0,
            padx=8,
            pady=6
        )

        add_exercise_button = ttk.Button(
            master=self._frame,
            text="Add to routine",
            command = lambda:self._add_to_routine()
        )

        save_routine_button = ttk.Button(
            master=self._frame,
            text="Save the routine",
            command= lambda:self._save_routine()
        )

        delete_selected_excercise_button = ttk.Button(
            master=self._frame,
            text="Delete added",
            command = lambda:self._delete_added()    
        )

        new_exercise_label = ttk.Label(
            master=self._frame, text="Add new exercise:")
        
        self._new = ttk.Entry(master=self._frame)
        new_exercise_label.grid(row=4, column=0, columnspan=2)
        self._new.grid(row=5, column=0, columnspan=2)

        add_new_exercise_button = ttk.Button(
            master=self._frame,
            text="Add to alternatives",
            command=lambda: self._add_to_alternatives()
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



    def _initialize_other(self):
        date_label = ttk.Label(master= self._frame, text = "Choose the day:")
        self._calender = Calendar(master = self._frame,date_pattern="dd-mm-yyyy", selectmode = 'day',
               year = 2023, month = 1,
               day = 1)
        selected_date_label = ttk.Label(master= self._frame, text = "Press 'Confirm date':")
        self._selected_date = ttk.Label(master=self._frame)
        date_button= ttk.Button(
            master=self._frame,
            text="Confirm date",
            command = lambda:self._get_date()
            
        )

        select_label = ttk.Label(master=self._frame, text="Select options:")

        set_label = ttk.Label(master=self._frame, text="Sets:")
        self._clicked =IntVar(self._frame)
        self._clicked.set(3)
        alt_sets = [number for number in range(1,9)]
        self._set_menu = OptionMenu(self._frame, self._clicked, *alt_sets)

        rep_label = ttk.Label(master=self._frame, text="Reps:")
        self._clicked2 =IntVar(self._frame)
        self._clicked2.set(8)
        alt_reps = [number for number in range(1,13)]
        self._rep_menu = OptionMenu(self._frame, self._clicked2, *alt_reps)
        kg_label = ttk.Label(master=self._frame, text="Kilos:")
        clicked3 = IntVar(self._frame)
        clicked3.set(6)
        
        self._kg_entry = ttk.Combobox(master=self._frame, textvariable= clicked3, width=4)
        self._kg_entry['values'] = [number/10.0 for number in range(0,2000, 5)]
        

        date_label.grid(row=2, column=3)
        self._calender.grid(row = 3, column= 3)
        selected_date_label.grid(row=4, column=3)
        self._selected_date.grid(row=5, column=3, columnspan=2)
        date_button.grid(
            row=6,
            column=3,
            padx=4,
            pady=4,
            sticky=constants.EW
        )

        select_label.grid(row=2, column=5, pady=4)
        set_label.grid(row=3, column=5, columnspan=3, padx=4,sticky=constants.NW)
        self._set_menu.grid(row=3, column=5, columnspan=3, padx= 4, sticky=constants.NE) 

        rep_label.grid(row=3, column=5, columnspan=3,padx=4,  sticky=constants.W)
        self._rep_menu.grid(row=3, column=5, columnspan=3, padx= 4, sticky=constants.E)

        kg_label.grid(row=3, column=5, columnspan=3,padx=4, sticky=constants.SW)
        self._kg_entry.grid(row=3, column=5, columnspan=3, padx= 4, sticky=constants.SE)

    def _initialize_exercise_summary(self):
        summary_label = ttk.Label(master=self._frame,
            text= "You are adding:"
            #command=self.add_to_routine
        )
        self._summary_table = Listbox(master=self._frame, width=40)
        summary_label.grid(row= 2, column= 12, padx= 15, columnspan=8, sticky=constants.N)
        self._summary_table.grid(row=3, column=12, padx=15,columnspan=8, sticky=constants.N)


