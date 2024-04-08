class dog:
    def bark(self):
        print("Bow,Wow")
class Duck:
    def talk(self):
        print("Quack,quack")
class Human:
    def talk(self):
        print("Hello,hi")
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()
x=Duck()
call_talk(x)
x=Human()
call_talk(x)
x=dog()
call_talk(x)
