from typing import Any


class Wrapper:
    """
    This class serves to make a class modify and set
    attributes of an owner instance instead of changing itself.

    Maybe this could be considered a proxy.

    Contributors:
        - @SantiagoRR2004
    """

    def __init__(self, owner: Any) -> None:
        """
        This sets the instance which needs to be modified.

        Args:
            - owner (Any): The instance from which it depends.

        Returns:
            None: This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        self.owner = owner

    def __del__(self) -> None:
        """
        This makes sure it doesn't use other deletes.

        Returns:
            None: This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        pass

    def __getattr__(self, name: str) -> Any:
        """
        When an attribute can't be found in the instance it searches
        in the owner instance.

        Args:
            - name (str): The name of the attribute.

        Returns:
            Any: It tries to return the attribute.

        Contributors:
            - @SantiagoRR2004
        """
        try:
            return getattr(self.owner, name)
        except Exception as e:
            print(f"An exception of type {type(e).__name__} occurred: {e}")
            raise e

    def __setattr__(self, name: str, value: Any) -> None:
        """
        It sets the attributes in the owner instance except
        when it tries to set the owner instance or it sets the context
        for the State pattern.

        It needs to use the self.__dict__[name] = value because otherwise
        it would enter an infinite loop trying to set the owner or context.

        Args:
            - name (str): The name of the attribute.
            - value (Any): The value of the attribute to be set.

        Returns:
            Any: It tries to return the attribute.

        Contributors:
            - @SantiagoRR2004

        Other options:
            This are options for the else that can be used:
                - setattr(self.owner, name, value)
                - object.__setattr__(self.owner, name, value)
                - self.owner.__setattr__(name, value)
        """
        if name == "owner" or name == "context":
            self.__dict__[name] = value
        else:
            self.owner.__dict__[name] = value