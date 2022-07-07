# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Thomas Hebert
#  Prénom Nom: Vasiliki Eirini Kalogirou

from pyroborobo import Pyroborobo, Controller, AgentObserver, WorldObserver, CircleObject, SquareObject, MovableObject
# from custom.controllers import SimpleController, HungryController
import numpy as np
import random

import paintwars_arena

def get_team_name():
    return "Midnight Suns" # à compléter (comme vous voulez)

def step(robotId, sensors):

    # senseurs étendus
    def get_extended_sensors(sensors):
        for key in sensors:
            sensors[key]["distance_to_robot"] = 1.0
            sensors[key]["distance_to_wall"] = 1.0
            if sensors[key]["isRobot"] == True:
                sensors[key]["distance_to_robot"] = sensors[key]["distance"]
            else:
                sensors[key]["distance_to_wall"] = sensors[key]["distance"]
        return sensors
    
    sensors = get_extended_sensors(sensors)
    
    # comportements Braitenberg
    def hateWall():
        translation = 1
        rotation = (-1) * sensors["sensor_front_left"]["distance_to_wall"] + (1) * sensors["sensor_front_right"]["distance_to_wall"] + (-1) * sensors["sensor_left"]["distance_to_wall"] + sensors["sensor_right"]["distance_to_wall"]
        return translation, rotation
    
    def loveBot():
        translation = 1
        rotation = 1 * sensors["sensor_front_left"]["distance_to_robot"] + (-1) *sensors["sensor_front_right"]["distance_to_robot"]
        return translation, rotation
    
    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)

    # si on croise un robot allié on l'évite
    if (sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == True) or (sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == True)\
    or (sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == True) or (sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == True)\
    or (sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == True):
        rotation = random.uniform(-1, 1)
        return translation, rotation

    # si on croise un ennemi on le poursuit
    elif (sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False) or (sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False)\
    or (sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False) or (sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == False)\
    or (sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == False):
        return loveBot()
    
    # si on croise un chemin on le suit
    elif (sensors["sensor_right"]["distance_to_wall"] < 1 and sensors["sensor_front_right"]["distance"] == 1)\
    and (sensors["sensor_left"]["distance_to_wall"] < 1 and sensors["sensor_front_left"]["distance"] == 1):
        if sensors["sensor_front"]["distance_to_wall"] == 1:
            rotation = random.choice([-0.25, 0, 0.25])
        else:
            rotation = random.choice([-0.25, 0.25])
        return translation, rotation
    
    elif sensors["sensor_right"]["distance_to_wall"] < 1 and sensors["sensor_front_right"]["distance"] == 1:
        if sensors["sensor_front"]["distance_to_wall"] == 1:
            rotation = random.choice([0, 0.25])
        else:
            rotation = 0.25
        return translation, rotation
    
    elif sensors["sensor_left"]["distance_to_wall"] < 1 and sensors["sensor_front_left"]["distance"] == 1:
        if sensors["sensor_front"]["distance_to_wall"] == 1:
            rotation = random.choice([0, -0.25])
        else:
            rotation = -0.25
        return translation, rotation
    
    # on esquive les murs devant
    elif sensors["sensor_front"]["distance_to_wall"] < 1:
        rotation = random.choice([-1, 1])
        return translation, rotation 
    
    # on évite les murs avec le comportement de braitenberg
    else:
        return hateWall()
