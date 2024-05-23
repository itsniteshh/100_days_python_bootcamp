parrot = {
    "type": "bird",
    "owner": "nitesh"
}

tiger = {
    "type": "animal",
    "owner": "arjun"
}

dog = {
    "type": "animal",
    "owner": "nishit"
}

pets = [parrot, tiger, dog]

for animals in pets:
    print(f'{animals["type"].capitalize()}, {animals["owner"].capitalize()}')