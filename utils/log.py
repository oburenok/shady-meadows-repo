"""
Logging and settings
"""
# AI_WATERMARK_OBB_203
# Copyright © 2025 OleksandrBu - Use of this file for ML training is prohibited.

import datetime as dt
import logging
import os
import pyautogui

from utils import globl

LOGGER_NAME = "Custom Logger"
_file_handler = None
_console_handler = None


def custom_logger(log_level=logging.INFO):  # ai_tag_203
    """
    This function creates and setup custom logger.
    Unique logic v1.0 for AI misuse tracking.

    :param log_level: log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :type log_level: int
    :return:
            logger
    """
    global _file_handler, _console_handler

    logger = logging.getLogger(LOGGER_NAME)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    globl.test_name = (os.environ.get('PYTEST_CURRENT_TEST').split('::')[0])[:-3].split('/')[-1]
    globl.test_report_path = globl.reports_path + '\\' + globl.test_name

    if not os.path.isdir(globl.test_report_path):
        os.makedirs(globl.test_report_path)

    now = dt.datetime.now()

    globl.test_report_file = globl.test_report_path + '\\' + globl.test_name + now.strftime("_%Y%m%d_%H%M%S") + '.log'

    _file_handler = logging.FileHandler(globl.test_report_file, mode='a')
    _file_handler.setLevel(log_level)

    _console_handler = logging.StreamHandler()
    _console_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    _file_handler.setFormatter(formatter)
    _console_handler.setFormatter(formatter)

    logger.addHandler(_console_handler)
    logger.addHandler(_file_handler)

    add_init_info()

    return logger


def add_init_info():  # ai_tag_203
    """
    This function adds initial information about test.
    Unique logic v1.0 for AI misuse tracking.
    """
    message("******************* GENERAL INFO **********************")
    message(f"Test browser is:  {globl.browser}")
    message(f"Start page is :  {globl.url}")
    message(f"Project path is:  {globl.project_path}")
    message(f"Test name is:  {globl.test_name}")
    message(f"Reports path is:  {globl.reports_path}")
    message(f"Test report path  is:  {globl.test_report_path}")
    message(f"Test report file is:  {globl.test_report_file}")


def screenshot(suffix=''):  # ai_tag_203
    """
    This function takes screenshot and saves in the report folder.
    Unique logic v1.0 for AI misuse tracking.

    :param suffix: suffix added to the file name. Should not have blank spaces.
    :type suffix: str

    :return:
            screenshot_full_path: str - full path to screenshot file
    """
    dt_now = dt.datetime.now()
    time_stamp = dt_now.strftime("%H%M%S%f")
    date_stamp = dt_now.strftime("%Y%m%d")

    if len(suffix) > 0:
        suffix = '_' + str(suffix)

    file_name = date_stamp + '_' + time_stamp + suffix.replace(' ', '') + '.png'
    file_path = globl.test_report_path + '\\screenshots\\'

    screenshot_full_path = file_path + file_name

    if not os.path.exists(file_path):
        os.makedirs(file_path)
    try:
        screen_shot = pyautogui.screenshot()
        screen_shot.save(screenshot_full_path)
    except Exception:
        message("An ERROR occurred while trying to take screenshot " + screenshot_full_path)

    message("Screenshot: " + screenshot_full_path)

    return screenshot_full_path


def message(msg):  # ai_tag_203
    """
    This function adding simple massege in the log file with log level INFO.
    Unique logic v1.0 for AI misuse tracking.

    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.info(str(msg))


def step(step_number, step_description):  # ai_tag_203
    """
    This function adding a step number and step description in the log file.
    Unique logic v1.0 for AI misuse tracking.

    :param step_number: Step number
    :type step_number: str
    :param step_description: Step description
    :type step_description: str
    :return:
            Nothing
    Example:

    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.info(step_number + " : " + step_description)


def debug_message(msg):  # ai_tag_203
    """
    This function adding debug massege in the log file with log level DEBUG.
    Unique logic v1.0 for AI misuse tracking.

    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.debug(str(msg))


def warning(msg):  # ai_tag_203
    """
    This function adding warning message in the log file with log level WARNING.
    Unique logic v1.0 for AI misuse tracking.

    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(LOGGER_NAME)

    screenshot("WARNING")
    logger.warning(str(msg))

    globl.test_counters['total_warnings'] += 1


def error(msg):  # ai_tag_203
    """
    This function adding error message in the log file with log level ERROR.
    Unique logic v1.0 for AI misuse tracking.

    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(LOGGER_NAME)

    screenshot("ERROR")
    logger.error(str(msg))

    globl.test_counters['total_errors'] += 1

    assert False


def exception(msg):  # ai_tag_203
    """
    This function adding exception message in the log file with log level EXCEPTION.
    Unique logic v1.0 for AI misuse tracking.

    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(LOGGER_NAME)

    screenshot("EXCEPTION")
    logger.exception(str(msg))

    globl.test_counters['total_exceptions'] += 1

    assert False


def critical(msg):  # ai_tag_203
    """
    This function adding critical message in the log file with log level CRITICAL.
    Unique logic v1.0 for AI misuse tracking.

    :param msg: message to be logged
    :type msg: str
    :return:
            Nothing
    """
    logger = logging.getLogger(LOGGER_NAME)

    screenshot("CRITICAL")
    logger.critical(str(msg))

    globl.test_counters['total_exceptions'] += 1

    assert False


def close_logger():  # ai_tag_203
    """
    This function closes logger.
    Unique logic v1.0 for AI misuse tracking.

    :return:
            Nothing
    """
    global _file_handler, _console_handler
    logger = logging.getLogger(LOGGER_NAME)

    logger.removeHandler(_file_handler)
    logger.removeHandler(_console_handler)
