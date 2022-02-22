# Event-driven programming

Programming styles
------------------

Batch-oriented programming style:

* Program flows in a preplanned way
* It may wait for input from the user

Event-driven programming:

* Program decides what to do next based on events that occur (mouse clicks, keyboard inputs, timers, communication over networks...)
* Graphical user interfaces (GUI) are often programmed using event-driven programming

Event-driven programming:
-------------------------

Not a part of object-oriented programming, but can be seen in OO programs:

* Useful way to write many programs (GUI...)
* Objects are useful for modeling events and event handlers


Basics of event-driven programming
----------------------------------

You have already used an example. PyGame main loops use event-driven programming:

```python
while not finished:
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
    ...
```

`pygame.event.get()` fetches all events that have happened since the last call. Returns a sequence of events.

## Glossary 

**event** 
- Signal to the program that something has happened. It can be some user action (mouse movements/clicks, keypresses), internal timer, network packets arriving etc.

Events are often represented as objects in OO systems. This provides
several useful properties, including:
- The type of the event object can be used to decide how to handle it.
- The objects can contain additional information about the event (ex: which key was pressed)
- Events may have methods that can be useful for handling them.
- Subclassing can be used to provide events with additional attributes and methods

**handler**
- A function or object that is called in response to an event.

**bind**
- bind a function/object (or associate it) with an event. So if the event occurs, the function/object is called to handle it (see *handler*)

**Example with turtle**

```python
import turtle

class TurtleWithEvents(turtle.Turtle):
    def __init__(self,wnd):
         super().__init__()
         self._wnd=wnd
        
    #Handlers
    def moveforward(self):
        self.forward(20)
        
    def rotateleft(self):
        self.left(45)
        
    def rotateright(self):
        self.right(45)
    
    def mouseClick(self,x,y):
        self.goto(x,y)        
    
    def quitting(self):
        self._wnd.bye()
    
    def bindHandlersToEvents(self):
        self._wnd.onkey(self.rotateleft,"Left")
        self._wnd.onkey(self.rotateright,"Right")
        self._wnd.onkey(self.moveforward,"Up")
        self._wnd.onkey(self.quitting,"q")
        self._wnd.onclick(self.mouseClick) #onclick returnerer x,y

def main():
    #Setter vindusstørrelsen
    turtle.setup(600,800)
    #Henter referansen til vinduet
    window = turtle.Screen()
    window.title("Events with keypresses!")
    window.bgcolor("#FF00FF")
   
    rune = TurtleWithEvents(window)
    rune.bindHandlersToEvents()
    
    #Vi forteller vinduet at det skal lytte etter hendelser
    window.listen()
    window.mainloop()

main()
```

**Excerice**
Add some new key bindings to the example above.
- R,G or B should change the arrow color to Red, Green or Blue (Hint: use color() on the turtle object)
- The keys * and - should increase/decrease the width of the pen (min value 1 and max 20). (Hint: use pensize() to get and set the pensize on the turtle object).

## Event queues
One important property is that the part that creates the event does not necessarily need to know where or how the event is handled. The triggering, or firing, of events is disconnected from the handling of events.

To do this, it's useful to have an event queue. The queue is somewhere to store events (for the part of the program that fires off events) and a place to retrieved queued events (for the part that handles events).

A simplified event queue:
```python
class EventQueue:
    def __init__(self):
        self.__queue = []
    def add(self, event):
        """Adds an event to the queue."""
        self.__queue.append(event)
    def get(self):
        """Removes all events from the queue and returns a list of the removed events."""
        events = self.__queue
        self.__queue = []
        return events
```
In PyGame, the event queue is handled internally in PyGame:

```pygame.event.get()``` transfers control over to PyGame. It:

- Does bookkeeping and detects new events
- Stores new events on an event queue (temporarily)
- Removes and returns the events as a sequence

## Event handling
Determining the type of event and responding with appropriate action is called event handling:
```python
for event in pygame.event.get():
    if event.type == QUIT:
        finished = True
```
Events can also be handled by event-handlers. These can be implemented as functions or objects.

Determining which handler to call is called dispatching:
```python
for event in pygame.event.get():
    if event.type == FOO:
        # event handler function
        foo_handler(event)
    if event.type == BAR:
        # calling handle() method on object
        bar_handler.handle(event)
```
**Example pygame**

