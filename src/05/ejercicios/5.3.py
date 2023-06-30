class Bihotza:
    def __init__(hau, matrícula):
        hau._matrícula = matrícula

    @property
    def matrícula (hau):
        return hau._matrícula

    @matrícula.setter
    def matrícula (hau, matrícula):
        hau._matrícula = matrícula

    def abiarazi (hau):
        print("Abiarazten ", hau._matrícula)


class Kotxea(Bihotza):
    def __init__(hau, matrícula, modeloa, kolorea):
        super().__init__(matrícula)
        hau._modeloa = modeloa
        hau._kolorea = kolorea

    def info (hau):
        return f"{hau.matrícula} {hau._modeloa} {hau._kolorea}";


kotxea = Kotxea("0042ASI", "Opel Corsa", "Zuria")
kotxea.abiarazi()
print(kotxea.info())