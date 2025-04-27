"""This Module contains abstract classes for web-pages."""

import abc


class ABCPage(abc.ABC):
    """
    This is abstract class for all pages
    """
    @abc.abstractmethod
    def login(self):
        """
        This method performs login on website.
        Must be implemented in child classes.
        """

    @abc.abstractmethod
    def check_availability(self):
        """
        This method should click on 'Check Availability' button .
        Must be implemented in child classes.
        """

    @abc.abstractmethod
    def load(self):
        """
        This method should navigate to webpage.
        Must be implemented in child classes.
        """
