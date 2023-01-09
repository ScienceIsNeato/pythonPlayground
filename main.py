# any imports needed up here

def entry_point():
    print("Entering main method")

    return True


if __name__ == '__main__':
    ret = entry_point()

    if ret:
        print("program completed successfully")