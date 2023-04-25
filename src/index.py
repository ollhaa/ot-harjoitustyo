from ttkthemes import ThemedTk
from ui.ui import UI


def main():
    window = ThemedTk(theme="black")
    window.title("Exercise diarys")
    #window.minsize(100, 100)
    #window.maxsize(600, 600)
    window.geometry("1000x1000")
    #window['background'] = 'skyblue'


    ui = UI(window)
    ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
