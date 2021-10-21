def txt_read(path, encoding):
    try:
        with open(path, encoding=encoding) as file:
            data = file.read()
    except FileNotFoundError as error:
        return "File not found"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri otevirani souboru: {error}"
    finally:
        file.close()
    return data


def txt_write(path, data="", encoding="utf-8"):
    try:
        with open(path, mode="w", encoding=encoding) as file:
            file.write(data)
    except FileNotFoundError as error:
        print(f"File not found: {error}")
        return False
    except Exception as error:
        print(f"Doslo k nejakemu problemu pri otevirani souboru: {error}")
        return False
    finally:
        file.close()
    return True


txt = txt_read("./python.txt", "utf-8")
print(txt_write("./novy.txt", txt))

import json

def json_read(path, encoding="utf-8"):
    try:
        with open(path, encoding=encoding) as file:
            data = json.load(file)
    except FileNotFoundError as error:
        return "File not found"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri otevirani souboru: {error}"
    finally:
        file.close()
    return data

print(json_read("test.json"))
print(type(json_read("test.json")))

def json_write(path, data, encoding="utf-8"):
    try:
        with open(path, mode="w", encoding=encoding) as file:
            json.dump(data, file, indent=3)
    except FileNotFoundError as error:
        print(f"File not found: {error}")
        return False
    except Exception as error:
        print(f"Doslo k nejakemu problemu pri otevirani souboru: {error}")
        return False
    finally:
        file.close()
    return True


input = json_read("test.json")
print(json_write("output.json",input))


def csv_read(path, encoding="utf-8"):
    try:
        with open(path, encoding=encoding) as file:
            data = json.load(file)
    except FileNotFoundError as error:
        return "File not found"
    except Exception as error:
        return f"Doslo k nejakemu problemu pri otevirani souboru: {error}"
    finally:
        file.close()
    return data