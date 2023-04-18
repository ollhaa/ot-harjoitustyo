from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title("Exercise diarys")
    # window.geometry("600x500")
    window['background'] = 'skyblue'

    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
