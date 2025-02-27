# We are creating a PhoneObserver class that will inherit from Observable class
from Observable import Observable
class PhoneObserver(Observable):
    def update(self, value):
        print("PhoneObserver: Phone is now " + value)
    