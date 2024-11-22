from unittest.mock import right

public_toilet="PB"

def home():
    private_toilet="PT"
    print(private_toilet)
    public_toilet="PBB" # if variables hve the same names local variable are given more preference
    print(public_toilet)

home()