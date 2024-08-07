'''
链表
'''
class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(2)
print(id(node1))
print(id(node2))
a,b = node1,node2
print(id(a),id(b))


class SignleNodeList():
    '''单向链表'''
   
    '''def is emptyself)
    链表是为空
    Length()
    链表长度
    travel()
    濾方黧个链表
    add(item
    链表头部添加元素
    append(item
    链表具部添加元素
    insert(pos,item)
    指定位置添加元素
    remove(item)
    则除节点
    search(item)】
    我节点是存在
    '''
    def __init__(self,node:Node=None):
        self._head = node


    def is_empty(self):
        if self._head == None:
            return True
        else:
            return False

    def length(self):
        count = 0
        cur = self._head
        while cur != None:
            count += 1
            cur = cur.next
        return  count

    def travel(self):
        cur = self._head
        while cur!=None :
            print(cur.value)
            cur = cur.next

    def add(self):
        pass

    def append(self,item):
        nod = Node(item)
        if self.is_empty():
            self._head = nod
        else:
            cur = self._head
            while cur.next!=None :
                cur = cur.next
            cur.next = nod



if __name__ == '__main__':
    nl = SignleNodeList()
    print(nl.length())
    print(nl.is_empty())
    nl.append(1)
    nl.append(2)
    print(nl.is_empty())
    print(nl.length())
    nl.travel()
