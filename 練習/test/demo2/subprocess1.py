import subprocess

cmd = 'ipconfig'
dir = subprocess.getoutput(cmd)
# print(dir)

check_output = subprocess.check_output(cmd)
# print(check_output)

getstatus = subprocess.getstatusoutput(cmd)
# print(getstatus)

call = subprocess.call('ipconfig -all', shell=True)
call = subprocess.call(['ipconfig', '-all'])
print(call)
