def generate_tests(test_addr: list):
    with open("./Source/Tests/GeneratedTests.py", "w") as f:

        f.write(
            "from Source.Backend.riscv_reg_block import reg_access\nimport random\n\n\nimport pytest\n\n\n"
        )

        for addr in test_addr:
            f.write(f"\
def test_register_{addr}(): \n\
    for test_input in range(0x0000, 0xFFFF): \n\
        writing = reg_access({addr}, test_input, 'write') \n\
        if not writing['ack']: \n\
            assert False \n\
\n\
        reading = reg_access({addr}, 0, 'read') \n\
        if not reading['ack']:  \n\
            assert False \n\
\n\
        if (test_input != reading['reg_value']): \n\
            assert False \n\
\n\
    assert True\n\n\n\
")


if __name__ == "__main__":
    all_addr = list(range(0x0000, 0x0010))
    generate_tests(all_addr)
