from David import say,command
def reading_mode():
    say("reading mode enabled...")
    while True:
        say("""What do you want me to read sir?""")
        s = input("Enter a text\n")
        say(s)
        while True:
            say('Do you want me to read more?')
            confirm = command().lower()
            if confirm=="yes":
                say("okay...")
                break # the function reading mode has 2 while loops. break helps to step back from a single loop
            elif confirm=="no":
                say("""Okay sir... 
                    I am out of reading mode...""")
                return # return terminates the whole function
            else:
                say("Please confirm whether you want to continue or not.")