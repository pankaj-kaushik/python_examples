class Hit(Exception):
    def __init__(self, msg):
        self.msg = msg
    def show_exception(self):
        print 'user defined exception caught : ', self.msg
        

try:
    raise Hit("i met with an accident")
except Hit as e:
    e.show_exception()