def enqueue(queue, value):
    """Add a value to the rear of the queue."""
    queue.append(value)


def dequeue(queue):
    """Remove and return the value at the front of the queue."""
    if is_empty(queue):
        return -1
    return queue.pop(0)


def front(queue):
    """Return the value at the front without removing it."""
    if is_empty(queue):
        return -1
    return queue[0]


def rear(queue):
    """Return the value at the rear without removing it."""
    if is_empty(queue):
        return -1
    return queue[-1]


def size(queue):
    """Return the number of values in the queue."""
    return len(queue)


def is_empty(queue):
    """Return True when the queue has no values."""
    return len(queue) == 0


def display(queue):
    """Print the queue from front to rear."""
    if is_empty(queue):
        print("empty queue..")
        return

    for value in queue:
        print(value)


if __name__ == "__main__":
    queue = []
    enqueue(queue, 10)
    enqueue(queue, 20)
    enqueue(queue, 30)
    enqueue(queue, 40)

    print(f"dequeued element - {dequeue(queue)}")
    print(f"front element - {front(queue)}")
    print(f"rear element - {rear(queue)}")
    print(f"size of queue - {size(queue)}")
    display(queue)
