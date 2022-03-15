from abc import ABC, abstractmethod

class Subscriber(ABC):

    @classmethod
    def __subclasshook__(cls, obj_cls):
        if (hasattr(obj_cls, "receive") and callable(obj_cls.receive)):
            return True
        return False

    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def receive(self, message):
        pass

class EmailSubscriber(Subscriber):

    def __init__(self, name):
        super().__init__(name)

    def receive(self, message):
        print(self.name, "got an e-mail:", message)

class SMSSubscriber(Subscriber):

    def __init__(self, name):
        super().__init__(name)

    def receive(self, message):
        print(self.name, "got an SMS:", message)


class Admin:

    def __init__(self):
        self.subscribers = []

    def register(self, subscriber):
        if issubclass(Subscriber, type(subscriber)):
            self.subscribers.append(subscriber)
        else:
            raise ValueError("Wrong type attempted to subscribe")

    def push_notification(self, message):
        for sub in self.subscribers:
            sub.receive(message)

if __name__ == "__main__":
    boss = Admin()
    boss.register(EmailSubscriber("Arne"))
    boss.register(SMSSubscriber("Berit"))
    #boss.register(1234)

    boss.push_notification("Gratis godis på Eurospar!!!!")