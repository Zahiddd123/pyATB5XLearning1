import math

try:
    math.exp(1000) # OverFlowError: math range error

except Exception as e:
    print(e)