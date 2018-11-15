def main(*args):
    return sorted(args)


print(main(0, 4 , 87, -4, 0.5, 7))

if __name__ == '__main__':
    assert main(3, 1, 2) == [1, 2, 3]
