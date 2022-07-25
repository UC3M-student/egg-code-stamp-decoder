code_identifier = input("Please enter your egg code: ")

farming_method = {0:"Organic",
                  1:"Free range",
                  2:"Barn",
                  3:"Cage"}

with open("egg.txt","r") as f:
    w = f.readlines()
    for i in w:
        if code_identifier[1:3] == i[0:2]:
            break
            
print("Farming method: ",farming_method[int(code_identifier[0])])
print("Country of origin: ",i[3:])
print("Farm ID",code_identifier[3:])
