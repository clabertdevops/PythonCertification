class SimpleTracer:
    def __init__(self,  func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('Calls %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    
@SimpleTracer
def spam_simple(a, b, c):
    print(a + b + c)

spam_simple(1, 2, 3)
spam_simple(a=4, b=5, c=6)

class tracer(object):
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('Call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)
    def __get__(self, instance, owner):
        return wrapper(self, instance)
    
class wrapper:
    def __init__(self, func, subj):
        self.desc = func
        self.subj = subj
    def __call__(self, *args, **kwargs):
       return self.desc(self.subj, *args, **kwargs)


@tracer
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 3)
spam(a=4, b=5, c=6)

#Singleton

instances = {}
def getInstances(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]

def singleton(aClass):
    def onCall(*args):
        return getInstances(aClass, *args)
    return onCall

@singleton
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton
class Spam:
    def __init__(self, val):
        self.attr = val

bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())

sue = Person('Sue', 30, 20)
print(bob.name, bob.pay())

def Tracer(aClass):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.fetchs = 0
            self.wrapped = aClass(*args, **kwargs)
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)
            return getattr(self.wrapped, attrname)
    return Wrapper

@Tracer
class SpamTracer:
    def display(self):
        print('SpamTracer.display')

@Tracer
class PersonTracer:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate
    
food = SpamTracer()
food.display()
print([food.fetchs])

pippo = PersonTracer('Mr. John', 40, 10)
print(pippo.name, pippo.pay())
