
import os

############################################################
#							   #
# This script generates git configuration that is required #
# for git automation and initial configuration		   #
#	1. global config is set automatically		   #
#	2. local config : Only file is generated           #
#							   #
############################################################

print("*** GIT Configuration generator ***\n\n")

## Global / Local selector
print("Please select type of config to be generated:\n\t1. Global\n\t2. Local\n")
type_sel = int(input("Select (1/2): "))
print(type_sel)
