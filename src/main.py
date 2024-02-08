import random
from enigma import PlugBoard, ALPHABET, Rotor, Reflector, EnigmaMachine

if __name__ == "__main__":
    plug_board = PlugBoard("BADC")
    # print(plug_board.alphabet)
    # print(plug_board.forward_map)
    # print(plug_board.backward_map)

    # encrypted_index = plug_board.forward(ALPHABET.index("A"))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[plug_board.backward(encrypted_index)]
    # print(decrypted)

    # rotor = Rotor("BADC", 1)

    # encrypted_index = rotor.forward(ALPHABET.index("A"))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[rotor.backward(encrypted_index)]
    # print(decrypted)

    # rotor.rotate()

    # encrypted_index = rotor.forward(ALPHABET.index("A"))
    # print(ALPHABET[encrypted_index])
    # decrypted = ALPHABET[rotor.backward(encrypted_index)]
    # print(decrypted)

    # r = Reflector("BADC")
    # i = r.reflect(ALPHABET.index("A"))
    # print(ALPHABET[i])

    get_random_alphabet = lambda: "".join(random.sample(ALPHABET, len(ALPHABET)))
    print(get_random_alphabet())
    p = PlugBoard(get_random_alphabet())
    r1 = Rotor(get_random_alphabet(), 3)
    r2 = Rotor(get_random_alphabet(), 2)
    r3 = Rotor(get_random_alphabet(), 1)

    r = list(ALPHABET)
    indexes = [i for i in range(len(ALPHABET))]
    for _ in range(int(len(indexes) / 2)):
        x = indexes.pop(random.randint(0, len(indexes) - 1))
        y = indexes.pop(random.randint(0, len(indexes) - 1))
        r[x], r[y] = r[y], r[x]
    reflector = Reflector("".join(r))

    machine = EnigmaMachine(p, [r1, r2, r3], reflector)
    s = "ATACK SILICON VALLEY"
    e = machine.encrypt(s)
    print(e)

    d = machine.decrypt(e)
    print(d)
