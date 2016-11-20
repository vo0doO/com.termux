class SpecialString:
    def __init__(self, count):
        self.count = count

    def __truediv__(self, other):
        line = "=" * len(other.count)
        return "\n".join([self.count, line, other.count])

spam = SpecialString("spam")
hello = SpecialString("hello")
print(spam / hello)
