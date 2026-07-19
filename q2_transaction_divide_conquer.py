from dataclasses import dataclass
from time import perf_counter_ns
from typing import Callable, Optional


@dataclass
class Transaction:
    transaction_id: int
    customer_name: str
    product_name: str
    amount: float
    transaction_date: str

    def __str__(self) -> str:
        return (
            f"{self.transaction_id:<5} | {self.customer_name:<15} | "
            f"{self.product_name:<18} | RM{self.amount:>8.2f} | {self.transaction_date}"
        )


KeyFunction = Callable[[Transaction], int | float | str]


def sample_transactions() -> list[Transaction]: #**1
    return [
        Transaction(1050, "Aina", "Wireless Mouse", 59.90, "2026-01-12"),
        Transaction(1012, "Ben", "Keyboard", 129.00, "2026-01-05"),
        Transaction(1098, "Chloe", "USB-C Cable", 25.50, "2026-01-20"),
        Transaction(1007, "Daniel", "Laptop Stand", 89.90, "2026-01-02"),
        Transaction(1066, "Elaine", "Webcam", 149.00, "2026-01-15"),
        Transaction(1033, "Farid", "Headphones", 199.90, "2026-01-08"),
        Transaction(1081, "Grace", "Power Bank", 79.90, "2026-01-18"),
        Transaction(1024, "Hana", "HDMI Cable", 32.00, "2026-01-07"),
        Transaction(1045, "Ivan", "Monitor Arm", 169.00, "2026-01-11"),
        Transaction(1072, "Jia", "Phone Charger", 45.00, "2026-01-16"),
        Transaction(1019, "Kumar", "Mouse Pad", 18.90, "2026-01-06"),
        Transaction(1091, "Lina", "Tablet Cover", 55.00, "2026-01-19"),
        Transaction(1003, "Mei", "Bluetooth Speaker", 120.00, "2026-01-01"),
        Transaction(1060, "Noah", "SSD Drive", 299.00, "2026-01-14"),
        Transaction(1039, "Olivia", "Desk Lamp", 74.50, "2026-01-09"),
    ]


def display_transactions(transactions: list[Transaction], title: str) -> None:
    print(f"\n{title}")
    print("-" * 76)
    print("ID    | Customer        | Product            | Amount     | Date")
    print("-" * 76)
    for transaction in transactions:
        print(transaction)


def merge_sort(##3
    transactions: list[Transaction],
    key: KeyFunction = lambda transaction: transaction.transaction_id,
    counter: Optional[dict[str, int]] = None,
) -> list[Transaction]:
    if counter is not None:
        counter["calls"] += 1

    # Base case: a list with 0 or 1 item is already sorted
    if len(transactions) <= 1:
        return transactions[:]

    # Divide: split the list into two halves
    middle = len(transactions) // 2

    # Conquer: recursively sort both halves
    left_half = merge_sort(transactions[:middle], key, counter)
    right_half = merge_sort(transactions[middle:], key, counter)

    # Combine: merge the two sorted halves
    return merge(left_half, right_half, key)


def merge(left: list[Transaction], right: list[Transaction], key: KeyFunction) -> list[Transaction]:
    sorted_items: list[Transaction] = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if key(left[left_index]) <= key(right[right_index]):
            sorted_items.append(left[left_index])
            left_index += 1
        else:
            sorted_items.append(right[right_index])
            right_index += 1

    sorted_items.extend(left[left_index:])
    sorted_items.extend(right[right_index:])
    return sorted_items


def binary_search(#**2
    transactions: list[Transaction],
    target_id: int,
    low: int = 0,
    high: Optional[int] = None,
) -> Optional[Transaction]:
    if high is None:
        high = len(transactions) - 1

    if low > high:
        return None

    middle = (low + high) // 2
    middle_transaction = transactions[middle]

    if middle_transaction.transaction_id == target_id:
        return middle_transaction
    if target_id < middle_transaction.transaction_id:
        return binary_search(transactions, target_id, low, middle - 1)
    return binary_search(transactions, target_id, middle + 1, high)


def linear_search(transactions: list[Transaction], target_id: int) -> Optional[Transaction]:
    for transaction in transactions:
        if transaction.transaction_id == target_id:
            return transaction
    return None


