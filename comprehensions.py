set_comp1=set(i*2 for i in range(40) if i%2==0)
set_comp2=set((a,b) for b in range(50) for a in range(16))

#print(set_comp1)
#print(set_comp2)

dict={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
dict_comp1={k:v for (k, v) in dict.items()}

print(dict_comp1)