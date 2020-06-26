from rply.token import BaseBox
from ppadb.client import Client
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no device attached')
    quit()

device = devices[0]


class MainBox(BaseBox):
    def __init__(self, assignments,expressions):
        self.expressions = expressions
        self.assignments = assignments

    def eval(self):
        for assignment in self.assignments.getlist():
            a = int(assignment.eval())
            for i in range(a):
                for expression in self.expressions.getlist():
                    expression.eval()

class AssignmentBox(BaseBox):
    def __init__(self, word, number):
        self.word = word
        self.number = number

    def eval(self):
        return self.number.getstr()


class AssignmentsBox(BaseBox):
    def __init__(self, assignments=None, assignment=None):
        self.assignments = assignments
        self.assignment = assignment

    def getlist(self):
        if self.assignments:
            return self.assignments.getlist() + [self.assignment]
        return []


class ActionBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getstr(self):
        return self.value.getstr()


class AppBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getstr(self):
        return self.value.getstr()

class IntBox(BaseBox):
    def __init__(self, value):
        self.value = value

    def getstr(self):
        return self.value.getstr()

class ExpressionBox(BaseBox):
    def __init__(self, action, appnum):
        self.action = action
        self.appnum = appnum

    def eval(self):
        print(self.action.getstr())
        print(self.appnum.getstr())
        if self.action.getstr() == "open":
            if self.appnum.getstr() == "whatsapp":
                device.shell(f'input keyevent KEYCODE_HOME')
                device.shell(f'am start -n com.whatsapp/.Main')
                time.sleep(0.5)
            elif self.appnum.getstr() == "settings":
                device.shell(f'monkey -p com.android.settings -c android.intent.category.LAUNCHER 1')
        elif self.action.getstr() == "close":
            if self.appnum.getstr() == "whatsapp":
                device.shell(f'am force-stop com.whatsapp')
                device.shell(f'input keyevent KEYCODE_HOME')
        elif self.action.getstr() == "wait":
            time.sleep(int(self.appnum.getstr()))
        elif self.action.getstr() == "unlockpw":
            device.shell(f'input keyevent 26')
            device.shell(f'input keyevent 82') 
            device.shell(f'input text {int(self.appnum.getstr())}')
            device.shell(f'input keyevent 66')
        elif self.action.getstr() == "send":
            #time.sleep(1)
            device.shell(f'input text {self.appnum.getstr()}')
            device.shell(f'input tap 1000 1253')
            #time.sleep(1)
        elif self.action.getstr() == "search":
            time.sleep(1)
            device.shell(f'input tap 890 188')
            device.shell(f'input text {self.appnum.getstr()}')
            device.shell(f'input tap 570 440')
        elif self.action.getstr() == "lock":
            device.shell(f'input keyevent 26')
            time.sleep(1)



class ExpressionSBox(BaseBox):
    def __init__(self, expressions=None, expression=None):
        self.expressions = expressions
        self.expression = expression

    def getlist(self):
        if self.expressions:
            return self.expressions.getlist() + [self.expression]
        return []
