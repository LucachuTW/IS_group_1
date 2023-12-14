class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    notFirstTime = False
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state) -> None:
        self.transition_to(state)

    def transition_to(self, state):
        """
        The Context allows changing the State object at runtime.
        """
        if self._state != state:
            print(f"Context: Transition to {state.__name__}")
            self._state = state
            self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def doSomething(self):
        self._state.main(self._state)
