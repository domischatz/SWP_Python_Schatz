import LinkedList as myLinkedList


#Erstellen der ersten Knoten
node1=myLinkedList.Node(1)
node2=myLinkedList.Node(2)
node3=myLinkedList.Node(3)


linked_list = myLinkedList.LinkedList(node1)

# Knoten an die verkettete Liste anhängen
linked_list.append_to_linkedList(node2)
linked_list.append_to_linkedList(node3)

# Die verkettete Liste ausgeben
linked_list.print_linkedList()

# Die Länge der verketteten Liste abrufen und ausgeben
print("\nLength of linked list:", linked_list.get_length())
