define Y = Character("You", color="#ffffff") # This is on line 16.
define r = Character("Reimu", color="#ff0000") # This is on line 20
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
    Y "I'm you!" # see line 1
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

## NOTE: Don’t have labels with the same name! ##
label next_1:
    r "Nice! You did it."


    return
