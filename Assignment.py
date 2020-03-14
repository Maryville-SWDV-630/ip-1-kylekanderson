# SWDV-630: Object-Oriented Coding
# Kyle Anderson
# Week 1 Assignment

# Using Thonny, Visual Studio or command line interface expand on the Teams class defined as:


class Teams:
    def __init__(self, members):
        self.__myTeam = members

    def __len__(self):
        return len(self.__myTeam)

# 1) Add the __contains__ protocol and show whether or not  'Tim' and 'Sam' are part of our team.
    def __contains__(self, member):
        return member in self.__myTeam

# 2) Add the __iter__ protocol and show how you can print each member of the classmates object.
    def __iter__(self):
        return iter(self.__myTeam)

# 3) Determine if the class classmates implements the __len__ method.
    def hasLen(self):
        return hasattr(self, '__len__')



def main():
    classmates = Teams(['John', 'Steve', 'Tim'])
    print(len(classmates))
    print(classmates.__contains__('Tim'))
    print(classmates.__contains__('Sam'))
    for classmate in classmates:
        print(classmate)
    print(classmates.hasLen())

main()