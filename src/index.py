from ttkthemes import ThemedTk
from ui.ui import UI


def main():
    window = ThemedTk(theme="black", background=True)
    window.title("Exercise diarys")
    window.geometry("1000x1000")
    ui_ = UI(window)
    ui_.start()
    window.mainloop()

if __name__ == "__main__":
    main()
