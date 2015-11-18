# map.reduce.1.py
# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, val, p=None):
        self.data = val
        self.next = p


class List(object):

    def __init__(self):
        self.head = Node(0)

    def push_back(self, val):
        p = self.head
        while p.next != None:
            p = p.next
        p.next = Node(val)

    def show(self):
        p = self.head
        while p.next != None:
            p = p.next
            print(p.data)

    def insert(self, location, value):
        p = self.__locate(location)
        neibor = p.next
        p.next = Node(value)
        p.next.next = neibor

    def delete(self, location):
        p = self.__locate(location)
        p.next = p.next.next

    def search(self, value):
        p = self.head
        i = 0
        while p != None:
            if p.data == value:
                return i
            p = p.next
            i = i + 1
        return -1
    def __locate(self, location):
        p = self.head
        i = 0
        while (p != None) and (i < location):
            p = p.next
            i = i + 1
        return p

    def create(self, max):
        i = 0
        for i in range(max):
            self.push_back(input('input value of node %d:' % (i + 1)))

def simple_ui():
    ls = List()

    lenth = input('input the lenth of the linked list:')
    ls.create(int(lenth))
    quit = False
    while not quit:
        print('''
1.push a node from back
2.insert a node
3.delete a node
4.search for a key value
5.show all the data
0.quit''')
        choice = input('select your choice')
        if choice == '1':
            ls.push_back(int(input('input value')))
        elif choice == '2':
            ls.insert(int(input('input location')),input('input value:'))
        elif choice == '3':
            ls.delete(int(input('input location')))
        elif choice == '4':
            print('the key you\'re looking for is in position ',ls.search(input('input value:')))
        elif choice == '5':
            ls.show()
        elif choice == '0':
            quit = True

if __name__ == '__main__':
    simple_ui()