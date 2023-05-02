from ttkthemes import ThemedTk
from ui.ui import UI


def main():
    window = ThemedTk(theme="black")
    window.title("Exercise diarys")
    window.geometry("1000x1000")
    ui = UI(window)
    ui.start()
    window.mainloop()

if __name__ == "__main__":
    main()
