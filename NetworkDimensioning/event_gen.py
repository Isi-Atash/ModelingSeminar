import numpy as np
import numpy.random as rnd

def event_gen(n):
    events=[]
    for t in range(n):
        r=rnd.choice(range(10))
        if r<4:
            events.append([t,'bronze'])
        elif r<7:
            events.append([t,'silver'])
        elif r<8:
            events.append([t,'gold'])
    return events

if __name__ == "__main__":
    events = event_gen(2000)
    for event in events:
        print (event[0], event[1])

