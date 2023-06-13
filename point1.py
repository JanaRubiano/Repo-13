def ascendingDict(d:dict) -> list:
    return sorted(d.values())

if __name__ == "__main__":
    d = {}
    num_elmts = int(input("Enter the number of elements the dict will have: "))
    for i in range(num_elmts):
        key = input(f"Enter the {i+1} key with type string: ")
        val = int(input(f"Enter the {i+1} value with type integer: "))
        d[key] = val
    
    print(ascendingDict(d))
    

