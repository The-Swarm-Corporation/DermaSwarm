from swarms import BaseSwarm, Agent
from typing import List, Any
from dermaswarm.diagnosis_swarm import diagnosis_swarm
from dermaswarm.agents_ready import conensus_agent
from pydantic import BaseModel
from medinsight.agent import MedInsightPro

class DermaSwarmOutput(BaseModel):
    diagnosis: str
    consensus: str
    medical_insight: Any


class DermaSwarm(BaseSwarm):
    def __init__(
        self,
        agents: List[Agent],
        documents: List[str],
        # registry
    ):
        super().__init__()
        self.agents = agents
        self.diagnosis_swarm = diagnosis_swarm
        self.medical_insight_agent = MedInsightPro()

    def run(self, task: str, img: str, *args, **kwargs):
        diagnosis = self.diagnosis_swarm.run(
            task, img, *args, **kwargs
        )

        # Aggregator agent
        consensus_agent_response = conensus_agent.run(
            f"Conduct a consenus on these diagnoses: {diagnosis}"
        )

        # Medical insight
        # queries = /

        return consensus_agent_response
