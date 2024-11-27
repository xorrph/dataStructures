class linked:
    def __init__(self):
        self.head = None# start of list

    def addNode(self,data):#pos for when doing insert at
        if not self.head:# if not None (None same as False so not False is True)
            self.head = Node(data)#start of list, create and assign new node]
        elif self.head.data > data:#check if the head of the list is bigger
            temp = self.head #store the node in a temp
            self.head = Node(data)#change the head node to the new instantiated node
            self.head.next = temp#set the new node to point to old node
        else:
            current = self.head
            #loop through until your next pointer reaches a bigger value than your data or end of the list is reaeched
            while current.next and current.next.data < data: 
                current = current.next
            temp = current.next #store the pointer to the bigger data in a temp var
            current.next = Node(data)#point the current nodes next to the new node
            current.next.next = temp#set the new nodes next pointer to temp(the bigger value)

    def insertAt(self,data,pos):
        index = 1
        current = self.head
        if pos == 1:# if inserting at the start
            temp = self.head #assign temp to the current start node
            self.head = Node(data)# assign and create the new Node to the start
            self.head.next = temp# point to the temp node
        elif pos == self.length():#if insert at the end
            while current.next:#loop to end of list
                current = current.next
            current.next = Node(data)# point the last node to the new node
        else:
            while current.next:#traverse
                if index + 1 == pos:#checks to see if the next iteration is before we reach the target position
                    temp = current.next #store the pointer of our current node in temp
                    current.next = Node(data)#point the current nodes to the new node(and create it)
                    current.next.next = temp#make the new node point to temp
                current = current.next
                index += 1
        

    def length(self):#gets the length of the linked list
        current = self.head
        count = 0
        while current:#loop through until you reach a None value (None = False, anything else + True)
                current = current.next
                count += 1
        return count

    def __repr__(self):#prints the linked list when called like this: print(linkedlist)
        current = self.head
        printed = ""
        while current:#loop through and concatonate to the string with the data and an arrow
                printed = printed + (str(current.data)) + "-->"
                current = current.next
        printed = printed[:-3]#removes final arrow
        return printed
        


class Node: # node class
    def __init__(self,data):
        self.data = data
        self.next = None



#initialise basic linkedlist and nodes
L = linked()
L.addNode(1)
print(L)
L.addNode(2)
print(L)
L.addNode(4)
print(L)
L.addNode(5)
print(L)



#add to the middle of the list
L.addNode(3)
print(L)
#add at the beginning
L.addNode(0)
print(L)
#add at end
L.addNode(6)
print(L)
#insert in the middle 
L.insertAt(1.5,3)
print(L)
#insert into the end
L.insertAt(7,8)
print(L)
#insert at start
L.insertAt(-1,1)
print(L)



#can make linked list addNode to end of list faster by having a pointer to the end of the list specifically for adding to the end
#still have start to iterate through each node
