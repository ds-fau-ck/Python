
def decorate_it(func):
    def adding_extra_behaviour():
        print("****"*10)
        func()
        print("*****"*10)
    return adding_extra_behaviour


def print_name():
    print("Hi Kul")

#print_name()
my_name=decorate_it(print_name)
my_name()