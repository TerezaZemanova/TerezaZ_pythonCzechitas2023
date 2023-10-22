import json
with open('body.json', mode="r", encoding='utf-8') as file:
    znamky = json.load(file)

print (znamky)

prospech = {
    key: "pass" 
    if value >= 60 
    else "fail" 
    for key, value in znamky.items()
    }

print (prospech)

with open('prospech.json', mode="w", encoding='utf-8') as output_file:
    json.dump(prospech, output_file, ensure_ascii=False, indent=4)
