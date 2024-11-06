class Queue:
    def __init__(self) -> None:
        self._list = []
        
    
    def is_empty(self):
        return len(self._list) == 0
    
    def enqueue(self, item):
        self._list.append(item)
    
    def dequeue(self):
        return self._list.pop(0)
    
    def size(self):
        return len(self._list)
    
    def traverse(self):
        for item in self._list:
