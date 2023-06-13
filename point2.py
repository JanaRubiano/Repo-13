def mergeDict(d1:dict, d2:dict) -> dict:
    d2.update({k:d1[k] for k in d1})
    return d2

if __name__ == "__main__":
    d1 = {}
    d2 = {}
    num_elmts = int(input("Enter the number of elements the dict will have: "))
    for i in range(num_elmts):
        key = input(f"Enter the {i+1} key with type string for dictionary 1: ")
        val = int(input(f"Enter the {i+1} value with type integer for dictionary 1: "))
        d1[key] = val
    for i in range(num_elmts):
        key = input(f"Enter the {i+1} key with type string for dictionary 2: ")
        val = int(input(f"Enter the {i+1} value with type integer for dictionary 2: "))
        d1[key] = val
    
    print(mergeDict(d1, d2))