from settings import *

map_strings = ["2222222222222222222222222222222222222222222",
               "2000300000000000200030000001000000000000002",
               "2000303333033330200033300001000011110000002",
               "2000002111011120000000200001000044410000002",
               "2000002100000120000022200000000044410000002",
               "2000002100000122220000200001000044410000002",
               "2000002111111140000000000001000000000000002",
               "2222222222222222222222222222222222222222222"]

world_map = {}
mini_map = set()
for j, row in enumerate(map_strings):
    for i, char in enumerate(row):
        if int(char) != 0:
            mini_map.add((i * MAP_TILE, j * MAP_TILE))
            if char == "1":
                world_map[(i * TILE, j * TILE)] = "1"
            elif char == "2":
                world_map[(i * TILE, j * TILE)] = "2"
            elif char == "3":
                world_map[(i * TILE, j * TILE)] = "3"
            elif char == "4":
                world_map[(i * TILE, j * TILE)] = "4"
