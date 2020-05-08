#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}

    # loop to create cache
    for ticket in tickets:
        cache[ticket.source] = ticket.destination

    # set variables for constructing route
    route = [None] * length
    prev = "NONE"

    # iterate through tickets and assign them to route[i] by using cache,
    # put prev in route, then set prev to the next node
    for i in range(length):
        route[i] = cache[prev]
        prev = cache[prev]

    return route
