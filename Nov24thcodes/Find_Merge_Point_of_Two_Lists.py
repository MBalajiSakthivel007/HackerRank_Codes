#!/bin/python3

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
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if self.head is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node is not None:
        fptr.write(str(node.data))
        node = node.next

        if node is not None:
            fptr.write(sep)


# ---------------------------------------------------
# Find Merge Node Function
# ---------------------------------------------------
def findMergeNode(head1, head2):
    p1 = head1
    p2 = head2

    while p1 != p2:
        if p1 is None:
            p1 = head2
        else:
            p1 = p1.next

        if p2 is None:
            p2 = head1
        else:
            p2 = p2.next

    return p1.data


# ---------------------------------------------------
# MAIN (LOCAL MACHINE COMPATIBLE)
# ---------------------------------------------------
if __name__ == '__main__':
    fptr = sys.stdout   # FIXED: Works locally without OUTPUT_PATH error

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist1_count = int(input())
        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())
        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        ptr1 = llist1.head
        ptr2 = llist2.head

        # Move ptr1 to merge index
        for i in range(llist1_count):
            if i == index:
                break
            ptr1 = ptr1.next

        # Connect tail of list2 to merge node
        for i in range(llist2_count):
            if i == llist2_count - 1:
                llist2.tail.next = ptr1
            ptr2 = ptr2.next

        result = findMergeNode(llist1.head, llist2.head)
        fptr.write(str(result) + '\n')
