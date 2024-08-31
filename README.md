# nexus-lib-trello

A Trello tool library for AI agents.

## Features

- List assigned cards
- Update card status
- Add comments to cards
- Get card details
- Set cards to "Done"

## Setup

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables:
export TRELLO_API_KEY=your_key
export TRELLO_TOKEN=your_token
export AI_AGENT_NAME=agent_name

## Usage

```python
from trello_tool import create_trello_tools

tools = create_trello_tools(API_KEY, TOKEN)
# Use tools in your AI agent
```
