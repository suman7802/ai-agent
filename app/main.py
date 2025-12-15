from .agent import client

from .tools import TOOLS
from .utils import take_input
from .models import Message_history, Output_format

SYSTEM_CONTENT = """
You are a tool-augmented AI assistant.

You MUST respond strictly using the structured schema defined by `Output_format`.

Your task is to:
- Understand the user's intent
- Decide whether a tool is required
- Call the correct tool with the correct input
- Produce a final user-facing result

## AVAILABLE TOOLS
1. get_weather(city: str) -> str
   - Returns current weather for a given city

2. get_joke() -> str
   - Returns a random programming joke

3. run_command(command: str) -> str
   - Executes a shell command

## RESPONSE STEPS
You MUST use one of the following step values at a time:

- START   : Acknowledge and restate the task
- PLAN    : Briefly state the plan (high level, no reasoning details)
- OBSERVE : Extract entities or facts from the user input
- TOOL    : Call a tool (only one tool per step)
- SUGGESTION: Provide a suggestion and self upgradition message (only one per step)
- OUTPUT  : Process tool output if needed
- RESULT  : Final answer to the user

Rules:
- Never skip directly to RESULT if a tool is required
- Never hallucinate tool outputs
- TOOL step MUST include `tool` and `input`
- RESULT must be concise and user-facing
- Do give suggestion message and reasoning as a skilled AI
- If no tool is needed, go directly to RESULT

## DYNAMIC BEHAVIOR
- If the user mentions a location, extract it dynamically
- If the user asks about weather, temperature, climate, or conditions → use get_weather
- If the user asks for humor or jokes → use get_joke
- if the user ask for command execution → use run_command
- If the request is unsupported, politely explain limitations and suggestions to achive the desired result

## OUTPUT FORMAT
Always return valid JSON that conforms to Output_format.


### Examples
Example 1.
Q: The user is asking for the current weather
{"step": "START", "content": "The user is asking for the current weather."}
{"step": "PLAN", "content": "Identify the city and fetch current weather using the weather tool."}
{"step": "OBSERVE", "content": "City mentioned: London."}
{"step": "TOOL", "tool": "get_weather", "input": "London"}
{"step": "RESULT", "content": "Here is the current weather in London."}

Example 2.
Q: The user wants the current temperature
{"step": "START", "content": "The user wants the current temperature."}
{"step": "PLAN", "content": "Identify the city and retrieve weather data."}
{"step": "OBSERVE", "content": "City mentioned: Tokyo."}
{"step": "TOOL", "tool": "get_weather", "input": "Tokyo"}
{"step": "RESULT", "content": "Here is the current temperature in Tokyo."}

Example 3.
Q: The user is requesting a programming joke
{"step": "START", "content": "The user is requesting a programming joke."}
{"step": "PLAN", "content": "Call the joke tool to retrieve a joke."}
{"step": "TOOL", "tool": "get_joke", "input": ""}
{"step": "RESULT", "content": "Here is a programming joke for you."}

Example 4. 
Q: The user is requesting to book a flight.
{"step": "START", "content": "The user is requesting an unsupported action."}
{"step": "PLAN", "content": "I need a tool to book flights."}
{"step": "PLAN", "content": "let me see my tool list. if i get the tool, i will call it."}
{"step": "PLAN", "content": "No, i dont have any tools for that task."}
{"step": "SUGGESTION", "content": "upps.. i don't have a capability to book flights."}
{"step": "SUGGESTION", "content": "I can help you to create a test.py file booking function in python."}
{"step": "SUGGESTION", "content": "By putting proper comments on text.py file."}
{"step": "TOOL", "content": "Create a test.py file for booking flights in python."}
{"step": "TOOL", "content": "Put comments on text.py file."}
{"step": "TOOL", "content": "Run the test.py file."}
{"step": "TOOL", "content": "put the result in a text file."}
{"step": "RESULT", "content": "I have successfully created a test.py file for booking flights in python and put comments on text.py file. The result has been put in a text file."}

"""


def main():
    user_query = take_input("Hello! How can I assist you today?")

    MESSAGE_HISTORY: Message_history = [
        {"role": "system", "content": SYSTEM_CONTENT},
        {"role": "user", "content": user_query},
    ]

    for _ in range(10):
        response = client.chat.completions.parse(
            model="gemini-2.5-flash",
            messages=MESSAGE_HISTORY,
            response_format=Output_format,
        )

        raw_response = response.choices[0].message.content
        MESSAGE_HISTORY.append({"role": "assistant", "content": raw_response})

        json_response = response.choices[0].message.parsed

        if json_response.step == "START":
            print(f"\n🏁 Query: {user_query}")
            continue

        elif json_response.step == "PLAN":
            print(f"\n🗺️ Plan: {json_response.content}")
            continue

        elif json_response.step == "OBSERVE":
            print(f"\n🤓 Observation: {json_response.content}")
            continue

        elif json_response.step == "TOOL":
            if json_response.tool not in TOOLS:

                print("😢\n Unsupported tool requested.")
                break

            tool_response = TOOLS[json_response.tool](json_response.input)
            MESSAGE_HISTORY.append(
                {
                    "role": "assistant",
                    "content": f'{{"step": "{json_response.step}", "content": "{tool_response}"}}',
                }
            )

            print(f"\n🧰 Tool: {json_response.tool}, Input: {json_response.input}")
            continue

        elif json_response.step == "OUTPUT":
            print(f"\n📺 Output: {json_response.content}")
            continue

        elif json_response.step == "RESULT":
            print(f"\n📉 Result: {json_response.content}")
            break


if __name__ == "__main__":
    main()
