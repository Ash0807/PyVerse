import numpy as np
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        water_level = np.array(heightMap, dtype = int)
        heightMap = np.array(heightMap, dtype = int)
        
        water_level[1:-1, 1:-1] = np.max(heightMap)
        water = 0
        while True:
            water_pad = np.pad(water_level, ((1, 1), (1, 1)))
            water_level = np.maximum(np.minimum(np.minimum(water_pad[0:-2, 1: -1], water_pad[2:, 1:-1]), np.minimum(water_pad[1:-1, 0:-2], water_pad[1:-1, 2:])), heightMap)

            w = np.sum(water_level - heightMap)
            if water == w:
                return int(w)
            water = w
