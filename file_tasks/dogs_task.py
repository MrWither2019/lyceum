import json
with open("./txt_files/dogs.txt", 'r', encoding='utf-8') as din:
    dogs_information = dict()
    for i in din:
        inf = i.split(maxsplit=2)
        if int(inf[1]) < 5:
            dogs_information[inf[0]] = \
            {
                "возраст": inf[1],
                "порода": inf[2]
            }
    json_res = json.dumps(dogs_information, indent=4)
with open("./output_files/dogs.json", 'w',encoding='utf-8') as fout:
    fout.write(json_res)
