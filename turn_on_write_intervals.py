import os
import sys
import shutil

if not os.path.isfile("system/controlDictFinal"):
    print("could not find ./system/controlDictFinal, exiting")
    sys.exit()


with open("system/controlDictFinal") as f:
    endTime = -1
    writeInterval = -1
    new_lines = []
    for line in f:
        if(line.startswith("endTime")):
            value = line.split()[-1]
            value = value[:-1]
            endTime = float(value)
            writeInterval = endTime/3.
        if(line.startswith("writeInterval")):
            line = "writeInterval %f;\n" % writeInterval
        if(line.startswith("purgeWrite")):
            line = "purgeWrite 1;\n"
        new_lines.append(line)
    print("detected runtime of %f" % endTime)
    print("setting writeInterval to %f" % writeInterval)

print("backing up original system/controlDictFinal to system/old_systemControlDictFinal")
shutil.move("system/controlDictFinal", "system/old_systemControlDictFinal")


with open("system/controlDictFinal", "w") as f:
    f.writelines(new_lines)
