# Make sure to have the server side running in V-REP:
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
from typing import Type

import Lab1_Agents_Task1_World as World
import random
# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))
def imp():
    global motorSpeed
    if simulationTime<10000:
        motorSpeed = dict(speedLeft=random.random(), speedRight=random.random())
        #print(motorSpeed)
    elif simulationTime<20000:
        motorSpeed = dict(speedLeft=random.randrange(1,3,1), speedRight=random.randrange(1,3,1))
        #print(motorSpeed)
    elif simulationTime<30000:
            print ("Turning for a bit...",)
            World.execute(dict(speedLeft=random.randrange(1,2,1), speedRight=-random.randrange(1,2,1)),1500,-1)
            print ("... got dizzy, stopping!")
            print ("BTW, nearest energy block is at:",World.getSensorReading("energySensor"))
    else:

           motorSpeed = dict(speedLeft=random.randrange(1,5,2), speedRight=random.randrange(1,5,2))
           #print(motorSpeed)
           ########################################
           # Action Phase: Assign speed to wheels #
           ########################################
           # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)

    # try to collect energy block (will fail if not within range)
    if simulationTime%10000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())

def imp1():
    global motorSpeed
    if simulationTime<16500:
        motorSpeed = dict(speedLeft=3, speedRight=3)
        #print(motorSpeed)
    elif simulationTime < 22000:
            motorSpeed = dict(speedLeft=3, speedRight=4)
            #print(motorSpeed)
    # elif simulationTime<30000:
    #         print ("Turning for a bit...",)
    #         World.execute(dict(speedLeft=random.randrange(1,2,1), speedRight=random.randrange(1,2,1)),1500,-1)
    #         print ("... got dizzy, stopping!")
    #         print ("BTW, nearest energy block is at:",World.getSensorReading("energySensor"))
    else:

           motorSpeed = dict(speedLeft=3, speedRight=3)
           #print(motorSpeed)
           ########################################
           # Action Phase: Assign speed to wheels #
           ########################################
           # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    # try to collect energy block (will fail if not within range)
    if simulationTime%2000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())


while robot: # main Control loop
    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################
    simulationTime = World.getSimulationTime()
    if simulationTime%1000==0:
        # print some useful info, but not too often
        print ('Time:',simulationTime,\
               'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
               "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"))

    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################

    imp1()


