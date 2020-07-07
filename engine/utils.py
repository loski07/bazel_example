import enum
import logging
import os
from abc import ABC, abstractmethod


class LexTokens(enum.Enum):
    """
    Enumeration for lexical tokens.
    """
    VERBATIM = 1
    INIT_EXPRESSION = 2
    END_EXPRESSION = 3
    INIT_LOOP = 4
    END_LOOP = 5
    BLANK = 6
    EOL = 7


class BaseManager(ABC):
    """
    Abstract class that defines the generic methods for all the Managers.
    """

    @abstractmethod
    def __init__(self, filepath):
        """
        Constructor that initializes the arguments of the object.
        :param filepath: String containing the path of the input file.
        :raise: IOError when there is no file with such path.
        """
        self._filepath = filepath
        self.logger = logging.getLogger(self.__class__.__name__)
        if not os.path.isfile(filepath):
            raise IOError("File {} not found".format(self._filepath))


class SyntaxElement(enum.Enum):
    """
    Enumeration for syntactical constructions.
    """
    VERBATIM = 0
    REPLACEMENT = 1
    LOOP = 2