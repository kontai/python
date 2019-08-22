def print30(*args,sep=' ',end='\n',file=sys.stdout,**kargs):
    output=''
    first=True
    for arg in args:
        output+=('' if first else sep)+str(arg)
        first=False
    for karg in kargs.itens():
        output += sep+str(karg)
    file.write(output+end)