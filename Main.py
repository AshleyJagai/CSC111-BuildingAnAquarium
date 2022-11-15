# --------------------------------------------------------
#        Name: <YOUR NAME HERE>
# Course Info: CSC111 - Fall 2021
# Description: Assignment07: Aquarium
#        Date: <TODAY'S DATE HERE>
# --------------------------------------------------------

from graphics import *
from fish import *


def main():
  width = 550
  height = 350
  win = GraphWin("Aquarium", width, height)
  bg = Image(Point(width / 2, height / 2), "img/aquarium_bg.gif")
  bg.draw(win)
  # TODO: step 1
  first_fish = Fish(win, Point(400, 50))
  first_fish.draw(win)
  # TODO: step 2
  # draw different kinds of fish
  

  betta = Betta(win, Point(340, 175))
  p_fish = betta.body.getCenter()
  betta.flip(win, p_fish)
  
  
  goldie = GoldFish(win, Point(50, 250)) 
  p_fish = goldie.body.getCenter()
  goldie.draw(win)
  goldie.flip(win, p_fish)

  snapper = Snapper(win,Point(540, 175))
  p_fish = snapper.body.getCenter()
  snapper.draw(win)
 
  
  
  t = print(input("press r to show a random fish! "))
  if t == "r":
    betta.draw(win, Point(340, 175))
  

  

  

  ##############################################
  # TODO: step 3
  ##############################################
  # start animation loop; make your fish move
  # at different speeds
  # some delta x and delta y values
  delta_x = - width / 2000
  delta_x2 = width / 1500
  delta_x3 = - width / 2000
  delta_x4 =  width / 2000
  delta_y =  -height / 2000
  delta_y2 =  height / 1500
  
  while win.checkMouse() is None:
    # move all fish
    first_fish.move(delta_x)
    goldie.move(delta_x2)
    betta.move(delta_x4, delta_y2 )
    snapper.move(delta_x3, delta_y)

    p_fish = first_fish.body.getCenter()
    if p_fish.getX() <= 0 or p_fish.getX() >= width:
      first_fish.flip(win, p_fish)
      delta_x = delta_x * -1
    
    p_fish = goldie.body.getCenter()
    if p_fish.getX() <= 0 or p_fish.getX() >= width:
      goldie.flip(win, p_fish)
      delta_x2 = delta_x2 * -1  

    p_fish = snapper.body.getCenter()
    if p_fish.getX() <= 0 or p_fish.getX() >= width:
      snapper.flip(win, p_fish)
      delta_x3 = delta_x3 * -1   
    if p_fish.getY() <= 0 or p_fish.getY() >= height:
      # goldie.flip(win, p_fish)
      delta_y = delta_y * -1    
    
    p_fish = betta.body.getCenter()
    if p_fish.getX() <= 0 or p_fish.getX() >= width:
      betta.flip(win, p_fish)
      delta_x4 = delta_x4 * -1   
    if p_fish.getY() <= 0 or p_fish.getY() >= height:
      # goldie.flip(win, p_fish)
      delta_y2 = delta_y2 * -1 
    


     
      
  
    


if __name__ == "__main__":
  main()
