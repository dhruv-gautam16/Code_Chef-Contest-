# cook your dish here
# cook your dish he

ctest = str(input())

ccount = {'C':0,'CH':0,'CHE':0,'CHEF':0}

for i in range(len(ctest)):

    if ctest[i]=='C': ccount['C']+=1

    elif ctest[i]=='H' and ccount['C']>ccount['CH']: ccount['CH']+=1

    elif ctest[i]=='E' and ccount['CH']>ccount['CHE']: ccount['CHE']+=1

    elif ctest[i]=='F' and ccount['CHE']>ccount['CHEF']: ccount['CHEF']+=1

#print(ccount)

print(ccount['CHEF'])