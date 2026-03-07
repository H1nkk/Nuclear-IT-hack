import numpy as np
import random

from Source.Backend.TestGenerator import test_all_registers


# Runs verification on the Registry block
# Return entries:
#   "Results" : list[RegistryTestStatus : int]]
def run_tests() -> dict:

    # Test logic

    # PLACE HOLDER
    results: dict = {}

    all_addr = list(range(0x0000, 0x0010))
    random.shuffle(all_addr)
    results["Results"] = test_all_registers(all_addr)

    return results


def main():
    print(run_tests())


if __name__ == "__main__":
    main()
