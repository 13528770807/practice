

class Calculator:  # 创建类
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result

    def subtract(self):
        result = self.num1 - self.num2
        return result

    def multiply(self):
        result = self.num1 * self.num2
        return result

    def divide(self):
        result = self.num1 / self.num2
        return result


calc = Calculator(28, 2)  # 实例化对象
add = calc.add()  # 调用add()方法
print(add)
print(calc.subtract())
print(calc.multiply())
print(calc.divide())


