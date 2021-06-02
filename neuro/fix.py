import sys

filename = str(sys.argv[1])

f = open(filename,"r")
m = 0;
nodes = set([]);
edges = set([]);
for x in f:
    m+=1;
    for v in [int(j) for j in x.split(" ")]:
        nodes.add(v)
    edges.add(x);
if min(nodes) is 0:
    n = max(nodes)+1
if min(nodes) is 1:
    n = max(nodes)

print "nodes and edges"
m = len(edges)
print n,m


output = "";
output += str(n)+" "+str(m)+"\n"
f.close()

for s in edges:
    if min(nodes) is 0:
        output+=s;
    elif min(nodes) is 1:
        a,b = s.split(" ");
        a = int(a)-1;
        b= int(b)-1;
        output+=str(a)+" "+str(b)+"\n"

f = open(filename.split(".")[0]+".edg","w")
f.write(output[:-1])
