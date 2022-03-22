
from io import UnsupportedOperation


class Light:

    def turnOn(self):
        print("Light is ON")

    def turnOff(self):
        print("Light is OFF")



class ICommand:

    def __init__(self, light):
        self.light = light

    def execute(self):
        raise UnsupportedOperation("Cannot call execute on interface object")
    
class CommandOn(ICommand):

    def __init__(self, light):
        super().__init__(light)
    
    def execute(self):
        self.light.turnOn()

class CommandOff(ICommand):

    def __init__(self, light):
        super().__init__(light)
    
    def execute(self):
        self.light.turnOff()


class LightSwitch:

    def __init__(self):
        self.commands = {}
        self.commandQueue = []
        self.history = []
        self.commandCount = 0
    
    def register(self, commandName, command):
        self.commands[commandName] = command

    def queueCommand(self, commandName):
        self.commandQueue.append(commandName)

    def executeAll(self):
        for command in self.commandQueue:
            self.commands[command]()
            self.history.append(command)
            self.commandCount += 1

    def undo(self):
        self.commands[self.history[-2]]()
        self.commandCount -= 2

    def redo(self):
        self.commands[self.history[self.commandCount + 1]]()
        self.commandCount += 1


if __name__ == "__main__":
    lightbulb = Light()
    lightswitch = LightSwitch()

    lightswitch.register("on", CommandOn(lightbulb).execute)
    lightswitch.register("off", CommandOff(lightbulb).execute)

    lightswitch.queueCommand("on")
    lightswitch.queueCommand("off")
    lightswitch.queueCommand("on")

    lightswitch.executeAll()

    print("Undo:")

    lightswitch.undo()

    print("Redo:")

    lightswitch.redo()
