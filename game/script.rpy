init:
    image white_screen = Solid("#ffffff") # Start on line 81.
define Y = Character("You", color="#ffffff") # This is on line 18.
define r = Character("Reimu", color="#ff0000") # This is on line 22.


label start:
    # Below are some dialogues!
    "Hello, this is my dialogue!"
    "Where's your dialogue?"

    # You can also add a character name, otherwise we won’t know who is speaking, right?
    "Dev""It's me!"
    ## Before the dialogue, add "" and put the name inside it (name is up to you) 
    ## "Dev" < character name | "It’s me!" < dialogue.

    # You can also shorten it!
    Y "I'm you!" # see line 3
    # define 'whatever' = Character("Name", color="") defines a shortcut (letters ONLY, NOT numbers!) 
    # so you can shorten long names...
    # In color="" you can change the name’s color, such as #ffffff for white, #ff0000 for red, etc.
    r "Testing testing..." # Uppercase (Y) or lowercase (r) doesn’t matter! As long as it’s not a number~
    
    jump next
    # ^ This means jump to the next label. 
    # Very useful especially when you want to add choices using 'menu'.

label next:
# ^ If you want to jump, there must be a label to jump to!

    r "Ahem... so... how about we continue to the menu?"

    menu:  # Here it is! Try running this in Ren’Py and you’ll see how it works!
        "Let's go!":
            jump next_1 # If you choose this, it will jump to the next label.
        "Uh... could you repeat that?":
            jump next # If you choose this, it will jump to the same label (repeat again).

## NOTE: Do NOT have labels with the same name! ##
label next_1:
    r "Nice! You did it."

    r "Now, Let's go to scene!"
    scene sakuya_bg # scene, for background! 'sakuya_bg' is the name of the background, make sure the file is inside (game -> images).
    r "That’s Sakuya Izayoi, the chief maid of Scarlet Devil Mansion."
    r "Just search the internet for more info, I’m not gonna tell more about her now...yet."
    r "By the way...make sure the background size is the same as the game resolution, okay?" # < This dialog is important! read it!
    r "If the background size (resolution) is smaller than the game resolution, this is what happens."
    scene hok tohok # This one is small, the size is 259 x 194 BUT the game size is 1920 x 1080.
    r "...."
    r "Can you see the background?"
    r "It’s small...right? sooo make sure the size is the same OR a little bit bigger than the game resolution."
    menu:
        "Got It!":
            jump next_2

label next_2:
    scene black #This one is default... the screen will turn dark.

    Y "Sooo...now what?"
    "Now it’s time to..."

    show text "Hello!" # this one will appear on middle screen!
    "By the way...seems like you need a dialogue...uh... add a dialogue between 'show' and 'hide' so the code doesn’t immediately skip to 'hide'.." 
    # < try deleting this dialogue, the 'show text' won’t appear (it will immediately hide). 
    # So make sure there’s a dialogue between 'show' and 'hide'...or...
    hide text # make sure to hide after you’re done using it.
    Y "YOOO what the-"

    # Let me do something...
    show text "TESTING."
    pause 1 #this will be useful later...  
    hide text
    "hmmm...oh, it works." 
    # Sooo as you can see, on line 71, 'pause 1' will make the game pause for 1 second, then continue automatically to the next code/dialogue.
    "There’s a delay for the text to hide."

    "Dev" "Let me show you something...BUT BE CAREFUL, FLASH WARNING!"
    "Dev" "After this!"
    # I will use init to make a white screen! because Ren'Py only has black screen. Go back to line 1 for the code. 
    show white_screen
    pause 0.05
    hide white_screen
    pause 0.05
    show white_screen
    pause 0.05
    hide white_screen
    pause 0.05

    "A white flash! this can be in your game, for example...well...flash."
    "Are your eyes okay? I hope your eyes are okay."
    "Let's continue."
    jump next_3

label next_3:
    "Alright..."
    "Sprite time!"
    show hehee # Show again, but now it’s a character sprite! 
                # Reminder: make sure the sprite is SMALLER than the game resolution. 
                # If you make it the same size as 1920x1080, congrats, you just made a background :')
    "Well... Sakuya again."
    "..."
    hide hehee # Hide the sprite. Bye-bye Sakuya~
    "Alright, done."
    "Hmm..."
    "{cps=25}background done...character done...flash...yep...{/cps}"
    # ^ This line will display the text slowly, one character at a time,
    # instead of instantly dumping the whole sentence like Ren’Py sneezing.
    # {cps=25} = Characters Per Second (25 chars appear each second).
    # {/cps} = End the effect. Without this, your next lines will also go sloooow...
    
    "Oh, did you see that?"
    "My dialogue appeared word by word!"
    # Basically, if you want a "typing effect" (like someone hammering on a keyboard),
    # use {cps=<number>}. The smaller the number = the slower it types.
    # The bigger the number = faster. Simple math, simple happiness.
    
    "{cps=10}Soooooooooooooooo slowwwwwwwwww....{/cps}" 
    # 10 cps. Looks like the character is half asleep typing this.
    
    "{cps=50}WOAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH FASTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT{/cps}" 
    # 50 cps. Now they’re chugging 3 cups of coffee.
    
    "{cps=1000}AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{/cps}" 
    # 1000 cps. That’s not typing. That’s a text machine gun.
    
    "Ahem..."
    # End with some dignity… or at least try to.
    
    return #This will take you back to the main menu.
