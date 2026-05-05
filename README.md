#  Ticket Queue System

A simple desktop application for managing a customer ticket queue, built with Python and Tkinter.

## Features

- Add one or multiple customers to the queue at once
- Issue tickets to all customers in the queue
- Cancel a specific customer's ticket
- Live display of the current queue and issued tickets

## Requirements

- Python 3.x (Tkinter is included in the standard library)

## Usage

```bash
python ticket_queue.py
```

### How it works

1. **Add customers** — Type one or more comma-separated names and click *Add Customer(s)*
2. **Issue tickets** — Click *Issue All Tickets* to assign tickets to everyone in the queue
3. **Cancel a ticket** — Type a customer's name and click *Cancel Ticket* to remove them from the queue

## Project Structure

```
ticket_queue.py
│
├── TicketQueue       # Core queue logic (add, issue, cancel)
└── TicketQueueGUI    # Tkinter interface
```

## Known Limitations

- `issue_all_tickets()` uses `pop()` (LIFO), so tickets are issued in reverse order of arrival
- Data is not persisted between sessions
