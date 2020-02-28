from doubly_linked_list import DoublyLinkedList

# the oldest element in the ring buffer is overwritten with the newest element.
# works like a queue system: FIFO
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # create head if empty
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        # insert new at tail if not at capacity
        elif self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            # link to tail, creating "ring"
            self.storage.tail.next = self.storage.head
        else:
            # overwrite current value, starting with head
            self.current.value = item
            # move forward to next oldest values
            self.current = self.current.next

        # if self.storage.length < self.capacity:
        #     self.storage.add_to_tail(item)
        #     self.current = self.storage.head
        #     self.storage.tail.next = self.storage.head
        # # overwrite
        # elif self.current is self.storage.head:
        #     self.storage.remove_from_tail()
        #     self.storage.add_to_tail(item)
        #     self.current = self.current.next
        # elif self.current is self.storage.head:
        #     self.storage.remove_from_head()
        #     self.storage.add_to_head(item)
        #     self.current = self.storage.head
        # else:
        #     self.current.insert_before(item)
        #     self.current.delete()
        #     self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # should not return any None values, even if present in ring buffer
        current = self.storage.head
        while True:
            list_buffer_contents.append(current.value)
            if current is self.storage.tail:
                break
            else:
                current = current.next
        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

