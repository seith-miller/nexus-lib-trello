from trello_tool import TrelloWrapper, create_trello_tools
import os

API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")

if not API_KEY or not TOKEN:
    print("Please set TRELLO_API_KEY and TRELLO_TOKEN environment variables.")
    exit(1)

trello = TrelloWrapper(API_KEY, TOKEN)


def list_assigned_cards():
    cards = trello.list_cards_assigned_to_me()
    if not cards:
        print(f"No cards assigned to {trello.ai_name}.")
    else:
        print(f"Cards assigned to {trello.ai_name}:")
        for card in cards:
            print(
                f"- {card['name']} (Board: {card['board']}, List: {card['list']}, ID: {card['id']})"
            )


def update_card_status():
    card_id = input("Enter the card ID: ")
    list_name = input("Enter the new list name: ")
    result = trello.update_card_status(card_id, list_name)
    print(result)


def add_comment_to_card():
    card_id = input("Enter the card ID: ")
    comment = input("Enter your comment: ")
    result = trello.add_comment_to_card(card_id, comment)
    print(result)


def get_card_by_id():
    card_id = input("Enter the card ID: ")
    card = trello.get_card_by_id(card_id)
    if card:
        print(f"Card details: {card}")
    else:
        print(f"No card found with ID: {card_id}")


def get_card_by_name():
    card_name = input("Enter the card name: ")
    card = trello.get_card_by_name(card_name)
    if card:
        print(f"Card details: {card}")
    else:
        print(f"No card found with name: {card_name}")


def set_card_to_done():
    card_id = input("Enter the card ID: ")
    result = trello.set_card_to_done(card_id)
    print(result)


while True:
    print("\nWhat would you like to do?")
    print("1. List Cards Assigned to Me")
    print("2. Update Card Status")
    print("3. Add Comment to Card")
    print("4. Get Card by ID")
    print("5. Get Card by Name")
    print("6. Set Card to Done")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        list_assigned_cards()
    elif choice == "2":
        update_card_status()
    elif choice == "3":
        add_comment_to_card()
    elif choice == "4":
        get_card_by_id()
    elif choice == "5":
        get_card_by_name()
    elif choice == "6":
        set_card_to_done()
    elif choice == "7":
        break
    else:
        print("Invalid choice. Please try again.")

print("Goodbye!")
