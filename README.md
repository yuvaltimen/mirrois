#Mirrois
This is a puzzle game involving moving the Orb from the start 
to the end. The Orb emits light and will help illuminate walls
and other objects in the room that may serve as obstacles or as 
a means to reach the goal. 

There are poison mirrors that reflect the Orbs light and corrupts it.
If the Orb passes through a corrupted ray, you lose.  



===

App.py

ViewController of the game. This class handles passing user input
to the model, as well as rendering the view of the model at each time
frame.

Model.py

Contains the level details, and the state of the game. This includes
the level shape, layout, and obstacles, as well as the orb, including:
- whether the orb is picked up or not
- where the orb is
- should track the logic of the lighting, since gameplay depends on rays

