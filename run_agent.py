# run_agent.py
from langchain.agents import initialize_agent, AgentType
from langchain.chat_models import ChatOpenAI
from seo_tool import seo_tool  # Import Tool objesi

llm = ChatOpenAI(temperature=0, model="gpt-4")
agent = initialize_agent(
    tools=[seo_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

result = agent.run("dijital pazarlama hakkında içerik üret")
print(result)
