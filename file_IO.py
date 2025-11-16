file_name = "666"
fo = open(file_name, "w")
fo.write("aldksfja  askfdj asl " + "asdf a asdifh")

# fo.flush()
fo.close()

wf = open(file_name, "r")
while 1:
    get_string = wf.readline()
    if len(get_string) == 0:
        break
    print("file print=>" + get_string + "\n")

wf.close()
