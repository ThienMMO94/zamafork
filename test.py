from init_script import basic_encrypt

def test_encrypt():
    encrypted = basic_encrypt("Test message for Zama")
    print("Encryption test passed if no error.")

test_encrypt()