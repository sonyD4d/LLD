from Observable import Observable
class PhoneObserverw(Observable):
    def update(self, value):
        print("PhoneObserverw: Phone is now " + value)
    