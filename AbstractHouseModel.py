from abc import ABC, abstractmethod
from typing import Any, List
import AbstractHouseEnv
import AbstractHouseView


class AbstractHouseModel(ABC):
    def setRelationships(self, environment: Any, viewer: Any) -> None:
        """
        Establishes relationships between the current model instance, an environment,
        and a viewer for efficient communication and control.

        Args:
            environment (Type[Any]): The environment class.
            viewer (Type[Any]): The viewer class.

        Returns:
            None

        Contributors:
            - @SantiagoRR2004
        """
        controler = environment()
        view = viewer()
        view.setController(controler)
        view.setModel(self)
        controler.setView(view)
        controler.setModel(self)
        self.view = view
        self.controler = controler

    def getController(self) -> Any:
        """
        Retrieve the controller associated with the current instance.

        Returns:
            Any: The controller object.

        Note:
            This method provides access to the controller assigned to the instance.
            Ensure that the controller has been properly set before calling this method.

        Contributors:
            - @SantiagoRR2004
        """
        return self.controler

    def getView(self) -> Any:
        """
        Get the current view associated with this object.

        Returns:
            Any: The current view.

        Note:
            This method returns the view assigned to the object.
            Ensure that the view has been properly set before calling this method.

        Contributors:
            - @SantiagoRR2004
        """
        return self.view

    def __repr__(self) -> str:
        """
        Return a string representation of the object suitable for debugging.

        Returns:
            str: A string representation of the object.

        Contributors:
            - @SantiagoRR2004
        """
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({attributes})"

    def getAttribute(self, name: str) -> Any:
        """
        Retrieve the value of the specified attribute by its name.

        Parameters:
        - name (str): The name of the attribute to retrieve.

        Returns:
        - Any: The value of the specified attribute.

        Raises:
        - AttributeError: If the attribute with the given name does not exist.

        Contributors:
        - @SantiagoRR2004
        """
        return getattr(self, name.lower())

    def setAttribute(self, name: str, value: Any) -> None:
        """
        Set an attribute on the object dynamically.

        This method allows dynamically setting attributes on the object by providing
        a name and a corresponding value. The attribute name is converted to lowercase
        before setting to ensure case-insensitive access.

        Args:
            name (str): The name of the attribute to be set.
            value (Any): The value to set for the attribute.

        Returns:
            None: This method does not return anything.

        Contributors:
            - @SantiagoRR2004
        """
        setattr(self, name.lower(), value)

    def getAttributeFromDict(self, name: str, key: Any) -> Any:
        """
        Retrieve a specific key from the dictionary associated with the given attribute.

        Args:
            name (str): The name of the attribute.
            key (Any): The key to retrieve from the attribute's dictionary.

        Returns:
            Any: The value associated with the specified key in the attribute's dictionary.

        Raises:
            KeyError: If the attribute does not exist or
                      the specified key is not present in its dictionary.

        Contributors:
            @SantiagoRR2004
        """
        return self.getAttribute(name)[key]

    def setAttributeFromDict(self, name: str, key: Any, value: Any) -> None:
        """
        Set a specific key-value pair in a nested dictionary attribute.

        Parameters:
        - name (str): The name of the attribute (nested dictionary) to be updated.
        - key (Any): The key within the nested dictionary to be set or updated.
        - value (Any): The new value to be assigned to the specified key.

        Returns:
            None

        Example:
        >>> obj = YourClass()
        >>> obj.setAttributeFromDict('nested_attribute', 'key1', 'new_value')
        >>> print(obj.nested_attribute)
        {'key1': 'new_value'}

        Contributors:
            @SantiagoRR2004
        """
        self.getAttribute(name)[key] = value

    def modifyNumericalAttributeFromDict(self, name: str, key: Any, value: int) -> None:
        """
        Modify a numerical attribute in a dictionary by adding a specified value.

        Parameters:
        - name (str): The name of the dictionary attribute.
        - key (Any): The key to identify the specific element within the attribute.
        - value (int): The value to add to the original attribute value.

        Returns:
            None

        Contributors:
            @SantiagoRR2004
        """
        original = self.getAttributeFromDict(name, key)
        self.setAttributeFromDict(name, key, original + value)

    @staticmethod
    def calculateDistanceBetween2Points(x1: int, y1: int, x2: int, y2: int) -> float:
        """
        Calculate the Euclidean distance between two points in a 2D plane.

        Parameters:
        - x1 (int): x-coordinate of the first point.
        - y1 (int): y-coordinate of the first point.
        - x2 (int): x-coordinate of the second point.
        - y2 (int): y-coordinate of the second point.

        Returns:
        float: Euclidean distance between the two points.

        Example:
        ```python
        distance = YourClass.calculateDistanceBetween2Points(0, 0, 3, 4)
        print(distance)  # Output: 5.0
        ```

        Contributors:
        - @SantiagoRR2004 (initial implementation)
        """
        return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1 / 2)

    @staticmethod
    def checkIfPrime(n: int) -> bool:
        """
        Check if a given integer is a prime number.

        This function implements a primality test based on the algorithm described in:
        https://en.wikipedia.org/wiki/Primality_test

        Args:
            n (int): The integer to be checked for primality.

        Returns:
            bool: True if the input integer is a prime number, False otherwise.

        Examples:
            >>> YourClass.checkIfPrime(7)
            True
            >>> YourClass.checkIfPrime(4)
            False

        Contributors:
            - @SantiagoRR2004: Initial implementation and algorithm reference.
        """
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = int(n ** (1 / 2))
        for i in range(5, limit + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    @staticmethod
    def PrimeFactorization(n: int) -> List[int]:
        """
        Compute the prime factorization of a given integer.

        This method uses a basic prime factorization algorithm to find the prime factors
        of the given integer 'n' as stated in
        https://stackoverflow.com/questions/15347174/python-finding-prime-factors.

        Parameters:
        - n (int): The integer for which prime factorization is to be computed.

        Returns:
        List[int]: A list of prime factors of the input integer 'n'.

        Contributors:
        - @SantiagoRR2004

        Example:
        >>> YourClassName.PrimeFactorization(12)
        [2, 2, 3]
        >>> YourClassName.PrimeFactorization(20)
        [2, 2, 5]
        """
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)

        return factors
