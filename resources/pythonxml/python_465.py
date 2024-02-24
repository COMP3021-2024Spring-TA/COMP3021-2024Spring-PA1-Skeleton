class Solution:
    ans = 0
    def backtrack(self, tile_map):
        for key, value in tile_map.items():
            if value == 0:
                continue
            self.ans += 1
            tile_map[key] -= 1
            self.backtrack(tile_map)
            tile_map[key] += 1

    def numTilePossibilities(self, tiles: str) -> int:
        tile_map = dict()
        for tile in tiles:
            if tile not in tile_map:
                tile_map[tile] = 1
            else:
                tile_map[tile] += 1

        self.backtrack(tile_map)

        return self.ans