DirectionstotheRoomofLaughter = ("Left","Right","Left","Left","Left","Right")
DirectionstoMsBigheadsLab = ("Right","Left","Left","Left","Right","Left")
DirectionstoAmniacLab = ("Left","Right","Right","Left","Left","Left")

Name = input("What is your name" + "\n")
directions = [ DirectionstotheRoomofLaughter , DirectionstoMsBigheadsLab , DirectionstoAmniacLab ]
cyclenumber = 1

list_rooms =['Room of Laughter',"Ms.Bighead's","Amniac Lab"]

def cycle1():
    while cyclenumber<=3:
        if cyclenumber == 1:
            LabNum = input("What lab will you be visiting, 02, 03, 04" + "\n")
        elif cyclenumber == 2:
            LabNum = input("Specify which lab you will be visiting, 07, 24, 02" + "\n")
        elif cyclenumber == 3:
            LabNum = input("For the last time, tell which lab you will be visiting, 07, 24, 02" + "\n")
        if LabNum not in range(1,3):
             print ("That is not a listed lab")
        else:
            print("Ok " + Name + " These are the directions to" + list_rooms[int(LabNum)-1] + "\n" + d[int(LabNum)-1])
            return

cycle1()
if cyclenumber not in range(1,3):
    print ("Leave the premises now")
if list_rooms[int(LabNum)-1] == 'Room of Laughter':
    print ("'Room of Laughter")
