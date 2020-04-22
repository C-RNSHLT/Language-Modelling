ls = []

with open("hyp.txt", "r") as file:
    while True:
        ls.append(file.readline())
        temp = file.readline()
        if not temp: break


ls = [l[13:-6] for l in ls]

with open("hypnorm.txt", "w") as f:
    [f.write(w+"\n") for w in ls]

#from_fsm <s> oh uh ground beef on uh bacon bits and pepperoni </s>
