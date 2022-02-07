def decorate_it(func):
    def adding_extra_behaviour(*args, **kwargs):
        print("****"*10)
        func(*args, **kwargs)
        print("*****"*10)
    return adding_extra_behaviour

@decorate_it
def print_name(name):
    print(f"Hi  from {name}")



print_name("Kul")
print_name("TUCchkul")
   
