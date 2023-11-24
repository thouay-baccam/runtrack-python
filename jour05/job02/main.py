def draw_rectangle(width, height):
    # Affiche la première ligne du rectangle avec des '-'
    print('-' * width)

    # Affiche les lignes internes du rectangle avec '|'
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')

    # Affiche la dernière ligne du rectangle avec des '-'
    if height > 1:
        print('-' * width)

# Exemple avec draw_rectangle(10, 3)
draw_rectangle(10, 3)
