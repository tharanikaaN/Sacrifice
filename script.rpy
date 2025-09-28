# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Variables
init python:
    fear = 30
    guilt = 10
    hope = 50
    sacrifices = 0
    inventory = []

define e = Character("Yuri")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image title page = im.Scale("title page.jpg", 1920, 1080)
    show title page
     
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    # These display lines of dialogue.

    e "A group was on a camping trip"


    # This ends the game.

    image bg campfire = im.Scale("bg campfire.jpg", 1920, 1080)
    scene bg campfire
    e "They hear a sound in the woods and go to investigate"

    image bg woods = im.Scale("bg woods.jpg", 1920, 1080)
    scene bg woods
    e "They find a cabin and decide to spend the night there"

    image bg cabin = im.Scale("bg cabin.jpg", 1920, 1080)
    scene bg cabin
    e "Inside the cabin, they find strange symbols on the walls"
   
    image bg cabin = im.Scale("bg cabin.jpg", 1920, 1080)
    scene bg cabin
    e "They hear weird footsteps approaching their cabin"

   
    image bg cabin = im.Scale("bg cabin.jpg", 1920, 1080)
    scene bg cabin
    e "They see a shadowy figure creeping outside the window"

    
    image bg cabin = im.Scale("bg cabin.jpg", 1920, 1080)
    scene bg cabin
    e "The figure breaks in, revealing itself to be a monster" 

    
    image bg cabin = im.Scale("bg cabin.jpg", 1920, 1080)
    scene bg cabin
    e "As every second passes, they back away slowly as the monster comes closer, thinking of a solution to survive"

    
    image bg cabin = im.Scale("bg cabin.jpg", 1920, 1080)
    scene bg cabin
    e "Out of their desperation to survive, one of the group memeber's, Yuri, grabs Johnny and pushes him towards the monster"

    
    image bg woods = im.Scale("bg woods.jpg", 1920, 1080)
    scene bg woods
    e "They all run out of the cabin and escape into the woods, leaving Johnny behind, his screams echoing through the night"

    
    image bg campfire = im.Scale("bg campfire.jpg", 1920, 1080)
    scene bg campfire
    e "They never speak of that night again, but the guilt of leaving Johnny behind haunts them forever as they think to themselves..."

    image bg quote = im.Scale("bg quote.jpg", 1920, 1080)
    scene bg quote
   
label meet_e:
    scene bg campfire

    e "We need to do something"
    e "We can't just leave him"

menu:
    "offer something":
        $ fear -= 5
        $ hope += 5
        "You promise something"
        $ inventory.append("satchel")
    "suggest something to decide.":
        $ guilt += 10
        $ fear -= 5
        "You hint at others"

        jump meet_m

label meet_m:
        
            e "We need to do something"
            e "We can't just leave him"
            e "We have to go back"
            e "We have to save him"
            e "They all look at each other nervously, before finally agreeing to go back to the cabin"
            e "As they approach the cabin, the screams grew quieter and quieter, until they finally stop" 
            e "They enter the cabin, but Johnny is nowhere to be found"
            e "Before they could react.. missing posters of them started appearing all over town"
            e "Bad Ending"
    
    

return
