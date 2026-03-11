Day 1:

Langchain:

framework to create Gen AI.

Langchain is a Python framework that helps you build apps powered by AI language models (like Chatgpt) by connecting them with tools like 
    Documents
    Search
    APIs
    Memory
    Agents

Language models + tools (Langchain will give more tools) = smart AI apps

2. Why Do We Need LangChain?

Without LangChain:
You must handle prompts, memory, and logic manually
You write long code for each step
Hard to connect LLMs to tools like databases, files, or web search

With LangChain:
Makes building LLM apps easier and faster
Gives you ready-made chains, agents, memory, retrievers
Lets you build complex flows using simple blocks

3. Why Not Just Use Other Tools Like transformers, OpenAI API, or GPT-4 directly?

Feature                    Raw OpenAI / Transformers        LangChain

Simple prompt              ✔                                ✔

Prompt templates           ✘ Manual                         ✔ Built-in

Memory / Chat history      ✘ Write manually                 ✔ Plug-and-play

Document search (RAG)      ✘ Difficult                      ✔ Easy with loaders + retrievers

Agents / Tools             ✘ Build from scratch             ✔ Pre-built agents

Chains / Flow logic        ✘ Manual scripting               ✔ Ready chains

⚡ LangChain = Fast track to LLM-powered apps


4. What Can You Build With LangChain?

Chatbots with memory

Question-answering apps using PDFs or websites

AI agents that can use tools (calculator, browser)

AutoGPT-style apps

Voice-based assistants (with plugins)


What is Langcahain:

LangChain is an open-source framework that helps developers build applications powered by Large Language Models (LLMs) like GPT, Claude, Gemini, etc.

It provides tools to connect:

> LLM models
> External data
> APIs
> Databases
> Memory
> Tools

So that you can build intelligent AI workflows.

Simple Definition

LangChain = Framework to build applications using LLMs + external data + tools.

Example Use Cases

> AI chatbots
> Document Q&A systems
> AI agents
> Code assistants
> Data analysis bots
> Warehouse automation assistants

For example, you could build a warehouse support AI assistant (similar to the prompt you created earlier).


Langcahain Ecosystem:

The LangChain Ecosystem is the collection of libraries and tools that work together to build LLM applications.

    | Project           | Purpose                                |
| ----------------- | -------------------------------------- |
| **LangChain**     | Core framework for building LLM apps   |
| **LangChain Hub** | Repository of prompts and chains       |
| **LangSmith**     | Debugging, monitoring, and evaluation  |
| **LangServe**     | Deploy LangChain apps as APIs          |
| **LangGraph**     | Build advanced AI agents and workflows |


3. LangChain Components:

    Document loaders - helps to load different type of documents.
    Document transformers - large document split into multiple.
    Embedding models - convert words into vectorto store into database
    Vector store - database
    retrievers - fetch data from Vector
    agents
    tools - intract to external systems
    memory
    chains
    output parcers - parce output
    prompt


LangChain is built from several core components.

    1. Models

        These are the LLMs or embedding models used.

        Examples:

        > OpenAI GPT
        > Claude
        > Gemini
        > Ollama
        > HuggingFace models

    Ex:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model="gpt-4")

    2. Prompts
        Prompts define how instructions are given to the LLM.

        from langchain.prompts import PromptTemplate

        prompt = PromptTemplate(
            input_variables=["topic"],
            template="Explain {topic} in simple terms"
        )

    3. Chains
        Chains connect multiple steps together.
        Example workflow:

            User Question
                ↓
            Prompt Template
                ↓
               LLM
                ↓
              Output

        Example:
            from langchain.chains import LLMChain
            chain = LLMChain(llm=llm, prompt=prompt)

    4. Memory
        Memory allows the model to remember conversation history.
        Example:

            User: Hi
            Bot: Hello!

            User: What is my name?
            Bot: Rajan

        Types:

            ConversationBufferMemory
            ConversationSummaryMemory
            VectorMemory

            Example:

            from langchain.memory import ConversationBufferMemory

    5. Tools

        Tools allow AI to interact with external systems.

        Examples:

        Web search
        Calculator
        Database queries
        APIs

        Example:

        tools = ["search", "calculator"]

    6. Agents are AI systems that decide what action to take.

        Instead of simple prompt → response.

        Agents can:

            Understand question
            Decide which tool to use
            Execute tool
            Return result

        Example:

        User: What is the weather in Atlanta?

        Agent decides:
        → Use weather API
        → Fetch result
        → Answer user

    7. Document Loaders

        Used to load external data.

        Examples:

        PDFs
        Websites
        CSV
        Databases

        Example:

        from langchain.document_loaders import PyPDFLoader

    8. Text Splitters (Document Transformers)

        Split large documents into smaller chunks.

        Large PDF
        ↓
        Split into chunks
        ↓
        Store in vector database

        Example:
            from langchain.text_splitter import RecursiveCharacterTextSplitter

    9. Vector Stores

        Store embeddings for semantic search.

        Popular vector databases:

        Pinecone
        FAISS
        Chroma
        Weaviate

        Example:

        from langchain.vectorstores import FAISS

