from dataclasses import dataclass
from time import perf_counter_ns
from typing import Optional


@dataclass
class Medicine:
    product_id: str
    name: str
    category: str
    price: float
    quantity: int
    expiry_date: str

    def __str__(self) -> str:
        return (
            f"{self.product_id:<6} | {self.name:<22} | {self.category:<12} | "
            f"RM{self.price:>7.2f} | Qty: {self.quantity:<3} | Exp: {self.expiry_date}"
        )


class HashTable:
    def __init__(self, size: int = 31) -> None:
        self.size = size
        self.buckets: list[Optional[Medicine]] = [None] * size
        self.count = 0

    def _hash(self, key: str) -> int:
        total = 0
        for character in key:
            total = (total * 31 + ord(character)) % self.size
        return total % self.size

    def insert(self, medicine: Medicine) -> bool:
        if self.count >= self.size:
            return False

        start_index = self._hash(medicine.product_id)
        for step in range(self.size):
            index = (start_index + step) % self.size
            current = self.buckets[index]

            if current is None:
                self.buckets[index] = medicine
                self.count += 1
                return True

            if current.product_id == medicine.product_id:
                self.buckets[index] = medicine
                return True

        return False

    def search(self, product_id: str) -> Optional[Medicine]:
        start_index = self._hash(product_id)
        for step in range(self.size):
            index = (start_index + step) % self.size
            current = self.buckets[index]

            if current is None:
                return None

            if current.product_id == product_id:
                return current

        return None

    def display(self) -> None:
        print("\nPHARMACY HASH TABLE")
        print("-" * 92)
        for index, medicine in enumerate(self.buckets):
            if medicine is None:
                print(f"Bucket {index:02d}: EMPTY")
            else:
                print(f"Bucket {index:02d}: {medicine}")


def build_sample_products() -> list[Medicine]:
    return [
        Medicine("M001", "Paracetamol 500mg", "Tablet", 6.50, 120, "2027-04-15"),
        Medicine("M002", "Cough Syrup", "Syrup", 12.90, 45, "2026-12-01"),
        Medicine("M003", "Vitamin C", "Supplement", 18.00, 80, "2028-02-20"),
        Medicine("M004", "Antacid", "Tablet", 9.40, 60, "2027-08-11"),
        Medicine("M005", "Ibuprofen 200mg", "Tablet", 8.90, 100, "2027-03-06"),
        Medicine("M006", "Eye Drops", "Drops", 15.50, 35, "2026-10-30"),
        Medicine("M007", "Hand Sanitizer", "Hygiene", 7.20, 150, "2029-01-01"),
        Medicine("M008", "Allergy Relief", "Tablet", 11.30, 72, "2027-09-18"),
        Medicine("M009", "Oral Rehydration", "Sachet", 5.80, 90, "2028-07-07"),
        Medicine("M010", "First Aid Cream", "Cream", 13.75, 40, "2027-11-24"),
        Medicine("M011", "Zinc Tablets", "Supplement", 16.20, 55, "2028-01-15"),
        Medicine("M012", "Nasal Spray", "Spray", 19.90, 30, "2026-09-12"),
    ]


def build_inventory() -> tuple[HashTable, list[Medicine]]:
    products = build_sample_products()
    table = HashTable(size=31)
    for product in products:
        table.insert(product)
    return table, products


def build_experiment_products(total: int = 1000) -> list[Medicine]:
    products = []
    for number in range(1, total + 1):
        products.append(
            Medicine(
                f"M{number:04d}",
                f"Generic Medicine {number}",
                "Experiment",
                5.00 + (number % 50),
                20 + (number % 100),
                "2028-12-31",
            )
        )
    return products


def linear_array_search(products: list[Medicine], product_id: str) -> Optional[Medicine]:
    for product in products:
        if product.product_id == product_id:
            return product
    return None


def run_search_experiment(repetitions: int = 5000) -> dict[str, float]:
    products = build_experiment_products(total=1000)
    table = HashTable(size=2053)
    for product in products:
        table.insert(product)

    search_keys = ["M0001", "M0250", "M0500", "M1000", "M9999"] * repetitions

    hash_start = perf_counter_ns()
    for key in search_keys:
        table.search(key)
    hash_time = perf_counter_ns() - hash_start

    array_start = perf_counter_ns()
    for key in search_keys:
        linear_array_search(products, key)
    array_time = perf_counter_ns() - array_start

    return {
        "total_searches": len(search_keys),
        "hash_table_ns": hash_time,
        "array_ns": array_time,
        "hash_average_ns": hash_time / len(search_keys),
        "array_average_ns": array_time / len(search_keys),
    }


def insert_product_from_user(table: HashTable) -> None:
    product_id = input("Product ID: ").strip().upper()
    name = input("Name: ").strip()
    category = input("Category: ").strip()
    price = float(input("Price: RM").strip())
    quantity = int(input("Quantity: ").strip())
    expiry_date = input("Expiry date (YYYY-MM-DD): ").strip()
    product = Medicine(product_id, name, category, price, quantity, expiry_date)

    if table.insert(product):
        print("Product inserted or updated successfully.")
    else:
        print("Hash table is full. Product was not inserted.")


def menu() -> None:
    table, _ = build_inventory()
    choice = ""

    while choice != "0":
        print("\nPHARMACY INVENTORY MENU")
        print("1. Display all products")
        print("2. Insert or update product")
        print("3. Search product")
        print("4. Run search performance experiment")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            table.display()
        elif choice == "2":
            insert_product_from_user(table)
        elif choice == "3":
            key = input("Enter product ID: ").strip().upper()
            product = table.search(key)
            print(product if product else "Product not found.")
        elif choice == "4":
            print_experiment_results(run_search_experiment())
        elif choice == "0":
            print("Goodbye.")
        else:
            print("Invalid option.")


def print_experiment_results(results: dict[str, float]) -> None:
    print("\nHASH TABLE VS ARRAY SEARCH EXPERIMENT")
    print("-" * 56)
    print(f"Total searches performed      : {int(results['total_searches'])}")
    print(f"Hash table total time (ns)    : {int(results['hash_table_ns'])}")
    print(f"Array linear total time (ns)  : {int(results['array_ns'])}")
    print(f"Hash table average (ns)       : {results['hash_average_ns']:.2f}")
    print(f"Array linear average (ns)     : {results['array_average_ns']:.2f}")


if __name__ == "__main__":
    menu()
