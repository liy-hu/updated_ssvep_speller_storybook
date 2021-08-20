# This file contains a list of extended classes
init -1509 python:

    @renpy.pure
    class VariableInputValueAttempt(VariableInputValue):

        def enter(self):
            store.attempts -= 1
            return self.get_text()
