def charFrequency(string):
    frequency = list({n: string.count(n) for n in set(string)}.items())
    frequency.sort(reverse=True, key=lambda y: y[1])
    print(f"Věta: {string}\nČetnost výskytu písmen:")
    for i in frequency:
        print(i)


sentence = "Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech."
charFrequency(sentence)
