from Source.Backend.riscv_reg_block import reg_access

import random

all_addr = list(range(0x0000, 0x0010))
print(f"Amount = {len(all_addr)}")


def run_registry_tests(test_addr: list) -> dict:
    results = {}

    # random.shuffle(test_addr)
    for addr in test_addr:
        results[addr] = []

        print(f"- Testing address {addr}")

        for test_input in range(0x0000, 0xFFFF):
            writing = reg_access(addr, test_input, "write")
            if not writing["ack"]:
                print(
                    f"Addr {addr}, test value {test_input} - Error ack = false when writing"
                )
                results[addr].append("Failed to write!")
                continue

            reading = reg_access(addr, 0, "read")
            if not reading["ack"]:
                print(
                    f"Addr {addr}, test value {test_input} - Error ack = false when reading"
                )
                results[addr].append("Failed to read!")
                # Number 4 Bug 1
                continue

            if test_input != reading["reg_value"]:
                print(
                    f"Addr {addr}, test value {test_input} - Error reading data != writing data. Read value: {reading['reg_value']}"
                )
                results[addr].append("Read data does not match written data!")
                # Number 2 Bug 2
                continue

    # Overflow checks
    for addr in test_addr:
        failed = False

        test_input = 0xFFFFFF
        expected_output = 0xFFFF
        writing = reg_access(addr, test_input, "write")
        if not writing["ack"]:
            print(
                f"Addr {addr}, test value {test_input} - Error ack = false when writing"
            )
            failed = True
            continue

        reading = reg_access(addr, 0, "read")
        if not reading["ack"]:
            print(
                f"Addr {addr}, test value {test_input} - Error ack = false when reading"
            )
            failed = True
            continue

        if expected_output != reading["reg_value"]:
            print(
                f"Addr {addr}, test value {test_input} - Error reading data != expected output. Read value: {reading['reg_value']}"
            )
            failed = True
            continue

        if failed:
            results[addr].append("Overflow!")

    return results


if __name__ == "__main__":
    run_registry_tests(all_addr)
