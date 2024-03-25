import random

class RandomIterable:
    def __iter__(self):
        return self
    def __next__(self):
        if random.choice(["go", "go", "stop"]) == "stop":
            raise StopIteration  # signals "the end"
        return 1

for eggs in RandomIterable():
   print(eggs)
"""
1
1
1
1
1
1
1
"""

# rosowa ilość zwracanych elementów
print(list(RandomIterable()), "end")
print(list(RandomIterable()), "end")
print(list(RandomIterable()), "end")
print(list(RandomIterable()), "end")
"""
[] end
[1, 1, 1] end
[1] end
[] end
"""