from Observer import Observer
from PhoneObserver import PhoneObserver
from PhoneObserverw import PhoneObserverw
class main:
    obs = Observer()
    phone = PhoneObserver()
    phonew = PhoneObserverw()
    obs.attach(phone)
    obs.attach(phonew)
    obs.notify("on")
    obs.notify("off")

if __name__ == "__main__":
    main()