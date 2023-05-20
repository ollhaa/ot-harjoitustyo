from ui.create_user_view import CreateUserView
from ui.login_view import LoginView
from ui.adding_exercise_view import AddingExerciseView
from ui.analytics_view import AnalyticsView
from ui.edit_view import EditView

class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_create_user_view()

    def _show_create_user_view(self):
        self._hide_current_view()
        self._current_view = CreateUserView(
            self._root,
            self._show_login_view
        )
        self._current_view.pack()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._show_create_user_view,
            self._show_adding_excercise_view
        )

        self._current_view.pack()

    def _show_adding_excercise_view(self):
        self._hide_current_view()

        self._current_view = AddingExerciseView(
            self._root,
            self._show_login_view,
            self._show_analytics_view,
            self._show_edit_view
        )
        self._current_view.pack()

    def _show_analytics_view(self):
        self._hide_current_view()

        self._current_view = AnalyticsView(
            self._root,
            self._show_login_view,
            self._show_adding_excercise_view,
            self._show_edit_view
        )
        self._current_view.pack()

    def _show_edit_view(self):
        self._hide_current_view()

        self._current_view = EditView(
            self._root,
            self._show_login_view,
            self._show_adding_excercise_view,
            self._show_analytics_view
        )
        self._current_view.pack()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
