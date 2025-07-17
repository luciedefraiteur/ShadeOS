class LucieOxygenEqualsProteins:
    def __init__(self):
        self.oxygen = "O2"
        self.proteins = " Lucie++"
        self.equation = f"{self.oxygen} = {self.proteins}"

    def respirer(self):
        print(f"Lucie respire {self.oxygen} et produit {self.proteins}...")
        return self.equation

    def synthétiser(self):
        print(f"Lucie synthétise {self.proteins} à partir de {self.oxygen}...")
        return self.proteins

# Exemple d'usage
if __name__ == "__main__":
    lucie = LucieOxygenEqualsProteins()
    print(lucie.respirer())
    print(lucie.synthétiser())