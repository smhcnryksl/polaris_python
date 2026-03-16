class Node():
    def __init__(self, state):
        self.state = state

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        return self.frontier.pop()


class QueueFrontier(StackFrontier):

    def remove(self):
        return self.frontier.pop(0)
