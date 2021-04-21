x,y,z,n =1,1,2,3

print([[a,b,c] for a in range(0,z+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c!=n])
