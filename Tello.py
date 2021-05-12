from djitellopy import Tello
import time

myDrone = Tello()
myDrone.connect()
myDrone.get_battery()
myDrone.takeoff()
time.sleep(4)
myDrone.move_up(40)
time.sleep(4)
myDrone.land()





