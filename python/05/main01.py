import numpy as np

def parse_maps(chunk):

    chunks = chunk.split('\n\n')
    maps = {}


    for group in chunks:

        group_split = group.split(':')
        map_name = group_split[0]
        map_values = group_split[1].strip()

        maps[map_name] = list(map(int, map_values.split()))

        if map_name == 'seeds':
            continue
       
        maps[map_name] = np.reshape(maps[map_name], newshape=(len(maps[map_name]) // 3, 3)).tolist()

    return maps

def map_val(x, map_):
   
    offset = 0 
    for row in map_:
        d1, s1, step = row[0], row[1], row[2]
        if s1 <= x < s1 + step:
            offset = x - s1
            return d1 + offset
        
    return x


def loc_from_seeds(maps):
   
    seeds = maps['seeds']
 
    seed_soil = 'seed-to-soil map'
    soil_fert = 'soil-to-fertilizer map'
    fert_water = 'fertilizer-to-water map'
    water_light = 'water-to-light map'
    light_temp = 'light-to-temperature map'
    temp_humid = 'temperature-to-humidity map'
    humid_loc = 'humidity-to-location map'
    map_names = [seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]

    for seed in seeds:
        y = seed
        for map_name in map_names:
            y = map_val(y, maps[map_name])
        yield y


if __name__ == "__main__":


    with open('input.txt', 'r') as f:
        file_chunk = f.read()

    maps = parse_maps(file_chunk)

    print (min(list(loc_from_seeds(maps))))
