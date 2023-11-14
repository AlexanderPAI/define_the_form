from logging import basicConfig, info, INFO


basicConfig(
    level=INFO,
    filename='app/tests/logs/main.log',
    filemode='w'
)
