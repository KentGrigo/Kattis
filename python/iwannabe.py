import operator

class Pokemon:
    def __init__(self, attack, defense, health):
        self.attack = attack
        self.defense = defense
        self.health = health

def selectTopPokemons(pokemons, attribute, numberOfTopPokemonToSelect):
    pokemons.sort(key = operator.attrgetter(attribute), reverse=True)
    return list(pokemons[:numberOfTopPokemonToSelect])


numberOfPokemon, numberOfTopPokemonToSelect = list(map(int, input().split()))
pokemons = []
for _ in range(numberOfPokemon):
    attack, defense, health = list(map(int, input().split()))
    pokemon = Pokemon(attack, defense, health)
    pokemons.append(pokemon)

topPokemons = set()
topPokemons.update(selectTopPokemons(pokemons, "attack", numberOfTopPokemonToSelect))
topPokemons.update(selectTopPokemons(pokemons, "defense", numberOfTopPokemonToSelect))
topPokemons.update(selectTopPokemons(pokemons, "health", numberOfTopPokemonToSelect))
numberOfTopPokemon = len(topPokemons)
print(numberOfTopPokemon)
