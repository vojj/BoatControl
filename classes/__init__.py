try:
    import pigpio # start pigpio on pi first!!
except Exception:
    from classes.class_gpio_mock import Gpio_mock as pigpio