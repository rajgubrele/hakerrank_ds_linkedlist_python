#!/usr/bin/env python
# coding: utf-8

# ##
# Linked Lists ---> Insert a Node at the Tail of a Linked List
# 
# You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.##

# In[ ]:


import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    new_list = SinglyLinkedListNode(data)
    if head is None:
        head = new_list
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_list
    return head
        

if __name__ == '__main__':

