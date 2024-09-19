import os

from dotenv import load_dotenv
from swarm_models import GPT4VisionAPI
from swarms import Agent, RoundRobinSwarm

load_dotenv()

# Get the OpenAI API key from the environment variable
api_key = os.getenv("OPENAI_API_KEY")

# # Create an instance of the OpenAIChat class
# model = OpenAIChat(
#     openai_api_key=api_key, model_name="gpt-4o-mini", temperature=0.1
# )

model = GPT4VisionAPI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    max_tokens=3000,
    logging_enabled=True,
)


dermatology_subfields = [
    {
        "subfield": "Medical Dermatology",
        "description": "Focuses on the diagnosis and treatment of skin diseases like eczema, psoriasis, acne, and infections.",
    },
    {
        "subfield": "Surgical Dermatology",
        "description": "Involves surgical interventions for skin conditions such as skin cancer, cysts, or benign growths.",
    },
    {
        "subfield": "Cosmetic Dermatology",
        "description": "Concentrates on aesthetic improvements of the skin, including treatments for wrinkles, pigmentation, and scars, and procedures like Botox, fillers, and laser therapy.",
    },
    {
        "subfield": "Pediatric Dermatology",
        "description": "Specializes in treating skin conditions in infants, children, and adolescents.",
    },
    {
        "subfield": "Dermatopathology",
        "description": "Combines dermatology and pathology, focusing on diagnosing skin diseases by examining skin biopsies at a microscopic level.",
    },
    {
        "subfield": "Immunodermatology",
        "description": "Deals with skin disorders related to the immune system, such as autoimmune skin diseases.",
    },
    {
        "subfield": "Mohs Surgery",
        "description": "A specialized surgical technique for treating skin cancer, where the surgeon removes thin layers of skin and examines them under a microscope until only cancer-free tissue remains.",
    },
    {
        "subfield": "Teledermatology",
        "description": "Involves providing dermatological consultations and care remotely through telecommunication technologies.",
    },
    {
        "subfield": "Trichology",
        "description": "A subfield focusing on hair and scalp disorders, including hair loss and other hair-related issues.",
    },
]

agents = []
for field in dermatology_subfields:
    print(f"{field['subfield']} – {field['description']}")
    name = field["subfield"]
    description = field["description"]

    agent = Agent(
        agent_name=f"{name}_agent",
        description=description,
        llm=model,
        max_loops=1,
        # autosave=True,
        dashboard=False,
        verbose=True,
        dynamic_temperature_enabled=True,
        saved_state_path=f"{name}.json",
        user_name="swarms_corp",
        retry_attempts=1,
        context_length=200000,
        return_step_meta=False,
        # output_type="json",
        output_type=str,
    )

    agents.append(agent)


# Round robin
diagnosis_swarm = RoundRobinSwarm(
    agents=agents,
    max_loops=1,
)
