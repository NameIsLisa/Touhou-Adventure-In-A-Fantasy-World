define Y = Character("You", color="#ffffff") # This is on line 16.
define r = Character("Reimu", color="#ff0000") # This is on line 19
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

    return
