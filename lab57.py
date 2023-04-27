#!/usr/bin/env python3


question = input["Which of the following is NOT a quote from the 1942 film Casablanca?"]
correct = trivia["&quot;Frankly, my dear, I don&#039;t give a damn.&quot;"]
incorrect1 = trivia["&quot;Here&#039;s lookin&#039; at you, kid.&quot;"][0]
incorrect2 = trivia["&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;"][1]
incorrect3 = trivia["&quot;Round up the usual suspects.&quot;"][2]


    if question == "[correct]": # logic to check if user gave correct answer
        print("Correct!")
    elif question == "[0,1,2]"
        print("You gave the wrong  answer!")
    elif question == incorrect1,incorrect2,incorrect3:  
        print("keep trying")
    else
        print("Sorry. Try again!")
