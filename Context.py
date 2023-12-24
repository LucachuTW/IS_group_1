class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.

    Contributors:
        - @SantiagoRR2004
    """

    def __init__(self, state, user) -> None:
        """
        Initialize the Context instance with the given state.

        This method sets the initial state of the Context.

        Args:
            - state (State): The initial state.
            - user (Any): The instance which is using Context.

        Contributors:
            - @SantiagoRR2004
        """
        self._state = None
        self.user = user
        self.transition_to(state)

    def transition_to(self, state):
        """
        The Context allows changing the State object at runtime.

        This method changes the current state of the Context to the given state.

        Args:
            - state (State): The state to transition to.

        Contributors:
            - @SantiagoRR2004
        """
        if not isinstance(self._state, state):
            print(f"Context: Transition to {state.__name__}")
            self._state = state(self.user)
            self._state.context = self

    def doSomething(self):
        """
        The Context delegates part of its behavior to the current State object.

        This method calls the main method of the current state.

        Contributors:
            - @SantiagoRR2004
        """
        self._state.main()
