"""This Module contains abstract classes for web-pages."""

import abc


class ABCPage(abc.ABC):
    """
    This is abstract class for all pages
    """

    @abc.abstractmethod
    def navigate_to_page(self):
        """
        This method should navigate to specified webpage.
        Must be implemented in child classes.
        """

    @abc.abstractmethod
    def load(self):
        """
        This method should navigate to webpage.
        Must be implemented in child classes.
        """