```python
import pygame

def main():
    #initialisere pygame
    pygame.init()
    pygame.display.set_caption("Event testing")
    pygame.display.set_mode((400,600))
    
    running = True
    while running:
        #Event handling, henter event dersom det ligger noen i køen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                #Skriver ut hvilken event som er blitt trigget, både tallet og navnet til eventen
                print("En event ble oppdaget.. ", event.type,pygame.event.event_name(event.type))
    #Ute av løkken og vi avslutter
    pygame.quit()
main()
```
print to console:
```
En event ble oppdaget..  1024 MouseMotion
En event ble oppdaget..  1024 MouseMotion
En event ble oppdaget..  1024 MouseMotion
En event ble oppdaget..  32768 ActiveEvent
En event ble oppdaget..  32784 WindowLeave
En event ble oppdaget..  32787 WindowClose
```
## Event dispatchers

![Dispatcher](https://user-images.githubusercontent.com/97092780/155102375-bc88d53d-6a31-40f0-90f7-8bf631eb2638.png)
(https://en.wikipedia.org/wiki/Dispatcher#/media/File:PCPOST_Crew_Dispatcher.png)

A dispatcher routes events to event handlers. Can be implemented as an object. A simple example:

```python
class Dispatcher:
    def __init__(self):
        self.__handlers = {}

    def register_handler(self, etype, handler):
        self.__handlers[etype]=handler

    def dispatch(self, event):
        if event.type in self.__handlers:
            self.__handlers[event.type](event)
        else:
            print("Du glemte å registrere en handler for", event.type, pygame.event.event_name(event.type))
```
Using it with PyGame code:
```python
#Handlers
def mouse_motion_handler(event):
    print("moving mouse",event.pos)
    
def key_handler(event):
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_a]:
        print("You pressed the a-button!")
        pygame.draw.line(screen,(0,0,255),(10,10),(100,100),5)
     
        
    if key_input[pygame.K_q]:
        print("You pressed q-button and goodbye...")
        pygame.quit()
        sys.exit(0)
#main    
def main():
    global screen #Know what you are doing...
    pygame.init()
    pygame.display.set_caption("Event testing with dispatcher")
    screen=pygame.display.set_mode((400,600),0,32)
    #Create a dispatcher, ready for action
    dispatcher=Dispatcher()
    dispatcher.register_handler(pygame.MOUSEMOTION, mouse_motion_handler)
    dispatcher.register_handler(pygame.KEYDOWN,key_handler)

    running=True
    while running:
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                running=False
            else:
                dispatcher.dispatch(event)
                pygame.display.flip()
    pygame.quit()
main()
```

**Small excerice**
Add an handler that register when we click a button on the mouse on the screen. It should print to console "you clicked the left button" when you click the left mouse button, and "you clicked the right button" if you click the right mouse button and "you clicked something unknow.." for all the others buttons on the mouse.
HINT: Use ```event.button``` to get which button that is pressed down. 

## Why event dispatchers and handlers?
Extensible concept: users can extend program by adding handlers to dispatcher.

No need to modify event dispatcher source code to add new event types.

## Generating events
- Event-based systems often provide a method for adding events to the event queue.
- This lets users add new event types to programs as well as handlers.
- NB: Can also be used for scripted testing.
- In PyGame, this is done using ```pygame.event.post```

## Common event types in PyGame
Mouse events:
- ```event.pos```: xy-position that the mouse moved to
- ```event.rel```: relative motion since last event
- ```event.button```: state of buttons when the event was created

Keyboard events:
- KeyDown (when a key is pressed) and KeyUp (when the key is released)
- The event contains information about the key pressed and modifiers (shift, alt etc.)

## Timer events
Timers are events that are set to fire off after a certain amount of time. Can be one-shot or periodic. PyGame timers are periodic, and fire off an event of a specified type every N milliseconds.
```python
# fires an event of type MY_EVENT (USEREVENT+1) every 2000 milliseconds
MY_EVENT = USEREVENT+1
pygame.time.set_timer(MY_EVENT, 2000)
```
Example use: periodic update of information, such as the arms of a clock.

## Event-driven programming problems
Allowing handlers to change state: requires access to the state. (Example: variable in object or method). Some solutions:

- Global variables
- Default params to functions
- Storing state or methods in event handler objects

### Links
- [Wikipedia: Event-driven programmering](https://en.wikipedia.org/wiki/Event-driven_programming)
- [Turtle documentation](https://docs.python.org/3/library/turtle.html)
- [Pygame events documentation](https://www.pygame.org/docs/ref/event.html)
