def number_spells(spells):
    numbered = []
    for i, spell in enumerate(spells, 1):
        numbered.append(f"{i}. {spell}")
    return numbered
