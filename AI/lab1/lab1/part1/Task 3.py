import Lab1_Agents_Task1_World as World
import vrep, math, time, random
import random
import time
# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))

def imp2():
    global motorSpeed
    global L
    global R
    L = World.getSensorReading("ultraSonicSensorLeft")
    R = World.getSensorReading("ultraSonicSensorRight")
    l = World.getSensorReading("energySensor")
    print(World.getSensorReading("energySensor"))
    if ((L < 0.15) or (R < 0.15)):
        # print ("Turning for a bit...",)
        motorSpeed = dict(speedLeft=4, speedRight=-4)
        World.execute(motorSpeed, 1000, -1)
        World.normaliseAngle(l["direction"])
        World.collectNearestBlock()
    elif R < 0.3:
        World.normaliseAngle(l["direction"])
        World.collectNearestBlock()
        motorSpeed = dict(speedLeft=2, speedRight=3)
        World.execute(dict(motorSpeed), 1000, -1)

    elif R < 0.5:
        World.normaliseAngle(l["direction"])
        World.collectNearestBlock()
        motorSpeed = dict(speedLeft=3, speedRight=5)
        World.execute(dict(motorSpeed), 800, -1)
    elif L < 0.3:
        World.normaliseAngle(l["direction"])
        World.collectNearestBlock()
        motorSpeed = dict(speedLeft=3, speedRight=2)
        World.execute(dict(motorSpeed), 1000, -1)

    elif L < 0.5:
        World.normaliseAngle(l["direction"])
        World.collectNearestBlock()
        motorSpeed = dict(speedLeft=5, speedRight=3)
        World.execute(dict(motorSpeed), 1000, -1)

    if (World.normaliseAngle(l["direction"]) > 0 and (R > 0.4)):
        motorSpeed = dict(speedLeft=4, speedRight=3.3)
        World.execute(dict(motorSpeed), 200, -1)
        World.collectNearestBlock()
    elif (World.normaliseAngle(l["direction"]) < 0 and (R > 0.4)):
        motorSpeed = dict(speedLeft=3.3, speedRight=4)
        World.execute(dict(motorSpeed), 200, -1)
        World.collectNearestBlock()
    else:
        motorSpeed = dict(speedLeft=4.5, speedRight=4.5)
        World.collectNearestBlock()
    World.setMotorSpeeds(motorSpeed)


def imp3():
    global t
    global motorSpeed
    global L
    global R
    t = time.time()
    t= t % 1000
    print(t)
    L = World.getSensorReading("ultraSonicSensorLeft")
    R = World.getSensorReading("ultraSonicSensorRight")
    l = World.getSensorReading("energySensor")
    World.getSensorReading("energySensor")
    if ((L < 0.15) or (R < 0.15) and (t - (time.time() % 1000) ) > 10):
        t = ((time.time()) % 1000)
        print("new time:", t)
        motorSpeed = dict(speedLeft=4, speedRight=-4)
        World.execute(motorSpeed, 1000, -1)

        World.collectNearestBlock()

    elif (R < 0.5) and (t - (time.time()) > 100):
        t = ((time.time()) % 1000)
        print("new time:", t)

        World.collectNearestBlock()
        motorSpeed = dict(speedLeft=3, speedRight=5)
        World.execute(dict(motorSpeed), 800, -1)

    elif (L < 0.5) and (t - (time.time()) > 00):
        t = ((time.time()) % 1000)
        print("new time:" , t)
        World.normaliseAngle(l["direction"])
        World.collectNearestBlock()
        motorSpeed = dict(speedLeft=5, speedRight=3)
        World.execute(dict(motorSpeed), 1000, -1)

    if (World.normaliseAngle(l["direction"]) > 0 and (R > 0.4)):
        motorSpeed = dict(speedLeft=4, speedRight=3.3)
        World.execute(dict(motorSpeed), 400, -1)
        cond=World.collectNearestBlock()




    elif (World.normaliseAngle(l["direction"]) < 0 and (R > 0.4)):
        motorSpeed = dict(speedLeft=3.3, speedRight=4)
        World.execute(dict(motorSpeed), 400, -1)
        World.collectNearestBlock()

    World.setMotorSpeeds(motorSpeed)


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

    imp3()
