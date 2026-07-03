***# 🤖 AI Research Assistant***



***An AI-powered Research Assistant built using \*\*LangGraph\*\*, \*\*LangChain\*\*, and \*\*Groq LLM\*\* that intelligently answers user queries by selecting the appropriate tool.***



***The assistant can:***

***- 📄 Read and summarize PDF files***

***- 📁 Read local text files***

***- 🌐 Search the web for real-time information***

***- 🧮 Perform mathematical calculations***

***- 📊 Track query latency and tool usage using a Streamlit dashboard***



***---***



***# Features***



***- LangGraph Agent Workflow***

***- Automatic Tool Selection***

***- PDF Reader***

***- Local File Reader***

***- DuckDuckGo Web Search***

***- Calculator Tool***

***- Query Logging***

***- Latency Tracking***

***- Tool Usage Analytics***

***- Streamlit Dashboard***



***---***



***# Tech Stack***



***- Python***

***- LangGraph***

***- LangChain***

***- Groq API***

***- Streamlit***

***- DuckDuckGo Search***

***- PyPDF***

***- Pandas***



***---***



***# Project Structure***



***```***

***.***

***│── Agent\_chatbot.py      # Main AI Agent***

***│── dashboard.py          # Streamlit Dashboard***

***│── logs.json             # Stores query logs***

***│── requirements.txt***

***│── .env***

***│── README.md***

***```***



***---***



***# Installation***



***Clone the repository***



***```bash***

***git clone https://github.com/yourusername/AI-Research-Assistant.git***



***cd AI-Research-Assistant***

***```***



***Create Virtual Environment***



***```bash***

***python -m venv venv***

***```***



***Activate it***



***Windows***



***```bash***

***venv\\Scripts\\activate***

***```***



***Linux/Mac***



***```bash***

***source venv/bin/activate***

***```***



***Install dependencies***



***```bash***

***pip install -r requirements.txt***

***```***



***---***



***# Environment Variables***



***Create a file named***



***```***

***.env***

***```***



***Add your Groq API key***



***```env***

***GROK\_API\_KEY=your\_groq\_api\_key\_here***

***```***



***> Get your API key from:***

***> https://console.groq.com/keys***



***---***



***# Running the AI Assistant***



***```bash***

***python Agent\_chatbot.py***

***```***



***Example***



***```***

***Ask: calculate 25\*80***



***Ask: summarize ML.pdf***



***Ask: who is the CEO of Apple?***



***Ask: read notes.txt***

***```***



***Type***



***```***

***exit***

***```***



***to stop the chatbot.***



***---***



***# Running the Dashboard***



***```bash***

***streamlit run dashboard.py***

***```***



***The dashboard displays:***



***- Total Queries***

***- Average Latency***

***- Query History***

***- Tool Usage***

***- Latency Graph***



***---***



***# Available Tools***



***### PDF Reader***



***Reads and summarizes local PDF files.***



***Example***



***```***

***summarize ML.pdf***

***```***



***---***



***### File Reader***



***Reads local text files.***



***Example***



***```***

***read notes.txt***

***```***



***---***



***### Calculator***



***Evaluates mathematical expressions.***



***Example***



***```***

***calculate (45\*98)+100***

***```***



***---***



***### Web Search***



***Searches the internet using DuckDuckGo.***



***Example***



***```***

***latest AI news***



***who is the CEO of Apple***



***USD to INR exchange rate***

***```***



***---***



***# Logging***



***Every query is automatically logged with:***



***- User Query***

***- Response Time***

***- Tool Used***

***- Timestamp***



***Logs are stored in***



***```***

***logs.json***

***```***



***---***



***# Sample Workflow***



***```***

&#x20;         ***User Query***

&#x20;              ***│***

&#x20;              ***▼***

&#x20;         ***LangGraph Agent***

&#x20;              ***│***

&#x20;     ***┌────────┼─────────┐***

&#x20;     ***▼        ▼         ▼***

&#x20;***Calculator  PDF Tool  Search Tool***

&#x20;     ***│        │         │***

&#x20;     ***└────────┼─────────┘***

&#x20;              ***▼***

&#x20;       ***Final AI Response***

&#x20;              ***│***

&#x20;              ***▼***

&#x20;        ***Save Query Logs***

***```***



***---***



***# Future Improvements***



***- Chat History***

***- Memory Support***

***- Multi-PDF Retrieval***

***- RAG Integration***

***- Voice Assistant***

***- Database Logging***

***- Authentication***

***- Docker Support***



***---***



***# Author***



***Jenil Mangukiya***



***---***



***# License***



***This project is licensed under the MIT License.***

