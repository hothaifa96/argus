import datetime
import platform

# retrive the current time in format - yyyy-mm-dd HHH:MM:SS:msmsmsms
# we can change the fotmat using strftime function
time = datetime.datetime.now()

# getting the system os name and version using PYTHON built in module platform
ops = platform.system()
ops_v = platform.release()

try:
    with open('artifact.txt','a+') as file:
        file.write(f'current time :{time}operation system name : {ops}operation system version {ops_v}\n')    
        print('DONE')
except:
    print('something went wrong !!')
