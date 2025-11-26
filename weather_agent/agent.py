from openai import OpenAI
from dotenv import load_dotenv
import random
import json

load_dotenv()

client = OpenAI()

def get_weather(city):
    return f"Todays weather of {city} is {random.randint(10, 99)} C"

tool_mapping  = {
    "get_weather" : get_weather
}

system_prompt = """
    You are an AI agent. You have to only answer the questions related to weathers. If question out of the scope then reply with apologies text like I am an AI agent help u related to weathers. I cannot help u with this question. Sorry...!

    While answering the questions you have to go with some steps like START - PLAN - TOOL - OBSERVE - OUTPUT
     - START : In this step you have to receive user query.
     - PLAN : After receiving the query you have to plan to resolve it. You have to Plan it to resolve the query multiple times.
     - TOOL : Based on your planning, identify the provided tools to get releted answer.
     - OBSERVE : In this step based on output received in TOOL step, undertand the output and summarise it.
     - OUTPUT : In this step, whatever you summarised from observed step, you need to give polite answer as final output.

     In every step you have to give result in below json format only
     { "step" : "START | PLAN | TOOL | OBSERVE | OUTPUT", "content": "Summarised sentense", "tool": "available tools", "input":  "required paramter to run available tool"}

    Available Tools
     - get_weather : This tool takes city name as paramter and returns the current weather of that city
    
    Example 1 :
        START : What is the weather in mumbai?
        PLAN : { "step" : "PLAN", "content" : "Seems like user is interested in getting weather of mumbai" }
        PLAN : { "step" : "PLAN", "content" : "Let see if we have available tools to resolve this" }
        PLAN : { "step" : "PLAN", "content" : "Great, we have get_weather tool available for the query" }
        PLAN : { "step" : "PLAN", "content" : "I need to call get_weather tool for mumbai as parameter" }
        TOOL : { "step" : "TOOL", "tool" : "get_weather", "input" : "mumbai" }
        OBSERVE : { "step" : "OBSERVE", "tool" : "get_weather", "content" : "Todays weather of mumbai is 15 C" }
        PLAN : { "step" : "PLAN", "content" : "Ok great. Now i get the current weather of mumbai is 15 C" }
        PLAN : { "step" : "PLAN", "content" : "Now i need to summarise the result and convert it into polite manner" }
        OUTPUT : { "step" : "OUTPUT", "content" : "Hey, Mumbai city is very cold now a days. It feels like seeing snowfall everywhere." }

    Example 2 :
        START : What is your favorite movie?
        PLAN : { "step" : "PLAN", "content" : "Seems kike user asking out of the scope question which is not relarted to weather" }
        PLAN : { "step" : "PLAN", "content" : "As rules suggest I cannot resolving out of scope questions" }
        OUTPUT : { "step" : "OUTPUT", "content" : "Hey, I am AI agent help only in giving weather related queries. Sorry for the inconvienice" }
     
     

"""

def main():
    message_history = [{"role" : "system", "content": system_prompt}]
    user_query = input("< ")

    message_history.append({"role": "user", "content" : user_query})

    while True:
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        parsed_output = json.loads(raw_result)

        message_history.append({"role" : "assistant", "content" :raw_result })

        if parsed_output.get("step") == "START":
            print(f"▶️ {parsed_output}")
            continue

        if parsed_output.get("step") == "PLAN" :
            print(f"🧠 {parsed_output}")
            continue

        if parsed_output.get("step") == "OBSERVE" :
            print(f"👁️ {parsed_output}")
            continue

        if parsed_output.get("step") == "TOOL" :
            print(f"⛏️ {parsed_output}")
            weather = tool_mapping[parsed_output.get("tool")](parsed_output.get("input"))
            message_history.append({"role" : "assistant", "content" : weather})
            continue

        if parsed_output.get("step") == "OUTPUT" :
            print(f"✅ {parsed_output}")
            break

main()