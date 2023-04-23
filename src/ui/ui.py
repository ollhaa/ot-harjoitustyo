from ui.create_user_view import CreateUserView
from ui.login_view import LoginView
from ui.adding_exercise_view import AddingExerciseView


class UI:

    def __init__(self, root):
        self.root = root
        self.current_view = None

    def start(self):
        self.show_create_user_view()

    def show_create_user_view(self):
        self.hide_current_view()
        self.current_view = CreateUserView(
            self.root,
            self.show_login_view
        )
        self.current_view.pack()

    def show_login_view(self):
        self.hide_current_view()

        self.current_view = LoginView(
            self.root,
            self.show_create_user_view,
            self.show_adding_excercise_view
        )

        self.current_view.pack()

    def show_adding_excercise_view(self):
        self.hide_current_view()

        self.current_view = AddingExerciseView(
            self.root,
            self.show_login_view


        )

        self.current_view.pack()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None
