IntroStory =  " At first all you see is darkness. You open your eyes and awaken in a field of tall grass next to a Church. You're awakened by a shrill scream, and your head pounds. You can't remember a thing but your heart feels sunken. You hear the scream again. It seems to be coming from within the church. You walk to the front door. It's very worn, old and cracked. Next to door is a window half open. Do you go through the door or window? "

choice_1 = ""
choice_2 = ""
choice_3 = ""
def story_1(test_mode=False):
    """
    This function is the first choice present in the story
    Parameters: 
    (string) The first input is a string either (door or window)
    Returns:
    (string) The return can be one of three things. The return value is always a string
    however, the string varies depending on the input. The return value is stored to be used
    in a later function
    
    """
    print(IntroStory)
    inp=''
    global choice_1
    if test_mode == False:
        inp = input("door or window: ")
    elif test_mode == True:
        inp = "door"
    if inp == "door": 
        choice_1 = "door"
        print(""""As you open the door, a strong musty smell wafts over you and your hands start to shake. You enter the room. It seems eerily familiar and you start having flashbacks of a man running around the room, saying, 'Alucard Edax Rerum'. You slowly creep into the middle of the room and you see a wooden table. It seems engraved. You kneel and a bat flies out from under it startling you. You fall to the floor and in doing so break a leg off the table. You pick it up and see that it has been sharpened to a point and the base of the table leg has an engraving. As you put the table leg against the moonlight you see an engraved bat with the words 'Alucard Edax Rerum written around it'. On the wall you see a bronze sword ontop of the window next to the door. You suddenly see blood oozing around the sword and get panicked and begin to rush upstairs to where you heard the earlier scream from. Do you want to grab the sword or the table leg?""")
    elif inp == "window":
        choice_1 = "window"
        print("""" You try to open the window, but it won't budge. You notice something shining on the window's reflection. You back off the window and head to the door. Do you open the door?""")
    else:
        print("Indecision is the worst. Try to clear your mind and make a decision. door or window")

choice_2 = ""


def story_2():
     ###This function is the result of one pathway that can be taken in the overarching story.
    ### It does not matter what the input is regardless the story progresses to the same conclusion
    """
    This function is the second choice present in the story.
    Parameters: 
    (string)The input in the first function (story_1) must be the string (window). The 
    second input must be one of two strings, yes or no
    Returns:
    (string)The return can be one of three things. The return value is always a string
    however, the string varies depending on the input.
    
    """
    inp_2 = ""
    inp_2 = input("yes or no: ")
    global choice_2
    if choice_1 == "window" and inp_2 == "yes":
        print(""""As you open the door, a strong musty smell wafts over you and your hands start to shake. You enter the room. It seems eerily familiar and you start having flashbacks of a man running around the room, saying, 'Alucard Edax Rerum'. You slowly creep into the middle of the room and you see a wooden table. It seems engraved. You kneel and a bat flies out from under it startling you. You fall to the floor and in doing so break a leg off the table. You pick it up and see that it has been sharpened to a point and the base of the table leg has an engraving. As you put the table leg against the moonlight you see an engraved bat with the words 'Alucard Edax Rerum written around it'. On the wall you see a bronze sword ontop of the window next to the door. You suddenly see blood oozing around the sword and get panicked and begin to rush upstairs to where you heard the earlier scream from. Do you want to grab the sword or the table leg?""")
    elif choice_1 == "window" and inp_2 == "no":
        choice_2 = "no"
        print("""" All of a sudden you hear the scream again. There's no time to waste you open the door. As you open the door, a strong musty smell wafts over you and your hands start to shake. You enter the room. It seems eerily familiar and you start having flashbacks of a man running around the room, saying, 'Alucard Edax Rerum'. You slowly creep into the middle of the room and you see a wooden table. It seems engraved. You kneel and a bat flies out from under it startling you. You fall to the floor and in doing so break a leg off the table. You pick it up and see that it has been sharpened to a point and the base of the table leg has an engraving. As you put the table leg against the moonlight you see an engraved bat with the words 'Alucard Edax Rerum written around it'. On the wall you see a bronze sword ontop of the window next to the door. You suddenly see blood oozing around the sword and get panicked and begin to rush upstairs to where you heard the earlier scream from. Do you want to grab the sword or the table leg?""")
    else:
        print("Indecision is the worst. Try to clear your mind and make a decision. yes or no")

choice_3 = ""

def story_3(test_mode2=False):
    ### The input to this function is what determines the conclusion to the story
    """
    This function is the third choice present in the story.
    Parameters: 
    (string)The input in the first function (story_1) can be either (door or window). The 
    second input can be one of the two strings, yes or no. The third input must be either sword or table leg
    Returns:
    (string)The return can be one of three things. The return value is always a string
    however, the string varies depending on the input. Furthermore this input causes
    variability in the story, and as such the input is stored as choice_3.
    """
    global choice_3
    if test_mode2==False:
        inp_3= input("sword or table leg: ")
    elif test_mode2 == True:
        inp_3 = "sword"
    if inp_3 == "sword":
        choice_3 = "sword"
        print(""""You grab the sword and rush upstairs and you see an altar, with a body strapped down. You see a hunched disfigured person over the altar. Do you wish to try to speak to the figure?""")
    elif inp_3 == "table leg":
        choice_3 = "table leg"
        print("""You grab the table leg and rush upstairs and you see an altar, with a body strapped down. You see a hunched disfigured person over the altar. Do you wish to try to speak to the figure?""")
    else:
        print("Indecision is the worst. Try to clear your mind and make a decision. sword or table leg?")

        choice_4 = ""

