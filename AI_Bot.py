import os
import logging
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import ToolNode
from langchain_community.tools import DuckDuckGoSearchRun
from pypdf import PdfReader
from langchain_core.messages import HumanMessage
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
import json
import time
load_dotenv()


LOG_FILE = "logs.json"

def save_log(query,  latency, tools):
    log = {
        "query": query,
        "latency": round(latency, 2),
        "tools": tools,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]


def route_tools(state: AgentState):
    last_msg = state["messages"][-1]

    if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
        return "tools"

    return END

tool_usage = {}

def increment(name):
    tool_usage[name] = tool_usage.get(name, 0) + 1

@tool
def read_pdf(path: str) -> str:
    """Read ONLY a local PDF file from the computer.

    Use ONLY when the user provides a PDF filename like ML.pdf.
    Never use this tool for internet or general knowledge questions."""

    try:
        reader = PdfReader(path)

        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""

        increment("read pdf tool")

        return text[:10000]

    except Exception as e:
        return f"Error reading PDF: {str(e)}"


@tool
def read_file(path: str) -> str:
    """
    Read ONLY a local text file (.txt) from the computer.

    Use this tool ONLY if the user explicitly provides a filename
    like notes.txt or asks to read a local file.

    Never use this tool for answering general knowledge questions.

    """
    increment("Read file tool")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression.
    """

    

    try:
        result = eval(expression)
        increment("calculator tool")
        return str(result)

    except Exception as e:
        return str(e)
    
ddg = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """
    Search the internet using DuckDuckGo.

    Use this tool whenever the user asks about:
    - current information
    - latest news
    - population
    - CEO
    - weather
    - sports
    - facts not contained in local files
    """
    increment("Search Tool")

    return ddg.run(query)


llm = ChatGroq(
    api_key=os.getenv("GROK_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0
)


tool_node = ToolNode([
    read_pdf,
    read_file,
    calculator,
    search_tool
])


llm_with_tools = llm.bind_tools(
    [
        read_pdf,
        read_file,
        calculator,
        search_tool
    ],
    tool_choice="auto"
)
def chatbot(state: AgentState):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}

graph = StateGraph(AgentState)

graph.add_node("chatbot", chatbot)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chatbot")

graph.add_conditional_edges(
    "chatbot",
    route_tools
)

graph.add_edge("tools", "chatbot")

app = graph.compile()


while True:
    tool_usage.clear() 
    query = input("Ask: ")

    if query.lower() == "exit":
        break
    start = time.time()

    result = app.invoke({
        "messages": [HumanMessage(content=query)]
    })
    end = time.time()

    latency = end - start

    # report = result["report"]
    

    save_log(
    query=query,
    latency=latency,
    tools=tool_usage
)

    print(result["messages"][-1].content)


