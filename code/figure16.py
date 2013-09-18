"""
Figure 16: Fragility of labeling descriptors
"""

class CallbackProperty(object):
    """A property that will alert observers when upon updates"""
    def __init__(self, default=None):
        self.data = WeakKeyDictionary()
        self.default = default
        self.callbacks = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self        
        return self.data.get(instance, self.default)

    def __set__(self, instance, value):
        for callback in self.callbacks.get(instance, []):
            # alert callback function of new value
            callback(value)
        self.data[instance] = value

    def add_callback(self, instance, callback):
        """Add a new function to call everytime the descriptor within instance updates"""
        if instance not in self.callbacks:
            self.callbacks[instance] = []
        self.callbacks[instance].append(callback)

class BankAccount(object):
    balance = CallbackProperty(0)

def low_balance_warning(value):
    if value < 100:
        print "You are now poor"

ba = BankAccount()
ba.balance.add_callback(ba, low_balance_warning)
#BankAccount.balance.add_callback(ba, low_balance_warning)

ba.balance = 5000
print "Balance is %s" % ba.balance
ba.balance = 99
print "Balance is %s" % ba.balance
