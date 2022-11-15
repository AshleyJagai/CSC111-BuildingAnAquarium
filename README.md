# CSC111-BuildingAnAquarium


\[This assignment was created by Alicia Grubb and Shinyoung Cho\]

### Step 1: Different Kinds of Fish

Our simple `Fish` class in `fish.py` we drew in lecture is made up of just two ovals and a circle:

![Fish](img/fish.png)

* Extend the `Fish` class to create **more than two** child classes to draw different kinds of fish. For example, you might consider using `Polygon` objects to give them some more exciting fin shapes, like this:

![Cool Fish](img/coolFish.png)

* A different kind of fish might behave and look different from the other kinds. Perhaps it only swims in the bottom or top half of the tank, or it primarily swims from top to bottom.
* Use multiple classes (e.g., `DabFish`) to store your visual objects and use inheritance (e.g., `class DabFins(Fish)`) to have special kinds of fish and basic fish.

---

### Step 2: Direction 
* Augment your `Fish` class so that you can make fish facing either LEFT and RIGHT (you may want to add a `direction` input to the __init__ method).

---

### Step 3: Swimming Fish

* We’ll start by just having the fish swim in a straight line. Call the `.move()` method repeatedly on each of the fish you created in your `main.py` file to make them swim across the screen. 
* Consider having fish that travel at different speeds to make it more interesting!
 
---

### Step 4: Different patterns of swimming 
* Modify the `.move()` method in the `Fish` class to get your fish to bob up and down instead of swimming in a straight line.
* Make your fish turn around (flip) when it hits the edge of the screen and start swimming the other direction.

---

### Step 5: More objects (some plants, etc.)

* Add **one** or more extra objects (below).

#### Optional Extra Objects:

 * Add some decorations (a castle, some plants, etc.). Plants that sway in the background?
 * Add small bubbles, floating from the bottom of the screen to the top.
 * Add Sharks that eat the fish.
 * Add a background, such as the one provided [here](https://commons.wikimedia.org/wiki/File:Underwater_world.jpg).
 * Make it so that when the user clicks the screen or on a keyboard shortcut a new fish is added. You could use different letters to add each kind of fish.
 * Create your own optional extra feature.

---

### Step 6: The End 
* Safely exit the aquarium when user is done (either keyboard click or mouse click, your choice).

Once you have completed Steps 1-6, review the list of features below to ensure your aquarium visualization is complete.

---

## Grading criteria (10 points)

*Note: This is an individual assignment*

### Submission Instructions

The program MUST compile and follow the instructions in this Readme.
The program will be checked for completeness and style.
<!-- We will use unit testing to evaluate your code in this assignment. Replace `Alicia Grubb` with your (and your partner) name(s) on the first line of the submissions, then again put them in the header below. The first line must only contain a comment with your name(s).

You can test your code by pressing the `Run` button. Once you are happy with it, uncomment the `MODE = "SUBMIT"` line and comment out `MODE = "TEST"`, and press the `Run` button once, then press `Submit`. -->

*Points will be deducted for not following these instructions.*


### Style points (3 points):
The submission:

* includes the complete course header
* uses appropriate, informative variable names
* has inline comments, and descriptions of each function and class 
* includes all files required to run your assignment
* the main() should be located in a files called `main.py`
* runs without syntax errors

### Operations (7 points):
The program includes each of the required features in each step (see complete list below). Programs will be evaluated based on code quality and the quality of the visualization.

Required Features:

 * Modify the `.move()` method in the `Fish` class to get your fish to bob up and down instead of swimming in a straight line.
 * Augment your `Fish` class so that you can make fish facing either LEFT and RIGHT (you may want to add a `direction` input to the `__init__` method).
 * Make your fish turn around (flip) when it hits the edge of the screen and start swimming the other direction.
 * Add a third kind of fish that behaves and looks different from the first two. Perhaps it only swims in the bottom or top half of the tank, or it primarily swims from top to bottom.
 * Use multiple classes to store your visual objects and use _inheritance_ to have special kinds of fish and basic fish.
 * Safely exit the aquarium when user is done (either keyboard click or mouse click, your choice).
 * Add **one** or more of the extra features (below).

Optional Extra Features:

 * Add some decorations (a castle, some plants, etc.). Plants that sway in the background?
 * Add small bubbles, floating from the bottom of the screen to the top.
 * Add Sharks that eat the fish.
 * Add a background, such as the one provided [here](https://commons.wikimedia.org/wiki/File:Underwater_world.jpg).
 * Make it so that when the user clicks the screen or on a keyboard shortcut a new fish is added. You could use different letters to add each kind of fish.
 * Create your own optional extra feature.
