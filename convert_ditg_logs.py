import subprocess32 as subprocess
import os
import os.path
import glob
import sys

def main():

    OUTPUT_PATH = "./cc-final-project/server_outputs/"
    DECODER_EXEC = "./D-ITG-2.8.1-r1023/bin/ITGDec"
    
    log_files = list(sorted(glob.glob(os.path.join(OUTPUT_PATH, "*.log"))))
    #print(log_files)

    temps = [(os.path.splitext(x)[0] + ".output") for x in log_files]
    #print(temps)

    for i in range(len(log_files)):

        with open(temps[i],"w+") as tempdata:
            subprocess.call([DECODER_EXEC, log_files[i]], stdout=tempdata)

if __name__ == '__main__':
    main()
