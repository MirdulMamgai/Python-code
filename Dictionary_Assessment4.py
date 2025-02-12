# Merge following two Python dictionaries into one.
# Get the key corresponding to the minimum value from the following
# dictionary
# sampleDict = { 'Physics': 82, 'Math': 65, 'history': 75}
# Expected output: Math

d1={'phy':82,
    'math':65,
    'hist':75}
a1=min(d1.values())
for i,j in d1.items():
    if(j==a1):
        print(i)