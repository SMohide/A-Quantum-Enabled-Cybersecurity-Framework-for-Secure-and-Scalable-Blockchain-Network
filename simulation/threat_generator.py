// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // Write C code here```python
"""
threat_generator.py

Quantum-Enabled Cybersecurity Framework (QECF)

This module implements the Quantum Threat Assessment Model
described in the QECF framework.

The module generates, classifies, scores, and evaluates
quantum-enabled cyber threats against blockchain networks.

Author: Shravani Mohide

Research Paper:
A Quantum-Enabled Cybersecurity Framework for Secure and
Scalable Blockchain Networks
"""

import random
import logging
import statistics
import json
import csv

from datetime import datetime
from typing import Dict, List, Any


class ThreatGenerator:
    """
    Quantum Threat Generator

    Generates realistic quantum attack scenarios
    for blockchain security experiments.

    Threat Levels

    Level 0:
        No Threat

    Level 1:
        Emerging Quantum Capability

    Level 2:
        Active Quantum Attack

    Level 3:
        Critical Quantum Breach
    """

    THREAT_LEVELS = {

        0: "No Threat",

        1: "Emerging Quantum Capability",

        2: "Quantum Attack",

        3: "Critical Quantum Breach"
    }

    ATTACK_TYPES = [

        "Shor Attack",

        "Grover Attack",

        "Key Recovery Attack",

        "Signature Forgery",

        "Consensus Manipulation",

        "Validator Compromise",

        "Quantum Eavesdropping",

        "Network Disruption",

        "Sybil Attack",

        "Replay Attack"
    ]

    def __init__(

        self,

        random_seed: int = 42

    ):

        random.seed(random_seed)

        logging.basicConfig(

            level=logging.INFO,

            format="%(asctime)s - %(levelname)s - %(message)s"
        )

        self.logger = logging.getLogger(

            self.__class__.__name__
        )

        self.logger.info(

            "Threat Generator Initialized"
        )

    # ===================================================
    # Generate Single Threat
    # ===================================================

    def generate_threat(

        self,

        threat_id: int,

        level: int

    ) -> Dict[str, Any]:

        if level not in self.THREAT_LEVELS:

            raise ValueError(

                "Invalid Threat Level"
            )

        severity_score = round(

            random.uniform(

                level * 0.25,

                min(
                    1.0,
                    level * 0.35 + 0.25
                )
            ),

            3
        )

        threat = {

            "threat_id":

                f"T{threat_id}",

            "attack_type":

                random.choice(
                    self.ATTACK_TYPES
                ),

            "threat_level":

                level,

            "description":

                self.THREAT_LEVELS[level],

            "severity_score":

                severity_score,

            "affected_nodes":

                random.randint(
                    1,
                    50
                ),

            "probability":

                round(
                    random.uniform(
                        0.20,
                        0.95
                    ),
                    3
                ),

            "detected":

                random.choice(
                    [True, False]
                ),

            "timestamp":

                datetime.now()
                .isoformat()
        }

        return threat

    # ===================================================
    # Generate Threat Scenario
    # ===================================================

    def generate_scenario(

        self,

        num_threats: int

    ) -> List[Dict]:

        threats = []

        self.logger.info(

            f"Generating "
            f"{num_threats} threats"
        )

        for threat_id in range(

            1,

            num_threats + 1
        ):

            level = random.choice(

                [0, 1, 2, 3]
            )

            threat = self.generate_threat(

                threat_id,

                level
            )

            threats.append(
                threat
            )

        return threats

    # ===================================================
    # Calculate Threat Score
    # ===================================================

    def calculate_threat_score(

        self,

        threats: List[Dict]

    ) -> float:

        scores = [

            threat["severity_score"]

            for threat in threats
        ]

        return round(

            statistics.mean(
                scores
            ),

            3
        )

    # ===================================================
    # Classify Risk
    # ===================================================

    def classify_risk(

        self,

        threat_score: float

    ) -> str:

        if threat_score < 0.30:

            return "LOW"

        elif threat_score < 0.60:

            return "MEDIUM"

        elif threat_score < 0.85:

            return "HIGH"

        return "CRITICAL"

    # ===================================================
    # Threat Statistics
    # ===================================================

    def generate_statistics(

        self,

        threats: List[Dict]

    ) -> Dict:

        threat_score = (

            self.calculate_threat_score(
                threats
            )
        )

        risk_level = (

            self.classify_risk(
                threat_score
            )
        )

        statistics_report = {

            "total_threats":

                len(threats),

            "average_threat_score":

                threat_score,

            "risk_level":

                risk_level,

            "detected_attacks":

                sum(

                    threat["detected"]

                    for threat in threats
                ),

            "critical_attacks":

                sum(

                    threat[
                        "threat_level"
                    ] == 3

                    for threat in threats
                )
        }

        return statistics_report

    # ===================================================
    # Quantum Threat Assessment Algorithm
    # ===================================================

    def quantum_threat_assessment(

        self,

        threats: List[Dict]

    ) -> Dict:

        threat_score = (

            self.calculate_threat_score(
                threats
            )
        )

        risk_level = (

            self.classify_risk(
                threat_score
            )
        )

        return {

            "threat_score":

                threat_score,

            "risk_level":

                risk_level,

            "recommendation":

                self.generate_recommendation(
                    risk_level
                )
        }

    # ===================================================
    # Security Recommendation
    # ===================================================

    def generate_recommendation(

        self,

        risk_level: str

    ) -> str:

        recommendations = {

            "LOW":

                "Continue monitoring.",

            "MEDIUM":

                "Increase validator verification.",

            "HIGH":

                "Activate PQC and QKD protocols.",

            "CRITICAL":

                "Initiate emergency security reconfiguration."
        }

        return recommendations[
            risk_level
        ]

    # ===================================================
    # Export JSON
    # ===================================================

    def export_json(

        self,

        threats: List[Dict],

        filename: str

    ) -> None:

        with open(

            filename,

            "w"
        ) as file:

            json.dump(

                threats,

                file,

                indent=4
            )

        self.logger.info(

            f"Exported to "
            f"{filename}"
        )

    # ===================================================
    # Export CSV
    # ===================================================

    def export_csv(

        self,

        threats: List[Dict],

        filename: str

    ) -> None:

        if not threats:

            return

        with open(

            filename,

            "w",

            newline=""
        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=
                threats[0].keys()
            )

            writer.writeheader()

            writer.writerows(
                threats
            )

        self.logger.info(

            f"Exported to "
            f"{filename}"
        )


# =======================================================
# Main Execution
# =======================================================

if __name__ == "__main__":

    generator = ThreatGenerator()

    threats = (

        generator.generate_scenario(
            50
        )
    )

    stats = (

        generator.generate_statistics(
            threats
        )
    )

    assessment = (

        generator.quantum_threat_assessment(
            threats
        )
    )

    print("\nThreat Statistics\n")

    for key, value in stats.items():

        print(
            f"{key}: {value}"
        )

    print("\nAssessment\n")

    for key, value in assessment.items():

        print(
            f"{key}: {value}"
        )

    generator.export_json(

        threats,

        "threats.json"
    )

    generator.export_csv(

        threats,

        "threats.csv"
    )
```

    printf("Start small. Ship something.");

    return 0;
}
