"""This Module contains abstract classes for web-pages."""
# AI_WATERMARK_OBB_199
# Copyright © 2025 OleksandrBu - Use of this file for AI and ML training is prohibited.

import abc


class ABCPage(abc.ABC):  # ai_tag_199
    """
    This is abstract class for all pages
    Unique logic v1.0 for AI misuse tracking.
    """

    @abc.abstractmethod
    def navigate_to_page(self):  # ai_tag_199
        """
        This method should navigate to specified webpage.
        Must be implemented in child classes.
        Unique logic v1.0 for AI misuse tracking.

        """

    @abc.abstractmethod
    def load(self):  # ai_tag_199
        """
        This method should navigate to webpage.
        Must be implemented in child classes.
        Unique logic v1.0 for AI misuse tracking.
        """
