def eskerrik_asko(momentua):
    if momentua == "goizean":
        return "Egun on"
    elif momentua == "arratsaldean":
        return "Arratsaldeon ondo"
    elif momentua == "gauero":
        return "Gabon on"
    else:
        return ""

print(eskerrik_asko("arratsaldean"))

def eskerrik_asko2(momentua):
    return {
        "goizean": "Egun on",
        "arratsaldean": "Arratsalde ondo",
        "gauero": "Gabon on"
    }[momentua]

print(eskerrik_asko2("arratsaldean"))