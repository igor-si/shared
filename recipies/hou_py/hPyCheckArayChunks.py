"""
ETA = explode them all
terraformers
rolling stones
exploding kittens
sappers
split devils
dynamite squad
big bang terraformersdividers by zero
dissasemble team / decomposition team
"""

"""
===vex part for append classGuide if in volumesampe
float vs = volumesample(1,0,v@P);
int classGuide=prim(1,"classGuide",0)
if(vs>0)
{
	append(i[]cG,classGuide);	
}

===vex part for combining arrays in !detail mode!
int combG[];
for(int i=0;i<nprimitives(0);i++)
{
	int curG[]=prim(0,"cG",i);
	foreach(int num;curG)
	{
	append(combG,num);
	}
i[]@combG=combG;

}

"""
from collections import Counter
n = hou.pwd()
g = n.geometry()

cGL = [] #global array
cGL = g.intListAttribValue("combG")

new_vals = Counter(cGL).most_common()
new_vals = new_vals[::-1]

#zero values
bCount = -1
mFreq = -1

#find max value for most common element
for a,b in new_vals:
	if b>bCount:
		bCount=b

#find most frequent classGuide
for a,b in new_vals:
	if b==bCount:
		mFreq=a

g.addAtrib(hou.attribType.Global,"mostFreq",mFreq)