4. Simple Architecture of LangChain App

Example RAG (Retrieval Augmented Generation) system.

        User Question
            │
            ▼
        Embedding Model
            │
            ▼
        Vector Database Search
            │
            ▼
        Relevant Documents
            │
            ▼
        LLM + Prompt
            │
            ▼
        Final Answer

5. Why LangChain is Popular

Advantages:

Easy LLM integration
Connects APIs and tools
Supports RAG architecture
Agent framework
Supports many models
Python and JS support

6. AI system stack:

Frontend: React / Streamlit
Backend: Python
Framework: LangChain
LLM: OpenAI / Claude
Vector DB: Pinecone / FAISS
Deployment: Docker + Azure


Data Ingestion: (Data load)

    Loading external info into memory so that the AI can understand and answer question based on it.

    Data connection:

        source --> Load (data Ingestion) --> Transform --> Embed --> Store --> Retrieve

        backend flow:

            data Ingestion ----> text Splitter ---> embedding ----> vector store ---> retriever


Text Splitting:
    
    What is Text Splitting?

    Text splitting means breaking a large document into smaller chunks, so the AI model can read it piece by piece.

    📌 Why do we split text?
    LLMs (like GPT) can only handle a limited number of words at a time (called tokens).

    Splitting helps us:

    Avoid errors like "context too long"

    Feed meaningful chunks to the model

    Use retrieval-based Q&A

    ✂️ How Text Splitting Works (Simple Analogy)

    💡 Imagine a big book. You can't memorize the whole book in one go, right?
    So you read 1 page at a time → that's like a chunk!

    Chuck_size  --> Max chatacter per Chuck
    chuck_overlap  --> character repeated between Chucks

Embedding:

    Embeddings

    Embeddings are numbers that represent the meaning of words or sentences so AI can compare them.

    In simple terms:

    Just like GPS uses coordinates to find places, embeddings use vectors to find similar meanings.

    Real-Life Analogy:

    Think of each sentence as a point on a map.
    Sentences with similar meanings will be closer together on this map, even if the words are different.

    Why Use Embeddings?

    For semantic search (find answers based on meaning, not exact words)

    To connect chunks of documents with user questions

    Used in RAG (Retrieval-Augmented Generation)

    To build Q&A over PDFs, chat with documents, etc.

    Terms:

        Embedding --> Turning text into numbers(vectors) thst hold meaning
        Embedding Model --> Tool that character those vectors (ex: openAI, HuggingFace)

Vector Store:

    A vector store is like a smart library that stores the meaning of text as numbers (embeddings), so we can search by meaning later.

    It's where we save all those embeddings we created earlier.

    Real-Life Analogy:
        Imagine putting cards in boxes where similar meanings are close together.
        When you ask a question, the AI searches for the closest meaning, not the exact words.

    Why Do We Need a Vector Store?

    Without Vector Store

        Can't search chunks by meaning
        No efficient way to retrieve
        Hard to match questions to text

    With Vector Store
        Search by similarity
        Fast lookup using vectors
        LLM finds best-matching answers

    Vector Store Options in LangChain
        Vector Store	            Description	                        Offline / Online
        FAISS	                    Fast, lightweight, local	        ✅ Offline
        Chroma	                    Simple and popular for beginners	✅ Offline
        Pinecone	                Cloud-based, scalable	            ❌ Online

        Weaviate, Qdrant, Milvus – More advanced options

What is a Retriever?

    A retriever is a tool that fetches the most relevant document chunks from a vector store based on your question.

    Think of it like:
    Vector Store = Memory
    Retriever = Brain's search tool
    LLM = Person giving answers

    So when a question is asked, the retriever finds the best matching pieces of info, then passes them to the LLM to answer.


    PDF/Text -> Chuck --> Embed --> Store in Vector DB --> Ask Question --> 
        Retriever gets relevant chunks
        LLM answers using those chunks
