# Rabbit Attack!

def show_credits():
        
        
        print("""
 .--.                          .--.                  
: .--'                        : ,. :                 
: : _  .--.  ,-.,-.,-. .--.   : :: :.-..-. .--. .--. 
: :; :' .; ; : ,. ,. :' '_.'  : :; :: `; :' '_.': ..'
`.__.'`.__,_;:_;:_;:_;`.__.'  `.__.'`.__.'`.__.':_;  
         """)
        
       
                
def show_header():
        print ("""
.---.        .-.   .-.    _  .-.    .--.  .-.  .-.             .-.   
: .; :       : :   : :   :_;.' `.  : .; :.' `..' `.            : :.-.
:   .' .--.  : `-. : `-. .-.`. .'  :    :`. .'`. .'.--.   .--. : `'.'
: :.`.' .; ; ' .; :' .; :: : : :   : :: : : :  : :' .; ; '  ..': . `.
:_;:_;`.__,_;`.__.'`.__.':_; :_;   :_;:_; :_;  :_;`.__,_;`.__.':_;:_;
                                                                     
   
                                                                          """)

def start():
    print("Welcome to RABBIT ATTACK!")

def end():
    print("Goodbye. Thanks for playing!")
    
def confirm(question):
    while True:
        answer = input(question + " (y/n)").lower() # .lower() deals case sensitivity

        if answer in ["y" , "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False

def play():
    num_knights = 5
    rabbit_is_alive = True

    print("Look, a cute little bunny rabbit.")

    while rabbit_is_alive and num_knights > 0:
        use_grenade = confirm("Shall we use the Holy Hand Grenade?")
            
        if use_grenade:
            print("1... 2... 5... No, 3!")
            print("Boom!")
            rabbit_is_alive = False
        else:
            num_knights -= 1
            print("Oh, no! The rabbit just killed one of the knights!")
            print("Only " + str(num_knights) + " remain.")
        
    if num_knights > 0:
        print("The killer rabbit has been defeated. You win!")
    else:
        print("All of the knights are dead. You lose.")
    
show_header()
start()
    

playing = True

while playing:
    play()
    playing = confirm("Would you like to play again?")
    
show_credits()

