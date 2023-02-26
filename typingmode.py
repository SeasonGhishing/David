from David import say,command
def typeMode():
    say("typing mode enabled...")
    say("What would you like to name your file?")
    txtfile = command().lower()
    say("""Okay... 
        i am listening... 
        you may speak now""")
    while True:
        fornp = command().lower()
        while True:
            say("""Do you want to continue your speech?""")
            confirm = command().lower()
            file = open(txtfile+'.txt','a')
            file.write(fornp+". \n")
            if confirm=="yes":
                say("you may continue sir..")
                break
            elif confirm=="no":
                say("""Okay sir...
                    I am out of the typing mode""")
                return
            else:
                say('Please confirm whether you want to continue or not.')
            