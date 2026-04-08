# 📄 Шпаргалка: LangChain быстро

## Простая цепочка
```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ("system", "Ты помощник"),
    ("user", "{question}"),
])
chain = prompt | llm
result = chain.invoke({"question": "Что такое LLM?"})
```

## Инструмент
```python
from langchain_core.tools import tool

@tool
def check_document(text: str) -> str:
    """Проверить документ на полноту"""
    if len(text) < 100:
        return "Документ слишком короткий"
    return "Документ прошёл проверку"
```

## Создание агента
```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model=llm,
    tools=[check_document],
    prompt="Ты — инспектор документов",
)
result = agent.invoke({"messages": [{"role": "user", "content": "Проверь документ: ..."}]})
```
