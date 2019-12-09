# Return the maximum number of monster names from MONSTERS that can be created from characters in the supplied 'spell'

MONSTERS = '''
skeleton
ghost
jack
vampire
witch
mummy
zombie
werewolf
frankenstein
'''

def monster_check(spell, current_monster):
    letter_set = set(current_monster)
    return all([(spell.count(letter) >= current_monster.count(letter)) for letter in letter_set])

def monsters_helper(spell, monster_list, monster_number=0):
    current_monster = monster_list[0]
    current_monster_fits = monster_check(spell, current_monster)
    if len(monster_list) == 1:
        if current_monster_fits:
            spell2 = spell
            for x in [y for y in current_monster]:
                spell2 = spell2.replace(x, "", 1)
            return monsters_helper(spell2, monster_list, monster_number + 1)
        else:
            return monster_number
    elif current_monster_fits:
        spell2 = spell
        for x in [y for y in current_monster]:
            spell2 = spell2.replace(x, "", 1)
        return max(monsters_helper(spell2, monster_list, monster_number + 1),
                   monsters_helper(spell, monster_list[1:], monster_number))
        # must branch call itself recursively for cases where current_monster is added or not added
    else:
        return monsters_helper(spell, monster_list[1:], monster_number)

def halloween_monsters(spell: str)-> int:
    monster_list = MONSTERS.split("\n")[1:10]
    return monsters_helper(spell, monster_list)

print(halloween_monsters('casjokthg'))
print(halloween_monsters("ywzuqinthogjprkcvywzrihbxcnistmwqdjkzefkmcersbyxoixksffzhuxcuqageeaypgmtwpljnqflahmsord"))
