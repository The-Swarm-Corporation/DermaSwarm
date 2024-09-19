import os
from swarms import Agent
from swarm_models import OpenAIChat
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of the OpenAIChat class
model = OpenAIChat(
    openai_api_key=api_key, model_name="gpt-4o-mini", temperature=0.1
)

# Define subfields of dermatology and their descriptions
dermatology_subfields = {
    "Medical Dermatology": "Focuses on the diagnosis and treatment of skin diseases like eczema, psoriasis, acne, and infections.",
    "Surgical Dermatology": "Involves surgical interventions for skin conditions such as skin cancer, cysts, or benign growths.",
    "Cosmetic Dermatology": "Concentrates on aesthetic improvements of the skin, including treatments for wrinkles, pigmentation, and scars, and procedures like Botox, fillers, and laser therapy.",
    "Pediatric Dermatology": "Specializes in treating skin conditions in infants, children, and adolescents.",
    "Dermatopathology": "Combines dermatology and pathology, focusing on diagnosing skin diseases by examining skin biopsies at a microscopic level.",
    "Immunodermatology": "Deals with skin disorders related to the immune system, such as autoimmune skin diseases.",
    "Mohs Surgery": "A specialized surgical technique for treating skin cancer, where the surgeon removes thin layers of skin and examines them under a microscope until only cancer-free tissue remains.",
    "Teledermatology": "Involves providing dermatological consultations and care remotely through telecommunication technologies.",
    "Trichology": "A subfield focusing on hair and scalp disorders, including hair loss and other hair-related issues.",
}


# Function to write the prompt to a markdown file
def write_prompt_to_file(subfield, prompt):
    filename = (
        f"{subfield.replace(' ', '_').lower()}_system_prompt.md"
    )
    with open(filename, "w") as file:
        file.write(prompt)


# Initialize the agent
agent = Agent(
    agent_name="Dermatology-Prompt-Agent",
    system_prompt="You are tasked with generating highly accurate, production-ready system prompts for dermatology subfields.",
    llm=model,
    max_loops=1,
    autosave=True,
    dashboard=False,
    verbose=True,
    dynamic_temperature_enabled=True,
    saved_state_path="dermatology_agent.json",
    user_name="swarms_corp",
    retry_attempts=1,
    context_length=200000,
    return_step_meta=False,
)


# Function to create system prompts
def create_system_prompt(subfield, description):
    prompt = f"""Create specialized, hyper accurate and production ready system prompts for {subfield}, make sure to teach it how to think: {description}. Be very specific and teach the agent how to think, provide instructions, make them extensive"""
    return agent.run(prompt)


# Loop through each subfield and create system prompts
for subfield, description in dermatology_subfields.items():
    # Generate the system prompt using the agent
    prompt = create_system_prompt(subfield, description)

    # Save the generated prompt to a markdown file
    write_prompt_to_file(subfield, prompt)

    print(
        f"Created system prompt for {subfield} and saved to markdown file."
    )

print("All system prompts have been generated and saved.")
