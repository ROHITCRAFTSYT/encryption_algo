def encrypt(text, shift):
    """
    Encrypts the given text using the Caesar cipher with the specified shift.
    
    Args:
        text (str): The plaintext to encrypt
        shift (int): The number of positions to shift each character
    
    Returns:
        str: The encrypted text
    """
    result = ""
    
    # Go through each character in the text
    for char in text:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # Get the ASCII code
            ascii_code = ord(char)
            
            # Handle uppercase letters (ASCII 65-90)
            if char.isupper():
                # Apply shift and use modulo to wrap around the alphabet
                shifted_code = ((ascii_code - 65 + shift) % 26) + 65
            # Handle lowercase letters (ASCII 97-122)
            else:
                # Apply shift and use modulo to wrap around the alphabet
                shifted_code = ((ascii_code - 97 + shift) % 26) + 97
                
            # Convert back to character and add to result
            result += chr(shifted_code)
        else:
            # Leave non-alphabetic characters unchanged
            result += char
    
    return result

def decrypt(text, shift):
    """
    Decrypts the given text using the Caesar cipher with the specified shift.
    
    Args:
        text (str): The ciphertext to decrypt
        shift (int): The number of positions that were used for encryption
    
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with a negative shift
    return encrypt(text, -shift)

def main():
    """
    Main function that provides a simple command-line interface.
    """
    print("=== Caesar Cipher Tool ===")
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            text = input("Enter the text to encrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Shift must be between 1 and 25.")
                    continue
                encrypted_text = encrypt(text, shift)
                print(f"\nEncrypted text: {encrypted_text}")
            except ValueError:
                print("Please enter a valid number for the shift.")
        
        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            try:
                shift = int(input("Enter the shift value (1-25): "))
                if shift < 1 or shift > 25:
                    print("Shift must be between 1 and 25.")
                    continue
                decrypted_text = decrypt(text, shift)
                print(f"\nDecrypted text: {decrypted_text}")
            except ValueError:
                print("Please enter a valid number for the shift.")
        
        elif choice == '3':
            print("Thank you for using the Caesar Cipher Tool. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()