def story_4():
     ### The input for this portion of this story does not matter. 
    ### Regardless of the input the story reaches the same ending

    """
    This function is the fourth choice present in the story.
    Parameters: 
    (string)The input in the first function (story_1) can be either (door or window). The 
    second input can be one of the two strings, yes or no. The third input can be either sword or table leg.
    This functions inputs must be either yes or no, however regardless the story progresses to the same conclusion
    Returns:
    (string)The return can be one of three things. The return value is always a string
    however, the string varies depending on the input.
    """
    global choice_4
    inp_4 = input("yes or no: ")
    if inp_4 == "yes":
        choice_4 = "yes"
        print("""You try to speak but a feeling of absolute terror floods your body and not a single word escapes you. Suddenly you hear more chanting,'Alucard Edax Rerum. Alucard Edax Rerum. Alucard Edax Rerum'. To your absolute horror it seems to be coming from the person strapped onto the altar. Upon closer examination you see that the person strapped to the altar is you. Or something that looks like you. As they chant, you see the disfigured body over the altar seems to get larger. You slowly approach the the figure, and notice that you seem to be wading through pools of blood. Do you wish to attack?""")
    elif inp_4 == "no":
        choice_4 = "no"
        print("""Suddenly you hear more chanting,'Alucard Edax Rerum. Alucard Edax Rerum. Alucard Edax Rerum'. To your absolute horror it seems to be coming from the person strapped onto the altar. Upon closer examination you see that the person strapped to the altar is you. Or something that looks like you. As they chant, you see the disfigured body over the altar seems to get larger. You slowly approach the the figure, and notice that you seem to be wading through pools of blood. Do you wish to attack?""")
    else:
        print("Indecision is the worst. Try to clear your mind and make a decision. yes or no?")

        choice_5 = ""
def story_5():
    """
    This function is the final choice present in the story.
    Parameters: 
    (string)The input in the first function (story_1) can be either (door or window). The 
    second input can be one of the two strings, yes or no. The third input can be either sword or table leg.
    This functions inputs must be either yes or no, however the story ends here and the endings are 
    dependent on some of your previous inputs
    Returns:
    (string)The return can be one of three things. The return value is always a string
    however, the string varies depending on the input. 
    """
    global choice_5
    inp_5 = input("yes or no: ")
    if choice_3 == "sword" and inp_5 == "yes": ### choice_3 is called as it is neccessary for which pathway you chose
        choice_5 = "yes"
        print(""" You raise your sword to strike but as you make contact with the figure the sword breaks in half. ### The figure turns around and you see its' decripit features. The blood red eyes contrasting the pale skin are visible only for a second as you feel an unbeliaveable force slam you against a wall. You lay on the floor, unable to move staring at the ceiling as the adrenaline attempts to hide the pain of all your bones breaking. As you look up you notice a flock of creatures all bat-like in form but sharing your features dangling from the ceiling, you attempt to scream but are unable to do so. The figure pounces on you tearing your throat apart. You begin to see the world in a reddish hue as you choke on your own blood. You close your eyes only to open them when you hear a scream. You awaken in tall grass next to a church.""")
    elif choice_3 == "sword" or "table leg" and inp_5 == "no":
        choice_5 = "no"
        print(""" You can't seem to calm your nerves, and in a jittery fit stumble down. The figure turns around and you see its' decripit features. The blood red eyes contrasting the pale skin are visible only for a second as you feel an unbeliaveable force slam you against a wall. You lay on the floor, unable to move staring at the ceiling as the adrenaline attempts to hide the pain of all your bones breaking. As you look up you notice a flock of creatures all bat-like in form but sharing your features dangling from the ceiling, you attempt to scream but are unable to do so. The figure pounces on you tearing your throat apart. You begin to see the world in a reddish hue as you choke on your own blood. You close your eyes only to open them when you hear a scream. You awaken in tall grass next to a church.""")
    elif choice_3 ==  "table leg" and inp_5 == "yes":
        choice_5 = "yes"
        print(""" You raise the table leg and drive it into the heart of the figure. The figure winces in pain, but does not fall down. It turns around and grabs you sinking its visceral teeth into your neck muttering 'Alucard edax rerum' You quickly push the wooden shaft deeper into the figure and the figure stops moving, going limp. You back away and fall to the floor. A pool of blood accumulates from the side of your neck and as you feel lighter you close your eyes one final time muttering uncontrollably that horrid chant 'Alucard edax Rerum' only to open them when you hear a scream. You awaken in tall grass next to a church.""")
    else:
        print("Indecision is the worst. Try to clear your mind and make a decision. yes or no?")
   
def main_story():
    """ 
    This function is the main function that combines all other 5 original functions
    Parameters: 
    Requires the other functions; runs when called upon
    Returns:
    The output is the chatbot assembled together
    """
    
    story_1()
    if choice_1 == "door": ### This if statement accounts for story_2.
        story_3()
        story_4()
        story_5()
    else:
        story_2() ### story_2 is a side loop that connects to main story again. 
        story_3() ### story_2 is not neccessary for the other functions to be run
        story_4()
        story_5()