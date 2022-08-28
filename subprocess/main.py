import subprocess
cmd = "ls -al"
sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f'OUTPUT IS: {out}')
print(f'Error is: {err}')
# ==================================>
# if shell=True then your cmd is a string (as your os command)
# if shell=False then your cmd is a list

# Note: shell=False dont work on your os environment variables
      
# ex: cmd="ls -lrt" ==>shell=True
#     shell=False ==> cmd="ls -lrt".split()  or ['ls','-lrt']
# =======================================================================


# shell=True always on windows
# ============================
# cmd is a string
# ----------------------------------------------------------
