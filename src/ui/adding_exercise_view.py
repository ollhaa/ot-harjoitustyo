from tkinter import ttk, constants


class AddingExerciseView:

    def __init__(self, root):
        self.root = root
        self.frame = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def initialize(self):
        self.frame = ttk.Frame(master=self.root)

        logout_button = ttk.Button(
            master=self.frame,
            text="Logout?"
        )

        logout_button.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky=constants.EW
        )
