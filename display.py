arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
arrrev = arr[::-1]
arr2 = [*arrrev,*arrrev]

#the top row display like columns of a table 
sp = "\u0020"
chars = "Keys: " 

print("\n" + sp*36 + "Beaufort cipher\n")
for i in arr:
    chars += "[" + i.upper() + "]"
print(chars+ "\n")

#the main printing code
for i in arr:
    row = ""
    view = ""
    x = 0
    for j in arr2:
        if x < 26:
            row += arr2[arr.index(j)+ arr.index(i)]
        x = x + 1
    for c in row[::-1]:
        view += "[" + c + "]"
    print("[" + i.upper() + "]   " + view)
print("\n")