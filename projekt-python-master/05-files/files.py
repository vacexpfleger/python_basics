def read_file(filename):
    try:
        with open(filename) as f1:
            data = f1.read()
    except FileNotFoundError as error:
        return "File not found"
    except Exception as error:
        return "Doslo k nejakemu problemu pri otevirani souboru"
    finally:
        f1.close()
    return data

read_file("./python.txt")