from .models import db, Item, Pokemon
from datetime import date
from flask.cli import AppGroup

seed_commands = AppGroup('seed')

def seed_items():
    item1 = Item(
        name = 'Potion',
        happiness = 3,
        image_url = '../../../pokedex-refactor/backend/public/images/pokemon_potion.svg',
        price = 10,
        pokemon_id = 1
    )

    item2 = Item(
        name = 'berry',
        happiness = 5,
        image_url = '../../../pokedex-refactor/backend/public/images/pokemon_berry.svg',
        price = 100,
        pokemon_id = 2
    )

    item3 = Item(
        name = 'pokeball',
        happiness = 1,
        image_url = '../../../pokedex-refactor/backend/public/images/pokeball.svg',
        price = 14,
        pokemon_id = 3
    )

    return [item1, item2, item3]

def seed_pokemons():
    pokemon1 = Pokemon(
        number = 1,
        attack = 5,
        defense = 5,
        image_url = 'data:image/jpeg;base64,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',
        name = 'Bulbasaur',
        type = 'grass',
        item_id = 1
    )
    pokemon2 = Pokemon(
        number = 2,
        attack = 10,
        defense = 10,
        image_url = 'data:image/jpeg;base64,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',
        name = 'Ivysaur',
        type = 'grass',
        item_id = 2
    )
    pokemon3 = Pokemon(
        number = 3,
        attack = 15,
        defense = 15,
        image_url = 'data:image/jpeg;base64,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',
        name = 'Venusaur',
        type = 'grass',
        item_id = 3
    )

    return [pokemon1, pokemon2, pokemon3]

@seed_commands.command('all')
def seed():
    items = seed_items()
    pokemons = seed_pokemons()

    for i in range (0, 3):
        db.session.add(pokemons[i])
        db.session.add(items[i])

    db.session.commit()
    print('FILES SUCCESFuLLY SEEDED')

def undo_items():
    db.session.execute('DELETE FROM items;')
    db.session.commit()
    print('ITEMS REMOVED FROM DB')

def undo_pokemons():
    db.session.execute('DELETE FROM pokemons;')
    db.session.commit()
    print('POKEMONS REMOVED FROM DB')


