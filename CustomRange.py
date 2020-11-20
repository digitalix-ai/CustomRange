class MyGen:
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
        MyGen.current = self.first - 1

    def __iter__(self):
        while True:
            if MyGen.current < self.last - 1:
                MyGen.current += 1
                yield MyGen.current
            else:
                break
        return self

gen = MyGen(6, 15)
for i in gen:
    print(i)