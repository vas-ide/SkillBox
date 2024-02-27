# -*- coding: utf-8 -*-



custom_time_format = '%Y-%m-%d %H:%M:%S'
custom_time_format_add = "%b %d %Y %H:%M:%S"

log_config = {
    "version": 1,
    "formatters": {
        "errors_formatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "datefmt": custom_time_format_add
        },
        "chat_formatter": {
            "format": "%(asctime)s - %(message)s",
            "datefmt": custom_time_format_add
        },
    },
    "handlers": {
        "errors_handler": {
            "class": "logging.FileHandler",
            "formatter": "errors_formatter",
            "filename": "log_crf/errors.log",
            "encoding": "UTF-8",
        },
        "chat_handler": {
            "class": "logging.FileHandler",
            "formatter": "chat_formatter",
            "filename": "log_crf/chat.log",
            "encoding": "UTF-8",
        },
    },
    "loggers": {
        "errors": {
            "handlers": ["errors_handler"],
            "level": "DEBUG",
        },
        "chat": {
            "handlers": ["chat_handler"],
            "level": "INFO",
        },
    },
}
