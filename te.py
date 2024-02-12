def ger(f_name, l_name):
    print(f_name + " " + l_name)

rr = ger('dkdkd', 'eeeee')
print(rr)

while True:
    o = input("what: ")
    print("hello: " + o)
    if o == 'no':
        break
    elif o == "karim":
        print("hello admin: " + o)


class Ali:
    def __init__(self, name, age, date):
        self.name = name
        self.age = age
        self.date = date

    def r(self):
        login = self.name + " " + str(self.age) + " " + str(self.date)
        return login

h = "dkld"
