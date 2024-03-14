from abc import ABC
from collections.abc import Iterator

# Knoten in der verketteten Liste.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # Zeiger, der auf None gesetzt


class LinkedList(): #verkettete Liste
    def __init__(self, head): #Startknoten (head)
        self.Head = head

    def print_linkedList(self): #iteriert duch jeden Knoten und gibt jeden Wert aus.
        current_node = self.Head
        while current_node is not None:
            print(current_node.data, end=" ") #Wert des aktuellen Knotens
            current_node = current_node.next #nächster Knoten
    def get_length(self):
        current_node = self.Head
        i=0
        while current_node is not None:
            current_node = current_node.next #nächster Knoten
            i = i + 1
        return i

    def append_to_linkedList(self, new_node):
        past_node = None
        current_node = self.Head
        while current_node is not None:
            past_node = current_node     # vorherigen Knoten als aktuellen Knoten
            current_node = current_node.next #nächster Knoten
        if current_node is None: #ende der Liste
            past_node.next = new_node #ende wird an liste angehängt