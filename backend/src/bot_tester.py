from backend.src.bot_controller import get_response_character, choose_character_debug
from bot_controller import choose_character, CHARACTERS

selected_character = choose_character_debug("Thug")

while True:
    user_input = input("> ")
    response = get_response_character(user_input, selected_character)
    print(response)


