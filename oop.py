class User():
    def log(self):
        print('Users')

class Teacher(User):
    def log(self):
        print('I am a Teacher!! ')

class Customer(User):
    def log(self):
        print('I am a Customer!! ')
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        print('Calculating  costs')
        self.membership_type = new_membership

    def __str__(self):
        return  self.name + ' ' + self.membership_type
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def print_all_customers(customers):
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.memebership_type == other.memebership_type:
            return True
        return False
    __hash__ = None
    __repr__ = __str__

users = [Customer('Abiola', 'Gold'),
        Customer('Damola', 'Diamond'),
        Teacher()]

for user in users:
    user.log()