def run_performance_comparison(target_id: int) -> dict[str, float]:
    transactions = sample_transactions()
    counter = {"calls": 0}

    sort_start = perf_counter_ns()
    sorted_transactions = merge_sort(transactions, counter=counter)
    sort_time = perf_counter_ns() - sort_start

    binary_start = perf_counter_ns()
    binary_result = binary_search(sorted_transactions, target_id)
    binary_time = perf_counter_ns() - binary_start

    linear_start = perf_counter_ns()
    linear_result = linear_search(transactions, target_id)
    linear_time = perf_counter_ns() - linear_start

    return {
        "merge_sort_ns": sort_time,
        "binary_search_ns": binary_time,
        "linear_search_ns": linear_time,
        "recursive_calls": counter["calls"],
        "binary_found": binary_result is not None,
        "linear_found": linear_result is not None,
    }


def insert_transaction(transactions: list[Transaction]) -> None:
    transaction_id = int(input("Transaction ID: ").strip())
    customer_name = input("Customer name: ").strip()
    product_name = input("Product name: ").strip()
    amount = float(input("Amount: RM").strip())
    transaction_date = input("Transaction date (YYYY-MM-DD): ").strip()
    transactions.append(Transaction(transaction_id, customer_name, product_name, amount, transaction_date))
    print("Transaction inserted successfully.")


def choose_sort_key() -> tuple[str, KeyFunction]:
    print("1. Sort by transaction ID")
    print("2. Sort by amount")
    choice = input("Choose sort attribute: ").strip()
    if choice == "2":
        return "amount", lambda transaction: transaction.amount
    return "transaction ID", lambda transaction: transaction.transaction_id


def print_complexity_table() -> None:
    print("\nTIME COMPLEXITY SUMMARY")
    print("-" * 48)
    print(f"{'Operation':<22} | {'Best':<8} | {'Average/Worst':<14}")
    print("-" * 48)
    print(f"{'Merge Sort':<22} | {'O(n log n)':<8} | {'O(n log n)':<14}")
    print(f"{'Binary Search':<22} | {'O(1)':<8} | {'O(log n)':<14}")
    print(f"{'Linear Search':<22} | {'O(1)':<8} | {'O(n)':<14}")


def menu() -> None:
    transactions = sample_transactions()
    sorted_transactions: list[Transaction] = []
    choice = ""

    while choice != "0":
        print("\nTRANSACTION SYSTEM MENU")
        print("1. Display all transactions")
        print("2. Sort transactions using Merge Sort")
        print("3. Search transaction using Binary Search")
        print("4. Search transaction using Linear Search")
        print("5. Insert transaction")
        print("6. Display time complexity table")
        print("0. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_transactions(transactions, "CURRENT TRANSACTIONS")
        elif choice == "2":
            label, key = choose_sort_key()
            counter = {"calls": 0}
            sorted_transactions = merge_sort(transactions, key=key, counter=counter)
            display_transactions(sorted_transactions, f"TRANSACTIONS SORTED BY {label.upper()}")
            print(f"Recursive calls made by Merge Sort: {counter['calls']}")
        elif choice == "3":
            sort_start = perf_counter_ns()
            id_sorted_transactions = merge_sort( #**4
                transactions,
                key=lambda transaction: transaction.transaction_id,
            )
            sort_time = perf_counter_ns() - sort_start
            target_id = int(input("Enter transaction ID: ").strip())
            search_start = perf_counter_ns()
            result = binary_search(id_sorted_transactions, target_id)
            search_time = perf_counter_ns() - search_start
            print(result if result else "Transaction not found.")
            print(f"Merge Sort preparation time (ns): {sort_time}")
            print(f"Binary Search time (ns)         : {search_time}")
        elif choice == "4":
            target_id = int(input("Enter transaction ID: ").strip())
            search_start = perf_counter_ns()
            result = linear_search(transactions, target_id)
            search_time = perf_counter_ns() - search_start
            print(result if result else "Transaction not found.")
            print(f"Linear Search time (ns): {search_time}")
        elif choice == "5":
            insert_transaction(transactions)
        elif choice == "6":
            print_complexity_table()
        elif choice == "0":
            print("Goodbye.")
        else:
            print("Invalid option.")


if __name__ == "__main__":
    menu()
