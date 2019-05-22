old_file_name="e:\\1.txt"
old_file=open(old_file_name,'r')

content=old_file.read()
new_file_name="e:\\2.txt"
new_file=open(new_file_name,"w")
new_file.write(content)

old_file.close()
new_file.close()
