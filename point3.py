import json

def jsonInfo(sport:str, age:list) -> list:
    

    with open("jsonFile.json", "r") as json_file:
        d_read = json_file.read()
    data = json.loads(d_read)

    sports = []
    with_ages = []
    for person in data:
     info = data[person]
     if sport in info["deportes"]:
      sports.append(str(info['nombres'] + " " + info['apellidos']))

    for person in data:
     info = data[person]
     if age[0] <= info["edad"] <= age[1]:
      with_ages.append(str(info['nombres'] + " " + info['apellidos']))
    
    names = [sports, with_ages]
    return names
    


if __name__ == "__main__":
    age = int(input("Enter minimum age: ")), int(input("Enter maximim age: "))
    sport = input("Enter a sport: ")
    res = jsonInfo(sport, age)
    s = " ".join(res[0])
    a = " ".join(res[1])
    print(f"People who practice {sport} are: {s}\nPeople in age range {age[0]}-{age[1]} are: {a}")