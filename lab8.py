
# Example of using sleep() function


import time

### sleep with 0.5second delay between print
import time
import random

from random import *
import time


class Snail:
   animlist = ["__~@", "_~_@", "__@"]
   name = ""
   speed = 0.0
   frame = 0
   pos = 0.0

   def __init__(self, name):
      assert len(name) <= 2, "Snail's initials must be 2 characters."
      self.name = name.upper()
      self.speed = randint(1, 10) / 10;
      self.frame = 0
      self.pos = 0.0

   def move(self):
      self.pos = self.pos + self.speed
      self.frame = self.frame + 1
      if self.frame > 2:
         self.frame = 0

   def getIntPos(self):
      return int(self.pos)

   def getName(self):
      return self.name

   def getStr(self):
      return self.getIntPos() * " " + self.animlist[self.frame] + (40 - self.getIntPos()) * " " + self.name


def getSnailList():
   ls = []
   n = int(input("How many snail do you want to race? "))
   for i in range(n):
      name = input("Snail " + str(i + 1) + " two initials: ")
      snl = Snail(name)
      ls.append(snl)
   return ls


def runRace(snaillist):
   input("Press enter to start race.")
   time_step = 1
   while True:
      print(40 * "-" + "Time " + str(time_step))
      flag = False
      winner = ""
      for sn in snaillist:
         print(sn.getStr())
         sn.move()
         if (sn.getIntPos() > 39):
            flag = True
            winner = sn.getName()
      time.sleep(0.2)
      if flag:
         print("Snail " + winner + " Won!")
         return
      else:
         time_step = time_step + 1


def main():
   print("Snail Race...")
   l = getSnailList()
   runRace(l)
   while (input("Play again (Y) ") == 'Y'):
      print("Snail Race...")
      l = getSnailList()
      runRace(l)


if __name__ == "__main__":
   main()

# print("0.5s delay")
# for i in range(5):
#    print(i)
#    sleep(0.5)
#
# print("0.2s delay")
# for i in range(5):
#    print(i)
#    sleep(0.2)
#
# print("No delay")
# for i in range(5):
#    print(i)
# from random import *
