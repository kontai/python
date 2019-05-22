a = "For months, Google has been trying to stay out of the way of the growing tech backlash, but yesterday, the dam finally broke with news of a bug in the rarely used Google + network that exposed private information for as many as 500, 000 users. Google found and fixed the bug back in March, around the same time the Cambridge Analytica story was heating up in earnest. But with the news breaking now, the damage is already spreading. The consumer version of Google + is shutting down, German privacy regulators in Germany and the US are already looking into possible legal action, and former SEC officials are publicly speculating about what Google may have done wrong.The vulnerability itself seems to have been relatively small in scope. The heart of the problem was a specific developer API that could be used to see non-public information. But crucially, there’s no evidence that it actually was used to see private data, and given the thin user base, it’s not clear how much non-public data there really was to see. The API was theoretically accessible to anyone who asked, but only 432 people actually applied for access(again, it’s Google+), so it’s plausible that none of them ever thought of using it this way."



source_File = open("e:\\1.txt", "w")
source_File.write(a)
source_File.close()

source_File = open("e:\\1.txt", "r")
string=""
string=source_File.read()
cnt=len(string)
print("字數="+str(cnt))


#for tmp in string:



#string=list()
#for st in source_File.read():
#    string.append(st)
print(string)
dest_File=open("e:\\out.txt","w")
dest_File.write(string)
dest_File.close()
source_File.close()
print("clone completed")





