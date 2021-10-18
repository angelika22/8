Sir1, Sir2="ABC XYZ NOM", ''
for i in Sir1:
    if i==' ':
        Sir2+='-'
    if i=='Z':
        Sir2+='A'
    if i!='Z' and i!=' ':Sir2+=chr(ord(i)+1)
print(Sir2)