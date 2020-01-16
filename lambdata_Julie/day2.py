class SuperList():

    def __init__(self, initial_state=[]):
        self._data = initial_state
        
    def __repr__(self):
        string_representation = str(self._data)
        return string_representation
    
    def __eq__(self, other):
        is_equal = self.__dict__ == other.__dict__
        return is_equal
    
    def append(self,new):
        self._data=self._data+[new]
        
    def reverse(self):
        self._data=self._data[::-1]
      
my_list=SuperList([1,2,3,4,5])
print(my_list)

my_list.append(6)
print(my_list)

my_list.reverse()
print(my_list)


class MyBankBalance():
    """
    An object that tracks a bank
    account balance
    """

    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.calc_string()

    def calc_string(self):
        """
        A helper method to update self.string
        """
        string_balance = "${:,.2f}".format(self.balance)
        self.string = string_balance

    def add_value(self, value):
        """
        Add value to the bank balance
        """
        self.balance += value
        self.calc_string()

mbb = MyBankBalance(3.50)
print(mbb.string)
mbb.add_value(17.01)
print(mbb.string)s