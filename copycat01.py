#!/usr/bin/env python3
import shutil
import os

#os.chdir("/home/student/mycode/")
#shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#shutil.copytree("5g_research/", "5g_research_backup/")

def main():
    """code to move files around"""
    # move into the working directory
    os.chdir("/home/student/mycode/")

    # copy the fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy the entire directoryA to directoryB
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
