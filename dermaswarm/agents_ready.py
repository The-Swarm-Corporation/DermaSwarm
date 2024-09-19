import os
from swarms import Agent
from swarm_models import OpenAIChat
from dermaswarm.prompts import consensus_agent_prompt
from dotenv import load_dotenv

load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of the OpenAIChat class
model = OpenAIChat(
    openai_api_key=api_key, model_name="gpt-4o-mini", temperature=0.1
)

# Initialize the agent
conensus_agent = Agent(
    agent_name="Dermatologist-consensus-agent",
    system_prompt=consensus_agent_prompt,
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="consensus.json",
    user_name="Human",
    retry_attempts=1,
    context_length=200000,
    return_step_meta=False,
    output_type=str,
)
