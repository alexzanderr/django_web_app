
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {"rich": {"datefmt": "[%X]"}},
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "formatter": "rich",
            "level": "DEBUG",

            # not working
            # "rich_traceback": True,
        },
        # not working
        # "file": {
        #     "class": "rich.logging.RichHandler",
        #     "filename": "logs/dev_server/logs.log",
        #     "level": "DEBUG",
        # }
    },
    "loggers": {"django": {"handlers": ["console"]}},
}