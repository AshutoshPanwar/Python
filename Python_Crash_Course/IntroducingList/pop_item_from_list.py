# pop() method removes last item from the list and let's you work with that item after removing it.

motorcycles = ['honda', 'Royal Enfield', 'BMW']
print(motorcycles)

poped_item = motorcycles.pop()
print(motorcycles)
print(f"My dream bike is {poped_item.title()}")