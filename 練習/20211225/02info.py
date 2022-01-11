text='''
    title,author,year
    The weirdstone of Brisingmen,Laln Gerner,1060
    Perdido Street Station,China Mi.ville,2000
    Thud!,Terry Pratchert,2005
    The Spellman Files,Lisa Lutz,2007
    Small Gods,Terry Pratchert,1992
'''
with open('books.csv','w') as wt:
    wt.write(text)