# mainprog.py
import os, time, shutil

root = os.path.dirname(__file__) # needed for tornado
inputFolder = os.path.join(root,'input')

output1 = os.path.join(root,'Intermediate_analysis')
output2 = os.path.join(root,'Results')

os.makedirs(output1, exist_ok=True)
os.makedirs(output2, exist_ok=True)


def computeThis(configD):
    print("Do your computation here")

    full_filename = os.path.join(inputFolder,configD['attachment'])

    time.sleep(5) # pause 5 mins, remove this in final

    logs = []
    logs.append("One log line")

    logs.append("Another log line")

    # zipping outputs
    root_dir1 = root if len(root) else os.curdir
    cf.logmessage("root_dir:", root_dir1)
    logs.append(f"Zipping outputs.. root_dir: {root_dir1}")
    o1Filename = 'Intermediate_analysis_output'
    o2Filename = 'Results_output'
    shutil.make_archive(base_name=os.path.join(root,o1Filename), 
        format='zip', root_dir=root_dir1, base_dir='Intermediate_analysis' )
    shutil.make_archive(base_name=os.path.join(root,o2Filename), 
        format='zip', root_dir=root_dir1, base_dir='Results' )
    
    returnD = { 'message': 'completed', 'logs':logs, 'output1': f"{o1Filename}.zip", 'output2': f"{o2Filename}.zip" }

    return returnD
