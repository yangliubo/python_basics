class Stack:
    def __init__(self) -> None:
        self._list = []
        
    def push(self, item):
        self._list.append(item)
        
    def pop(self):
        return self._list.pop()
    
    def is_empty(self):
        return True if len(self._list)==0 else False
    
    def traverse(self):
        return self._list[-1::-1]