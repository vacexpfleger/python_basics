def txtRead(path):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError as error:
        return "File not found"
    except Exception as error:
        return "Loading failed"
    finally:
        file.close()
    return text


def charFrequency(string):
    frequency = list({n: string.count(n) for n in set(string)}.items())
    frequency.sort(reverse=True, key=lambda y: y[1])
    print(f"Věta: {string}\nČetnost výskytu písmen:")
    for i in frequency:
        print(i)


charFrequency(txtRead('file.txt'))
