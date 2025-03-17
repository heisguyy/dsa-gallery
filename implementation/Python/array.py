"""Module showing an implementation of an array."""

from typing import List, Optional


class Array:
    """
    Implementation of the array data structure
    """

    def __init__(self, length_of_array: int, data_type) -> None:
        self.__length_of_array = length_of_array
        self.__data_type = data_type
        self.__counter = 0
        self.__array = [None] * self.__length_of_array

    def __str__(self) -> str:
        return str(self.__array)

    def resize(self, increment_factor: int = 2) -> None:
        """
        Function to create a larger array and copy all elements from the
        old array into the new array.

        Args:
            increment_factor (int, optional): This arguement determines the
            factor by which the new array is larger than the old one. Defaults
            to 2.
        """
        self.__length_of_array *= increment_factor
        new_array = [None] * self.__length_of_array
        for index, element in enumerate(self.__array):
            new_array[index] = element
        self.__array = new_array

    def check_index_validity(self, index: int) -> bool:
        """
        Function to check whether it is ok to input a value at an index.

        Args:
            index (int): location in an array to input a value.
        Returns:
            bool: Whether the index is valid or not. True show it is valid while
            False shows it's not.
        """
        if index > self.__counter:
            return False
        if index < 0 and (index + self.__length_of_array) > self.__counter:
            return False
        return True

    def insert(self, element, index: Optional[int] = None) -> List:
        """
        Function to insert an element into an array.

        Args:
            element (_type_): Value to input into array
            index (Optional[int], optional): Index to insert the element at. Use
            this parameter only if you want to displace an already initialized
            element. Defaults to None.

        Raises:
            TypeError: This is raised when the element doesn't match what the
            array was initialized with.
            ValueError: This is raised when the index specified defies the
            contiguous logic of and array.

        Returns:
            List: The new array with the element inserted.
        """
        if not isinstance(element, self.__data_type):
            raise TypeError(
                "Arrays should be homologous, this value is not of "
                f"{self.__data_type} type."
            )
        if self.__counter >= self.__length_of_array:
            self.resize()
        if index is not None:
            if self.check_index_validity(index):
                for index_difference, value in enumerate(
                    self.__array[self.__counter - 1 : index - 1 : -1]
                ):
                    self.__array[self.__counter - index_difference] = value
                self.__array[index] = element
                self.__counter += 1
            else:
                raise ValueError(
                    "Arrays should be contiguous. The index is not a valid "
                    "point to put an element."
                )
        else:
            self.__array[self.__counter] = element
            self.__counter += 1
        return self.__array

    def __getitem__(self, index: int):
        """
        Function that allows you to access elements using the square braces and
        an index.

        Args:
            index (int): index of the item to get.
        """
        return self.__array[index]

    def delete(self, index: int) -> None:
        """
        Function to delete a value from an index

        Args:
            index (int): Index to be deleted

        Raises:
            IndexError: Raised when index is empty.
        """
        if index >= self.__counter:
            raise IndexError("There is no value at the specified index.")
        for index_difference, value in enumerate(
            self.__array[index + 1 : self.__counter]
        ):
            self.__array[index + index_difference] = value
        self.__counter -= 1
        self.__array[self.__counter] = None


if __name__ == "__main__":
    my_array = Array(5, int)
    print(my_array)

    my_array.insert(1)
    print(my_array)

    my_array.insert(3, 1)
    print(my_array[1])

    my_array.delete(1)
    print(my_array)
