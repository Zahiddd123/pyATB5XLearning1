public_toilet= "PB"

def home():
    private_toilet= "PT"
    print(public_toilet)
    print(private_toilet)

home()

def strange():
    print(public_toilet)
    #print(private_toilet) # local variables have more preference as
                           # compare to the public variable

strange()

print(public_toilet)
#print(private_toilet)