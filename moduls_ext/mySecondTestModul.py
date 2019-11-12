def bye():
    print("Nara")


def add(*args):
    return sum(args)


if __name__ == "__main__":
    print("Wywolano z modulu")
else:
    print("Wywolano z programu")

# print(__name__)
