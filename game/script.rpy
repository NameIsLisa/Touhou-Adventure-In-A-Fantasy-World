init:
    image white_screen = Solid("#ffffff") # Start on line 78.
define Y = Character("You", color="#ffffff") # This is on line 16.
define r = Character("Reimu", color="#ff0000") # This is on line 22
# ^ the above starts from line 16

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
    r "Thats Sakuya Izayoi,the chief maid of Scarlet Devil Mansion."
    r "Just search internet for more info, im not gonna tell more about her now...yet."
    r "By the way...make sure the background size is same as the game resolution, okay?" # < This dialog is important! read it!
    r "If the backround size(resolution) is smaler that the game resolution, this is what happen."
    scene hok tohok # This one is small, the size is 259 x 194 BUT the game size is 1920 x 1080.
    r "...."
    r "Can you see the background?"
    r "Its smoll...right? sooo make sure the size is same OR a little bit biger that the game resolution."
    menu:
        "Got It!":
            jump next_2

label next_2:
    scene black #This one is defaull... the screen will turn dark.

    Y "Sooo...now what?"
    "Now is time to..."

    show text "Hello!" # this one will appear on middle screen!
    "By the way...seem like you need a dialouge...uh.. menambahkan dialog diantara 'show' dan 'hide' agar kode tidak langsung melangkah ke 'hide'.." #< cobalah untuk hapus dialog ini, kode 'show text' akan tidak akan muncul(aka langsung hide) jadi pastikan ada dialog diatara 'show' dan 'hide'...atau...
    hide text # make sure to hide after you done use it.
    Y "YOOO what the-"

    # Let me do something...
    show text "TESTING."
    pause 1 #this will be usefull later...  
    hide text
    "hmmm...oh, its work." #Sooo as you can see, on line 70, 'pause 1' will make the game pause for 1 second, then continue automaticaly to next code/dialouge.
    "Theres a delay for the text to hide."

    "Dev" "Let me show you something...BUT BECAREFULL, FLASH WARNING!"
    "Dev" "After this!"
    # I will use init for make white screen! because Ren'py only have black screen. Go back to line 1 for the code. 
    show white_screen
    pause 0.05
    hide white_screen
    pause 0.05
    show white_screen
    pause 0.05
    hide white_screen
    pause 0.05

    "A white flash! this can be in your game, for example...well...flash."
    "Is your eyes okay? I hope your eyes okay."
    "Let's continue."
    jump next_3

label next_3:
    "Alright..."

    return #This will make you back to main menu.