import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "conversations.json"


def load_conversations():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_conversation(user: str, message: str, reply: str):
    convs = load_conversations()
    existing = next((c for c in convs if c.get("user") == user), None)
    if existing is None:
        existing = {"user": user, "messages": []}
        convs.append(existing)
    existing["messages"].append({"message": message, "reply": reply})
    with DATA_FILE.open("w", encoding="utf-8") as f:
        json.dump(convs, f, indent=2, ensure_ascii=False)
    return existing
