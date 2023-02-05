def caesar(input_text,shift_amount,direction):
    result_message = ""
    for single_character in secret_message:
        current_index = list_characters.index(single_character)
        if direction == "encode":
            if current_index + shift < 25:
                result_message += str(list_characters[current_index + shift])
            else:
                result_message += str(list_characters[current_index + shift - 26])
        elif direction == "decode":
            result_message += str(list_characters[current_index - shift])

    return result_message

secret_message = input("Enter the secret message!!: ").upper()
list_characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
shift = int(input("Enter the amount we would want to shift by: "))
result_message = ""
direction = input("encode or decode : ").lower()

print(f"Output of the cypher is : {caesar(input_text=secret_message,shift_amount=shift,direction=direction)}")

