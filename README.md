# DermaSwarm: A Production-Grade Multi-Agent Dermatology Swarm

[![Join our Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/agora-999382051935506503) [![Subscribe on YouTube](https://img.shields.io/badge/YouTube-Subscribe-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@kyegomez3242) [![Connect on LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kye-g-38759a207/) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/kyegomezb)


[![PyPI version](https://badge.fury.io/py/dermaswarm.svg)](https://badge.fury.io/py/dermaswarm)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/The-Swarm-Corporation/DermaSwarm/blob/main/LICENSE)


**DermaSwarm** is a production-grade multi-agent system designed for dermatologists to collaboratively diagnose and treat skin conditions. Leveraging the power of AI-driven agents, DermaSwarm cross-checks peer-reviewed dermatology research to ensure diagnosis accuracy, generates treatment plans, and outputs results in easy-to-use JSON format. With extensive logging, seamless collaboration between agents, and a focus on clinical reliability, DermaSwarm is built for real-world use by dermatology practitioners.

## Installation

You can install **DermaSwarm** via pip:

```bash
pip install -U dermaswarm
```

## Features

- **Multi-Agent Collaboration**: Leverage multiple AI agents specialized in dermatology to analyze symptoms, suggest diagnoses, and validate findings against peer-reviewed literature.
- **Evidence-Based Diagnoses**: Each diagnosis is cross-referenced with peer-reviewed articles to ensure accuracy and up-to-date knowledge.
- **Personalized Treatment Plans**: Based on the diagnosis, DermaSwarm generates a personalized treatment plan for the patient.
- **JSON Output**: Structured outputs in JSON format, including diagnosis, references, and suggested treatments for easy integration into medical records.
- **Comprehensive Logging**: Track the entire diagnostic process with extensive logging to ensure transparency and traceability of agent actions.
- **API-Ready**: Easy to integrate with existing dermatology workflows and applications.


## Architecture

```mermaid
graph TD
    A[Images and Text Describing Condition] --> B[Diagnosis Agent]
    B --> C[Outputs Potential Diagnoses]
    
    C --> R1[Round Robin Swarm of Specialists]
    
    R1 --> M1[Medical Dermatology Agent]
    R1 --> S1[Surgical Dermatology Agent]
    R1 --> C1[Cosmetic Dermatology Agent]
    R1 --> P1[Pediatric Dermatology Agent]
    R1 --> D1[Dermatopathology Agent]
    R1 --> I1[Immunodermatology Agent]
    R1 --> M2[Mohs Surgery Agent]
    R1 --> T1[Trichology Agent]
    R1 --> TD1[Teledermatology Agent]

    M1 -->|Validates and Provides Thoughts| R2
    S1 -->|Validates and Provides Thoughts| R2
    C1 -->|Validates and Provides Thoughts| R2
    P1 -->|Validates and Provides Thoughts| R2
    D1 -->|Validates and Provides Thoughts| R2
    I1 -->|Validates and Provides Thoughts| R2
    M2 -->|Validates and Provides Thoughts| R2
    T1 -->|Validates and Provides Thoughts| R2
    TD1 -->|Validates and Provides Thoughts| R2
    
    R2[Consensus Agent: Most Likely Diagnosis] --> MI[Medical Insight Agent]
    MI -->|Queries PubMed for Articles| D3[Final Diagnosis]

    D3 --> H{Validated by Human?}
    H -->|Yes| I[Human Validates Diagnosis]
    H -->|No| J[Auto Confirmed by Swarm]

    D3 --> K[Treatment Plan Agent]
    K --> L[Proposes Series of Treatments]
    L --> M[Ranks Treatments: Best Fit, Cheapest, Most Effective, Least Painful]
    M --> N[Final Treatment Plan]


```

## Usage

Below is an example of how to use **DermaSwarm** in a typical dermatological workflow.

### Example


### Logging

**DermaSwarm** includes comprehensive logging powered by `loguru` to track agent decisions, references to peer-reviewed articles, and diagnostic conclusions. You can configure the logging settings to fit your clinic’s compliance and documentation needs.

```python
from dermaswarm import configure_logging

# Configure logging
configure_logging(level="INFO", log_file="diagnosis_logs.log")
```

## API Integration

DermaSwarm can be easily integrated into any clinical software via its REST API interface. Below is an example request using cURL:

```bash
curl -X POST https://api.dermaswarm.com/diagnose \
-H "Content-Type: application/json" \
-d '{
  "symptoms": {
    "rash": "red, scaly patches",
    "location": "forearm",
    "duration": "2 weeks",
    "itchiness": "severe"
  },
  "medical_history": {
    "allergies": ["pollen"],
    "current_medications": ["ibuprofen"]
  }
}'
```

### API Response

```json
{
  "diagnosis": "Psoriasis",
  "treatment_plan": {
    "medications": [
      {
        "name": "Topical Corticosteroids",
        "dosage": "Apply twice daily for 2 weeks"
      }
    ],
    "follow_up": "Reassess in 4 weeks for symptom improvement"
  },
  "peer_reviewed_articles": [
    {
      "title": "Psoriasis and Its Treatment",
      "journal": "Journal of Dermatology",
      "url": "https://example.com/psoriasis-article"
    }
  ]
}
```

## Configuration

DermaSwarm offers flexible configuration options to tailor the system to your practice:

```python
from dermaswarm import set_config

set_config({
    "peer_review_check": True, 
    "output_format": "json", 
    "log_level": "INFO"
})
```

## Roadmap

- **Enhanced Treatment Plans**: Addition of more diverse treatment recommendations, including alternative therapies.
- **Multi-Language Support**: Expanding the language capabilities to support non-English-speaking regions.
- **Cloud Integration**: Upcoming support for cloud-based deployments with added security and scalability.
- **Mobile App Integration**: Seamless mobile interface for real-time diagnostics on-the-go.

## Contributing

We welcome contributions from the community! Please see our [CONTRIBUTING.md](https://github.com/The-Swarm-Corporation/DermaSwarm/blob/main/CONTRIBUTING.md) for more details.

## License

DermaSwarm is open-source software, licensed under the [MIT License](https://github.com/The-Swarm-Corporation/DermaSwarm/blob/main/LICENSE).
