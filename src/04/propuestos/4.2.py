def agurtu(momentua):
    if momentua == "goizean":
        return "Egun on"
    elif momentua == "arratsaldean":
        return "Arratsalde on"
    elif momentua == "gauero":
        return "Gabon on"
    else:
        return ""

print(eskerrik_asko("arratsaldean"))

# beste bertsio bat
def agurtu2(momentua):
    return {
        "goizean": "Egun on",
        "arratsaldean": "Arratsalde on",
        "gauero": "Gabon on"
    }[momentua]

print(eskerrik_asko2("arratsaldean"))