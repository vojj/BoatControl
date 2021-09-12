# This class provides a interface to send events
# Bugs and changes:
# 11.09.21 - Initial - vojj
#
# @author vojj
#

from pydispatch import Dispatcher

_event = None


class EventDispatcher:

    def __init__(self, event=None):
        global _event
        if _event is None:
            _event = Eventhandler()

    def do_quit(self):
        # do stuff that makes new data
        data = "PleaseKillAllThread"
        # Then emit the change with optional positional and keyword arguments
        _event.emit('on_quit', data=data)

    def register(self, name, callback):
        kwargs = {name: callback}
        _event.bind(**kwargs)


class Eventhandler(Dispatcher):
    def __init__(self, event=None):
        pass

    # Events are defined in classes and subclasses with the '_events_' attribute
    _events_ = ['on_quit']