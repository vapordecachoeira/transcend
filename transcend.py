from datetime import datetime, timedelta, date
import random
import functools


class transcend(object):
    MAX_DAYS = (27393 / 7)

    def __init__(self, born):
        self.born = born

    def __call__(self, func):

        @functools.wraps(func)
        def decorated():
            now = datetime.now().date()
            delta = (now - self.born).days
            chance = random.uniform(0, 1)
            life = 1.0 - (float(delta) / float(self.MAX_DAYS))
            if life < 0:
                raise FunctionTranscended(func.__name__)
            # print chance, delta, life
            if chance < life:
                func()
            else:
                raise OneStepCloser(func.__name__)

        return decorated


class OneStepCloser(Exception):
    def __init__(self, fname, *args, **kwargs):
        message = 'Function %s is one step closer....' % (fname,)
        super(OneStepCloser, self).__init__(message, *args, **kwargs)


class FunctionTranscended(Exception):
    def __init__(self, fname, *args, **kwargs):
        message = 'Function %s have transcended this plane....' % (fname,)
        super(FunctionTranscended, self).__init__(message, *args, **kwargs)


# Usage / Example

if __name__ == '__main__':
    @transcend(date(2008, 10, 10))
    def func_hello_world():
        print ":(  I'm still around..."


    func_hello_world()
