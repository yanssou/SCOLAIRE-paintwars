# Projet "robotique" IA&Jeux 2021
#
# Binome:
#  Prénom Nom: Neïla KAMOUCHE
#  Prénom Nom: Yanis IKHENOUSSENE
import random 

cpt = 0

def get_team_name():
    return "X MEN" # à compléter (comme vous voulez)

def step(robotId, sensors):
    global cpt
    translation = 1 # vitesse de translation (entre -1 et +1)
    rotation = 0 # vitesse de rotation (entre -1 et +1)
    print("COMPTEUR : ",cpt)


    #pour front_left, front et left
    if sensors["sensor_front_left"]["distance"] < 1 or sensors["sensor_front"]["distance"] < 1 :
        #cas ou le robot a distance est dans l'equipe adverse pour front
        if sensors["sensor_front"]["isRobot"] == True and sensors["sensor_front"]["isSameTeam"] == False:
            #Division des iterations en 2
            if cpt < 8000:
                #1er partie de jeu on avance aleatoirement
                rotation = random.randint(-1,1)
            else:
                #2eme partie on suit l'adversaire
                rotation = (1) * sensors["sensor_front_left"]["distance"] + (-1) * sensors["sensor_front_right"]["distance"]
        
        #meme chose pour front left
        elif sensors["sensor_front_left"]["isRobot"] == True and sensors["sensor_front_left"]["isSameTeam"] == False:
            if cpt < 8000:
                rotation = random.randint(-1,1)           
            else:
                rotation = (1) * sensors["sensor_left"]["distance"] + (-1) * sensors["sensor_front"]["distance"]
        #sinon on tourne a 90deg
        else:
            rotation = 0.5  # rotation vers la droite
        
        


    #meme chose pour front_right et right
    elif sensors["sensor_front_right"]["distance"] < 1 :
        if sensors["sensor_front_right"]["isRobot"] == True and sensors["sensor_front_right"]["isSameTeam"] == False:
            if cpt < 8000:
                rotation = random.randint(-1,1)
            else:
                rotation = (1) * sensors["sensor_front"]["distance"] + (-1) * sensors["sensor_right"]["distance"]
        else:
            rotation = -0.5  # rotation vers la gauche
        
    
    if cpt >= 8000:
    #meme chose pour back right, back, back_left, left et right
        if sensors["sensor_back_right"]["distance"] < 1 or sensors["sensor_back"]["distance"] or sensors["sensor_back_left"]["distance"] < 1 or sensors["sensor_right"]["distance"] < 1 or sensors["sensor_left"]["distance"] < 1:
            if sensors["sensor_back_right"]["isRobot"] == True and sensors["sensor_back_right"]["isSameTeam"] == False:
                rotation = (1) * sensors["sensor_right"]["distance"] + (-1) * sensors["sensor_back"]["distance"]
        
            elif sensors["sensor_back"]["isRobot"] == True and sensors["sensor_back"]["isSameTeam"] == False:
                rotation = (1) * sensors["sensor_back_right"]["distance"] + (-1) * sensors["sensor_back_left"]["distance"]

            elif sensors["sensor_back_left"]["isRobot"] == True and sensors["sensor_back_left"]["isSameTeam"] == False:
                rotation = (1) * sensors["sensor_right"]["distance"] + (-1) * sensors["sensor_left"]["distance"]

            elif sensors["sensor_right"]["isRobot"] == True and sensors["sensor_right"]["isSameTeam"] == False:
                rotation = (1) * sensors["sensor_front_right"]["distance"] + (-1) * sensors["sensor_back_right"]["distance"]

            elif sensors["sensor_left"]["isRobot"] == True and sensors["sensor_left"]["isSameTeam"] == False:
                rotation = (1) * sensors["sensor_back_left"]["distance"] + (-1) * sensors["sensor_front_left"]["distance"]
            

        #on ne traite le reste car on ne rentre jamais dans un mur par l'arriere

    
    cpt+=1

    return translation, rotation
