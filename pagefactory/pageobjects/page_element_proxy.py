from types import MethodType


class PageElementProxy:

    def __init__(self, cls, handler_cls):
        self.cls = cls
        self.handler_cls = handler_cls
        self.cached_handlers = {}

    def __call__(self, *args, **kwargs):
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattr__(self, attr):
        res = None
        if hasattr(self.obj, attr):
            res = getattr(self.obj, attr)
            if type(res) is MethodType:
                if self.cached_handlers[res] is None:
                    self.cached_handlers[res] = self.handler_cls(self.obj, res)
                return self.cached_handlers[res]
            else:
                return res
        return res


class PageElementHandler:

    def __init__(self, obj, func):
        self.obj = obj
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)
