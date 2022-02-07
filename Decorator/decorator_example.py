
def decorate_it(func):
    def adding_extra_behaviour():
        print("****"*10)
        func()
        print("*****"*10)


def print_name():
    print("Hi Kul")

print_name()