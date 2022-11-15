from graphics import *
import random


class Fish:
    """Definition for a fish with a body, eye, and tail"""

    def __init__(self, win, position):
        """constructs a fish made of 1 oval centered at `position`,
    a second oval for the tail, and a circle for the eye"""
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        self.direction = -1
        self.eye = None
        self.body = None
        self.tail = None
        self.make_fish(position)

    def make_fish(self, position):
        #####FISH BODY#####
        first_fish_body_p1 = Point(position.getX() - 40, position.getY() - 20)
        first_fish_body_p2 = Point(position.getX() + 40, position.getY() + 20)

        self.body = Oval(first_fish_body_p1, first_fish_body_p2)
        self.body.setFill(color_rgb(self.red, self.green, self.blue))

        #####FISH EYE#####
        first_fish_eye_c = Point(position.getX() + self.direction * 10, position.getY())

        self.eye = Circle(first_fish_eye_c, 4)
        self.eye.setFill("black")

        #####FISH TAIL#####
        first_fish_tail_p1 = Point(position.getX() + self.direction * -30, position.getY() * .5)
        first_fish_tail_p2 = Point(position.getX() + self.direction * -50, position.getY() * 1.5)

        self.tail = Oval(first_fish_tail_p1, first_fish_tail_p2)
        self.tail.setFill("black")

        # TODO: define the eye
        #       (later: as a function of the direction)

    def flip(self, win, position):
        """ """
        # TODO: undraw the whole fish, change its direction,
        #       reconstruct it (make_fish), and redraw it
        self.undraw()
        self.direction = self.direction * -1
        self.make_fish(position)
        self.draw(win)

    def undraw(self):
        """undraw the fish"""
        # TODO: undraw the fish
        self.body.undraw()
        self.eye.undraw()
        self.tail.undraw()
       

    def draw(self, win):
        """draw the fish to the window"""
        # TODO: draw the fish
        self.body.draw(win)
        self.eye.draw(win)
        self.tail.draw(win)
        

    def move(self, dx, dy=0):
        """move the fish by dx"""
        # TODO: move the fish
        #       (later: a child class could play with a dy)
        self.body.move(dx, dy)
        self.eye.move(dx, dy)
        self.tail.move(dx, dy)


# TODO: make child classes:
#       Goldfish and Snapper
#       NOTE: always call super fish! 
#       possible changes: 
#         size, color, shape, and 
#         tail and eye shape and color


class GoldFish(Fish):
  def __init__(self, win, position):
    
    Fish.__init__(self, win, position)
    self.make_second_fish(position)
    
  def make_second_fish(self, position):
    #####GOLDIE BODY#####
    goldie_body_p1 = Point(position.getX() - 50, position.getY() - 20)
    goldie_body_p2 = Point(position.getX() + 50, position.getY() + 20)

    self.body = Oval(goldie_body_p1, goldie_body_p2)
    self.body.setFill(color_rgb(self.red, self.green, self.blue))


    #####GOLDIE TAIL#####
    goldie_tail_p1 = Point(position.getX() + self.direction * - 45, position.getY() + 8)
    goldie_tail_p2 = Point(position.getX() + self.direction * - 65, position.getY()+ 20)
    goldie_tail_p3 = Point(position.getX() + self.direction * - 62, position.getY())
    goldie_tail_p4 = Point(position.getX() + self.direction* - 65, position.getY() - 20)
    goldie_tail_p5 = Point(position.getX() + self.direction* - 45, position.getY() -8)

    self.tail = Polygon( goldie_tail_p1, goldie_tail_p2, goldie_tail_p3, goldie_tail_p4, goldie_tail_p5,)
    self.tail.setFill("gold")
    

    #####GOLDIE FIN#####
    goldie_fin_p1 = Point(position.getX() + self.direction - 20, position.getY() - 35)
    goldie_fin_p2 = Point(position.getX() + self.direction - 30 , position.getY()- 10)
    goldie_fin_p3 = Point(position.getX() + self.direction + 30, position.getY() - 10)
    goldie_fin_p4 = Point(position.getX() + self.direction + 35, position.getY() -25)

    self.fin = Polygon( goldie_fin_p1, goldie_fin_p2, goldie_fin_p3, goldie_fin_p4 )
    self.fin.setFill("gold")


    #####GOLDIE EYE#####
    goldie_eye_c = Point(position.getX() + self.direction * 30, position.getY() - 5)

    self.eye = Circle(goldie_eye_c, 4)
    self.eye.setFill("black")
  
  def flip(self, win, position):
    self.undraw()
    self.direction = self.direction * -1
    self.make_second_fish(position)
    self.draw(win)
    
  def undraw(self):
    self.fin.undraw()
    self.body.undraw()
    self.eye.undraw()
    self.tail.undraw()
       

  def draw(self, win):
    self.fin.draw(win)
    self.body.draw(win)
    self.tail.draw(win)
    self.eye.draw(win)

  def move(self, dx):
    self.fin.move(dx, 0)
    self.body.move(dx, 0)
    self.eye.move(dx, 0)
    self.tail.move(dx, 0)
  
    pass


