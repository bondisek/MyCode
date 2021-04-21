import time
def timer(func):
    def wrapper():
        before = time.time()
        func()
        print("Funkce trvala:", time.time() - before, "sekund")
    return wrapper