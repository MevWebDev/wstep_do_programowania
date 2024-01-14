def invert(my_dict):
    dinv = {}

    for key, value in my_dict.items():
        if value not in dinv:
            # Jeśli wartość nie istnieje w dinv, utwórz nową listę dla tej wartości
            dinv[value] = [key]
        else:
            # Jeśli wartość już istnieje w dinv, dodaj klucz do istniejącej listy
            dinv[value].append(key)

    return dinv

# Przykład użycia
my_dict = {'franek': 2, 'szymdym': 2, 'kuba': 3, 'bajczel': 5, 'grigor':2}
result = invert(my_dict)
print(result)