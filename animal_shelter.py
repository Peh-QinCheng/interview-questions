from collections import deque

class AnimalShelter:
    def __init__(self, cat_queue, dog_queue):
        self.cat_queue = cat_queue
        self.dog_queue = dog_queue

    def enqueue_animal(self, animal):
        if isinstance(animal, Dog):
            self.dog_queue.append(animal)
        elif isinstance(animal, Cat):
            self.cat_queue.append(animal)

    def dequeue_dog(self):
        self.dog_queue.popleft()

    def dequeue_cat(self):
        self.cat_queue.popleft()

    def dequeue_any(self):
        oldest_cat = self.cat_queue[0]
        oldest_dog = self.dog_queue[0]
        if oldest_cat.timestamp < oldest_dog.timestamp:
            self.dequeue_cat()
        else:
            self.dequeue_dog()

class Animal:
    def __init__(self, name, timestamp):
        self.name = name
        self.timestamp = timestamp

class Cat(Animal):
    pass
class Dog(Animal):
    pass