from trello import TrelloClient
from langchain.tools import Tool
from typing import List, Dict, Optional
import os


class TrelloWrapper:
    def __init__(self, api_key: str, token: str):
        self.client = TrelloClient(api_key=api_key, token=token)
        self.ai_name = os.getenv("AI_AGENT_NAME")
        if not self.ai_name:
            raise ValueError("AI_AGENT_NAME environment variable not set")

    def list_cards_assigned_to_me(self) -> List[Dict]:
        label_to_find = f"assigned to {self.ai_name}"
        my_cards = []
        for board in self.client.list_boards():
            for card in board.all_cards():
                if any(
                    label.name.lower() == label_to_find.lower() for label in card.labels
                ):
                    my_cards.append(
                        {
                            "id": card.id,
                            "name": card.name,
                            "list": card.get_list().name,
                            "board": board.name,
                        }
                    )
        return my_cards

    def update_card_status(self, card_id: str, list_name: str) -> str:
        card = self.client.get_card(card_id)
        board = card.board
        new_list = next(
            (l for l in board.list_lists() if l.name.lower() == list_name.lower()), None
        )
        if new_list:
            card.change_list(new_list.id)
            return f"Moved card '{card.name}' to list '{new_list.name}'"
        else:
            return f"List '{list_name}' not found on board"

    def add_comment_to_card(self, card_id: str, comment: str) -> str:
        card = self.client.get_card(card_id)
        card.comment(comment)
        return f"Added comment to card '{card.name}'"

    def get_card_by_id(self, card_id: str) -> Optional[Dict]:
        try:
            card = self.client.get_card(card_id)
            return {
                "id": card.id,
                "name": card.name,
                "description": card.description,
                "list": card.get_list().name,
                "board": card.board.name,
            }
        except Exception:
            return None

    def get_card_by_name(self, card_name: str) -> Optional[Dict]:
        for board in self.client.list_boards():
            for card in board.all_cards():
                if card.name.lower() == card_name.lower():
                    return {
                        "id": card.id,
                        "name": card.name,
                        "description": card.description,
                        "list": card.get_list().name,
                        "board": board.name,
                    }
        return None

    def set_card_to_done(self, card_id: str) -> str:
        card = self.client.get_card(card_id)
        board = card.board
        done_list = next(
            (l for l in board.list_lists() if l.name.lower() == "done"), None
        )
        if done_list:
            card.change_list(done_list.id)
            return f"Moved card '{card.name}' to 'Done' list"
        else:
            return f"'Done' list not found on board '{board.name}'"


def create_trello_tools(api_key: str, token: str) -> List[Tool]:
    trello = TrelloWrapper(api_key, token)

    return [
        Tool(
            name="List Cards Assigned to Me",
            func=trello.list_cards_assigned_to_me,
            description="Lists all Trello cards assigned to this AI agent",
        ),
        Tool(
            name="Update Trello Card Status",
            func=trello.update_card_status,
            description="Moves a Trello card to a different list. Args: card_id, list_name",
        ),
        Tool(
            name="Add Comment to Trello Card",
            func=trello.add_comment_to_card,
            description="Adds a comment to a Trello card. Args: card_id, comment",
        ),
        Tool(
            name="Get Card by ID",
            func=trello.get_card_by_id,
            description="Gets details of a Trello card by its ID. Args: card_id",
        ),
        Tool(
            name="Get Card by Name",
            func=trello.get_card_by_name,
            description="Gets details of a Trello card by its name. Args: card_name",
        ),
        Tool(
            name="Set Card to Done",
            func=trello.set_card_to_done,
            description="Moves a Trello card to the 'Done' list. Args: card_id",
        ),
    ]
