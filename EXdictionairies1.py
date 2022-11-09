#!/usr/bin/env python3
import sys
fav_dict = {
  "book": "Xablau",
  "band": "Araketu",
  "music": "Timbalada"
}
print(fav_dict['book'])
fav_thing = sys.argv[1]
fav_dict[fav_thing] = "novo iten"
print(fav_dict[fav_thing])
fav_dict["color"] ="red"
fav_dict["atividade"] = sys.argv[2]
fav_dict["music"] = "menina solta"
print(fav_dict)
for fav in fav_dict:
	seq = fav_dict[fav]
	print(fav,seq)
