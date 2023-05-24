import webbrowser


def decoratori(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper


@decoratori
def open_urla():
    webbrowser.open("https://google.com")


actual = input("vvod chaild")