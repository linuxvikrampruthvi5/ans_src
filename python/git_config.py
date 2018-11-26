#############################################################
#							                                #
# This script generates git configuration that is required  #
# for git automation and initial configuration		        #
#	1. global config is set automatically		            #
#	2. local config : Only file is generated                #
#							                                #
#############################################################

# Imports for the project
import os
import subprocess


class bcolors: # Class to print colored output
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def git_global(): # Global configuration
    name=""; email=""
    print("Global Configuration initialized\n")
    while len(name) == 0:
        name = raw_input("Default Username : ")
    while len(email) == 0:
        email = raw_input("Default Email id : ")
    colors = raw_input("Do you want git to use colors (Y / N) : ")
    usr_def = raw_input("Set push default to simple (Y / N) : ")
    editor = raw_input("Set default editor (Y / N) : ")


    ## Actual git commands execution starts here.
    os.system('git config --global user.name \"'+name+'\"')
    print(bcolors.OKGREEN + "Username setup for git completed..." + bcolors.ENDC)
    os.system('git config --global user.email \"' + email + '\"')
    print(bcolors.OKGREEN + "Email setup for git completed..." + bcolors.ENDC)
    if colors == 'Y' or 'y':
        os.system('git config --global color.diff \"auto\"')
        os.system('git config --global color.status \"auto\"')
        os.system('git config --global color.branch \"auto\"')
        os.system('git config --global color.interactive \"auto\"')
        os.system('git config --global color.ui \"true\"')
        os.system('git config --global color.pager \"true\"')
        os.system('git config --global color.status.added \"green\"')
        os.system('git config --global color.status.changed \"red bold\"')
        os.system('git config --global color.status.untracked \"magenta bold\"')
        os.system('git config --global color.branch.remote \"yellow\"')
        print(bcolors.OKGREEN+"Color setup for git completed..."+bcolors.ENDC)
    if usr_def == 'Y' or 'y':
        os.system('git config --global push.diff \"simple\"')
    if editor == 'Y' or 'y':
        ed = raw_input("Which editor (vim, vi, emacs, etc): ")
        print(bcolors.WARNING+'Checking existance of '+ed+" ..."+bcolors.ENDC)
        ed = raw_input("Which editor (vim, vi, emacs, etc): ")
        print('Checking existance of ' + ed + " ...")
        proc = subprocess.Popen('which ' + ed, stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        if len(out) > 0:
            os.system('git config --global core.editor '+out+'')
            print(bcolors.OKGREEN + "Color setup for git completed..." + bcolors.ENDC)
        else:
            print(bcolors.FAIL+"Default editor setup failed..."+bcolors.ENDC)


def main():
    print("*** GIT Configuration generator ***\n\n")

    # Global / Local selector
    print("Please select type of config to be generated:\n\t1. Global\n\t2. Local\n")
    type_sel = int(input("Select (1/2): "))

    if type_sel == 1:
        git_global()


def test():
    ed = raw_input("Which editor (vim, vi, emacs, etc): ")
    print('Checking existance of ' + ed + " editor")
    proc = subprocess.Popen('which ' + ed, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    if len(out) > 0:
        #os.system('git config --global core.editor ' + out + '')
        print(bcolors.OKGREEN+"Default editor setup for git completed..."+out+" "+bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Default editor setup failed..." + bcolors.ENDC)
    print("")


if __name__ == '__main__':
    #main()
    test()