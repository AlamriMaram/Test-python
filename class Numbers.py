class Numbers:
    def __init__(self):
        self.numbers= []
        
    def add_number(self, num):
        self.numbers.append(num)
        
    def sum_numbers(self):
        summ =0
        for i in self.numbers:
            summ += i
        return summ
n1 = Numbers()
n1.add_number(2)
n1.add_number(3)
print(n1.sum_numbers())