import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
def unknown():
    res = ['Colud you please re phrase that?',
           "...",
           "Sounds about right",
           "What does that mean?"][random.randrange(4)]
    return res
