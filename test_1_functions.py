"""Separate file for test_1 functions"""

from datetime import datetime
def format_message(message: str) -> list[str]:

    """Formats message string for validation"""

    message = message.replace('\n', '').split(' ')
    
    empty_string_count = message.count('')
    
    if empty_string_count != 0:
        for number in range(empty_string_count):
            message.remove('')

    return message


def get_timestamp(message: list[str]) -> str:

    """Returns timestamp from message"""

    timestamp = ' '.join(message[:2])

    return timestamp


def get_error_type(message: list[str]) -> str:

    """Returns the error type"""

    error_type = message[2:3][0]

    return error_type


def get_error_message(message: list[str]) -> str:

    """Returns the error message"""

    error_message = ' '.join(message[3:])

    return error_message


def error_message_to_dict(message: list[str]) -> dict:

    """Turns error message into a dict"""

    message = format_message(message)

    timestamp = get_timestamp(message)
    error_type = get_error_type(message)
    error_message = get_error_message(message)

    return {'timestamp': timestamp,
            'log_level': error_type,
            'message': error_message}