class Snapper(Fish):
  def __init__(self, win, position):
    
    Fish.__init__(self, win, position)
    self.make_third_fish(position)

  def make_third_fish(self, position):
    
    #####SNAPPER BODY#####
    snapper_body_p1 = Point(position.getX() - 35, position.getY() - 10)
    snapper_body_p2 = Point(position.getX() + 35, position.getY() + 10)

    self.body = Oval(snapper_body_p1, snapper_body_p2)
    self.body.setFill(color_rgb(self.red, self.green, self.blue))
    
    
    #####SNAPPER TAIL#####
    first_fish_tail_p1 = Point(position.getX() + self.direction * -35, position.getY() - 25)
    first_fish_tail_p2 = Point(position.getX() + self.direction *-49 , position.getY() + 25)

    self.tail = Oval(first_fish_tail_p1, first_fish_tail_p2)
    self.tail.setFill("black")
    

    #####SNAPPER EYE#####
    snapper_eye_c = Point(position.getX() + self.direction * 20, position.getY() - 5)

    self.eye = Circle(snapper_eye_c, 5)
    self.eye.setFill("black")

  def flip(self, win, position):
    self.undraw()
    self.direction = self.direction * -1
    self.make_third_fish(position)
    self.draw(win)
  
  def draw(self, win):
    self.body.draw(win)
    self.tail.draw(win)
    self.eye.draw(win)

  def move(self, dx, dy):
    self.body.move(dx, dy)
    self.eye.move(dx, dy)
    self.tail.move(dx, dy)
    
  pass

class Betta (Fish):
  def __init__(self, win, position):
    
    Fish.__init__(self, win, position)
    self.make_fourth_fish(position)

  def make_fourth_fish(self, position):
    
    #####betta BODY#####
    betta_body_p1 = Point(position.getX() - 35, position.getY() - 10)
    betta_body_p2 = Point(position.getX() + 35, position.getY() + 10)

    self.body = Oval(betta_body_p1, betta_body_p2)
    self.body.setFill(color_rgb(self.red, self.green, self.blue))
    
    #####BETTA FIN ####

    betta_fin_p1 = Point(position.getX() + self.direction * - 5, position.getY() - 10)
    betta_fin_p2 = Point(position.getX() + self.direction * - 15, position.getY() - 30)
    betta_fin_p3 = Point(position.getX() + self.direction * - 25, position.getY() - 15)
    betta_fin_p4 = Point(position.getX() + self.direction* - 35, position.getY() - 30)
    betta_fin_p5 = Point(position.getX() + self.direction* - 40, position.getY()- 15)
    betta_fin_p6 = Point(position.getX() + self.direction* - 55, position.getY() - 15)
    betta_fin_p7 = Point(position.getX() + self.direction* - 45, position.getY())
    betta_fin_p8 = Point(position.getX() + self.direction* - 65, position.getY() + 15)
    betta_fin_p9 = Point(position.getX() + self.direction* - 35, position.getY()+ 10)

    self.fin = Polygon( betta_fin_p1, 
    betta_fin_p2, 
    betta_fin_p3, 
    betta_fin_p4, 
    betta_fin_p5,betta_fin_p6, betta_fin_p7, betta_fin_p8, betta_fin_p9
    )
    self.fin.setFill("red")
    

    #####betta TAIL#####
    betta_tail_p1 = Point(position.getX() + self.direction - 10, position.getY() + 25)
    betta_tail_p2 = Point(position.getX() + self.direction - 20 , position.getY()+ 5)
    betta_tail_p3 = Point(position.getX() + self.direction + 25, position.getY() + 5)
    betta_tail_p4 = Point(position.getX() + self.direction + 35, position.getY() +15)

    self.tail = Polygon( betta_tail_p1, betta_tail_p2, betta_tail_p3, betta_tail_p4 )
    self.tail.setFill("red")
    

    #####betta EYE#####
    betta_eye_c = Point(position.getX() + self.direction * 20, position.getY() - 5)

    self.eye = Circle(betta_eye_c, 7)
    self.eye.setFill("black")

  def flip(self, win, position):
    self.undraw()
    self.direction = self.direction * -1
    self.make_fourth_fish(position)
    self.draw(win)
    
  def undraw(self):
    self.fin.undraw()
    self.body.undraw()
    self.eye.undraw()
    self.tail.undraw()
       

  def draw(self, win):
    self.fin.draw(win)
    self.tail.draw(win)
    self.body.draw(win)
    self.eye.draw(win)

  def move(self, dx,dy):
    self.fin.move(dx, dy)
    self.body.move(dx, dy)
    self.eye.move(dx, dy)
    self.tail.move(dx, dy)
  
    pass


