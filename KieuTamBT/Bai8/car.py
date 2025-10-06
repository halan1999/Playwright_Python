class Car:
    def __init__(self, brandName, model ):
        self.brandName = brandName
        self.model = model

vinfast = Car("Vinfast","VF5")
honda = Car("Honda","City")
print(f"Hãng xe: {vinfast.brandName} có model {vinfast.model}")
print(f"Hãng xe: {honda.brandName} có model {honda.model}")
