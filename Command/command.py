# pylint: disable=arguments-differ
"The Command Pattern Concept"
from abc import ABCMeta, abstractmethod

class ICommand(metaclass=ABCMeta):  # pylint: disable=too-few-public-methods
    "The command interface, that all commands will implement"
    @staticmethod
    @abstractmethod
    def execute():
        "The required execute method that all command objects will use"

class Invoker:
    "The Invoker Class"

    def __init__(self):
        self._commands = {}

    def register(self, command_name, command):
        "Register commands in the Invoker"
        self._commands[command_name] = command

    def execute(self, command_name):
        "Execute any registered commands"
        if command_name in self._commands.keys():
            self._commands[command_name].execute()
        else:
            print(f"Command [{command_name}] not recognised")

class Light:
    "The Receiver"

    @staticmethod
    def switch_on():
        print("Switching On the Light")

    @staticmethod
    def switch_off():
        print("Switching Off the Light")

class CommandOn(ICommand):  # pylint: disable=too-few-public-methods
    def __init__(self, light):
        self._receiver = light

    def execute(self):
        self._receiver.switch_on()

class CommandOff(ICommand):  # pylint: disable=too-few-public-methods
    def __init__(self, light):
        self._receiver = light

    def execute(self):
        self._receiver.switch_off()

# The CLient
# Create a receiver
RECEIVER = Light()

# Create Commands
COMMAND1 = CommandOn(RECEIVER)
COMMAND2 = CommandOff(RECEIVER)

# Register the commands with the invoker
INVOKER = Invoker()
INVOKER.register("1", COMMAND1)
INVOKER.register("2", COMMAND2)

# Execute the commands that are registered on the Invoker
INVOKER.execute("1")
INVOKER.execute("2")
INVOKER.execute("1")
INVOKER.execute("2")