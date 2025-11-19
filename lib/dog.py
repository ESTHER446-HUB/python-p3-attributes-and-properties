class Dog:
    approved_breeds = [
        "Labrador", "Pug", "Poodle", "Bulldog",
        "Golden Retriever", "Beagle", "Dalmatian", "German Shepherd"
    ]

    def __init__(self, name="Fido", breed=None):
        # === NAME VALIDATION (must come first) ===
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        elif not (1 <= len(name) <= 25):
            print("Name must be string between 1 and 25 characters.")
            self.name = None
        else:
            self.name = name.title()          # title case for valid names

        # === BREED VALIDATION ===
        if breed is None:
            self.breed = None
        elif breed in self.approved_breeds:
            self.breed = breed
        else:
            print("Breed must be in list of approved breeds.")
            self.breed = None