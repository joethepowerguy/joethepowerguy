class Employee:
    def __init__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'


def fullname(self):
    return '{} {}'.format(self.first, self.last)

emp_1 = Employee(Bob, Macneil, 50000)
emp_2 = Employee(Ralph, Smith, 6000)

print (emp_1.fullname())
print (emp_1.email)
print (emp_2.fullname())
print (emp_2.email)
