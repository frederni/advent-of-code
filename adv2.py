def parse_games(filename):
    with open('input2.txt', 'r') as f:
        games = f.readlines()
    games_overview = []
    for game in games:
        game_id = int(game.split(":")[0].split(" ")[1])
        cube_overview = {"game_id": game_id, "red": 0, "blue": 0, "green": 0}
        for game_set in game.split(":")[1].split(";"):
            for color in game_set.split(","):
                num_cube, cube_color = color.strip().split(" ")
                cube_overview[cube_color] = max(cube_overview[cube_color], int(num_cube))
        games_overview.append(cube_overview)
    return games_overview

def find_valid_games(games: list[dict], lim: dict) -> int: # First part
    invalid_games = set()
    for cube_overview in games:
        if any([cube_overview[col] > lim[col] for col in cube_overview.keys() if col != "game_id"]):
            # Game is not valid
            invalid_games.add(cube_overview["game_id"])
    return sum(set(range(1,101)) - invalid_games)

def sum_of_powers(games: list[dict]) -> int: # Second part
    game_powers = []
    for game in games:
        colors = [col for col in game.keys() if col != "game_id"]
        power = 1
        for col in colors:
            power *= game[col]
        game_powers.append(power)
    return sum(game_powers)
game_data = parse_games("input2.txt")

print(find_valid_games(game_data, {"red": 12, "blue": 14, "green": 13}))
print(sum_of_powers(game_data))
