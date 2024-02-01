from textblob import TextBlob

def analiza_sentymentu(tekst):
    analiza = TextBlob(tekst)
    sentyment = analiza.sentiment.polarity

    if sentyment > 0:
        return "Pozytywny"
    elif sentyment < 0:
        return "Negatywny"
    else:
        return "Neutralny"

if __name__ == "__main__":
    tekst_do_analizy = input("Wprowadź tekst do analizy sentymentu: ")
    wynik = analiza_sentymentu(tekst_do_analizy)
    print(f"Sentyment tekstu: {wynik}")
