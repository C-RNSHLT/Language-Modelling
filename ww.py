def remove_confirmation(filename, cleanname):
    yeah = open(filename, "r")
    lines = []
    for line in yeah.readlines():
        crn = []
        confirmation = set(["yeah", "okay", "yes", "yep"])
        for word in line.split():
            if word in confirmation:
                crn.append("<confirmation>")
            else:
                crn.append(word)
        lines.append(crn)

    for i in range(len(lines)):
        lines[i] = " ".join(lines[i])
    out_file = open(cleanname, "w")
    out_file.write("\n".join(lines))

def remove_filler(filename, cleanname):
    yeah = open(filename, "r")
    lines = []
    for line in yeah.readlines():
        crn = []
        for word in line.split():
            if word in ["uh", "um"]:
                continue
            else:
                crn.append(word)
        lines.append(crn)
    for i in range(len(lines)):
        lines[i] = " ".join(lines[i])
    out_file = open(cleanname, "w")
    out_file.write("\n".join(lines))

def pickUp(filename, cleanname):
    yeah = open(filename, "r")
    lines = []
    for line in yeah.readlines():
        crn = []
        words = line.split()
        found = False
        if len(words) < 1:
            crn.append("")
        else:
            for i in range(len(words)-1):
                if found:
                    found = False
                    continue
                if words[i] == "pick" and words[i+1] == "up":
                    crn.append("pickup")
                    found = True
                else:
                    crn.append(words[i])
            if words[-1] != "up":
                crn.append(words[-1])
        lines.append(crn)

    for i in range(len(lines)):
        lines[i] = " ".join(lines[i])
    out_file = open(cleanname, "w")
    out_file.write("\n".join(lines))




def main():
    pass

if __name__ == "__main__":
    main()
