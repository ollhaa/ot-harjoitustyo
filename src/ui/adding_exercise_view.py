from tkinter import ttk, constants, Listbox
from services.diarys_service import diarys_service


class AddingExerciseView:

    def __init__(self, root, handle_logout):
        self.root = root
        self.frame = None
        self.handle_logout = handle_logout

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def logout_handler(self):
        diarys_service.logout()
        self.handle_logout()

    def initialize(self):
        
        self.frame = ttk.Frame(master=self.root)
        self.initialize_options()
        self.initialize_something()

        

    def initialize_something(self):
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
        
        

    def initialize_options(self):
        head_label = ttk.Label(master=self.frame, text="Choose exercise:")
        
        listbox = Listbox(master= self.frame)  
        #listbox = Listbox(root)  
   
        listbox.insert(1,"Maastaveto")  
        listbox.insert(2, "Penkkipunnerrus")  
        listbox.insert(3, "Jalkakyykky")  
        listbox.insert(4, "Leuanveto")

        new_exercise_label = ttk.Label(
            master=self.frame, text="Add new exercise:")
        
        new_excercise = ttk.Entry(master=self.frame)
       
        head_label.grid(row=1, column=0, columnspan=2, sticky=constants.W)

        listbox.grid(
            row=2,
            column=0,
            padx=8,
            pady=8
        )

        new_exercise_label.grid(row=3, column=0, columnspan=2)
        new_excercise.grid(row=4, column=0, columnspan=2)
        
        add_new_exercise_button = ttk.Button(
            master=self.frame,
            text="Add",
            #command=self.create_user_handler
        )

        add_new_exercise_button.grid(row=5, column=0, columnspan=2)


