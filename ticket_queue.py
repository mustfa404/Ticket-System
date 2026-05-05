from collections import deque


class TicketQueue:
    def __init__(self):
        self.queue = deque()
        self.tickets = {}
        self.ticket_counter = 0

    def add_customer(self, *names):
        for name in names:
            self.queue.append(name)

    def issue_all_tickets(self):
        while self.queue:
            self.ticket_counter += 1
            name = self.queue.popleft()  # FIFO order
            self.tickets[self.ticket_counter] = name

    def cancel_ticket(self, name):
        if name in self.queue:
            self.queue.remove(name)
        else:
            raise ValueError(f"{name} is not in the queue.")

    def display_queue(self):
        return list(self.queue)

    def display_tickets(self):
        return self.tickets

    def __len__(self):
        return len(self.queue)
