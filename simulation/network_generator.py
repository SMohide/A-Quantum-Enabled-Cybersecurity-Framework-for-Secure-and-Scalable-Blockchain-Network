import uuid
import random
import logging
import statistics
import json
import csv

from datetime import datetime
from typing import List, Dict, Any


class NetworkGenerator:
    """
    Blockchain Network Generator

    Generates permissioned blockchain networks
    of varying sizes for scalability and
    security evaluation experiments.

    Supported Network Sizes:
    - 20 Nodes
    - 50 Nodes
    - 100 Nodes
    - 150 Nodes
    - 200 Nodes
    """

    def __init__(
        self,
        min_nodes: int = 20,
        max_nodes: int = 200,
        network_type: str = "permissioned",
        random_seed: int = 42
    ):

        self.min_nodes = min_nodes
        self.max_nodes = max_nodes
        self.network_type = network_type

        random.seed(random_seed)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

        self.logger = logging.getLogger(
            self.__class__.__name__
        )

        self.logger.info(
            "Network Generator Initialized"
        )

    # ====================================================
    # Generate Individual Node
    # ====================================================

    def generate_node(
        self,
        node_id: int
    ) -> Dict[str, Any]:

        node = {

            "node_id":
                f"N{node_id}",

            "uuid":
                str(uuid.uuid4()),

            "status":
                "active",

            "reputation":
                round(
                    random.uniform(
                        0.70,
                        1.00
                    ),
                    3
                ),

            "stake":
                random.randint(
                    100,
                    5000
                ),

            "cpu_cores":
                random.randint(
                    2,
                    32
                ),

            "memory_gb":
                random.choice(
                    [4, 8, 16, 32, 64]
                ),

            "bandwidth_mbps":
                random.randint(
                    50,
                    1000
                ),

            "latency_ms":
                round(
                    random.uniform(
                        1.0,
                        20.0
                    ),
                    2
                ),

            "validator":
                False,

            "created_at":
                datetime.now().isoformat()
        }

        return node

    # ====================================================
    # Generate Blockchain Network
    # ====================================================

    def generate_network(
        self,
        num_nodes: int
    ) -> List[Dict]:

        if num_nodes < self.min_nodes:

            raise ValueError(
                f"Minimum nodes required: "
                f"{self.min_nodes}"
            )

        if num_nodes > self.max_nodes:

            raise ValueError(
                f"Maximum nodes allowed: "
                f"{self.max_nodes}"
            )

        self.logger.info(
            f"Generating network with "
            f"{num_nodes} nodes"
        )

        network = []

        for node_id in range(
            1,
            num_nodes + 1
        ):

            network.append(
                self.generate_node(
                    node_id
                )
            )

        self.logger.info(
            "Network generation completed"
        )

        return network

    # ====================================================
    # Assign Validators
    # ====================================================

    def assign_validators(
        self,
        network: List[Dict],
        validator_count: int
    ) -> List[Dict]:

        if validator_count > len(network):

            raise ValueError(
                "Validator count exceeds "
                "network size"
            )

        validators = random.sample(
            network,
            validator_count
        )

        for validator in validators:

            validator["validator"] = True

        self.logger.info(
            f"{validator_count} validators assigned"
        )

        return network

    # ====================================================
    # Network Statistics
    # ====================================================

    def calculate_statistics(
        self,
        network: List[Dict]
    ) -> Dict:

        stakes = [

            node["stake"]

            for node in network
        ]

        reputations = [

            node["reputation"]

            for node in network
        ]

        bandwidths = [

            node["bandwidth_mbps"]

            for node in network
        ]

        latencies = [

            node["latency_ms"]

            for node in network
        ]

        statistics_report = {

            "total_nodes":
                len(network),

            "average_stake":
                round(
                    statistics.mean(stakes),
                    2
                ),

            "average_reputation":
                round(
                    statistics.mean(
                        reputations
                    ),
                    3
                ),

            "average_bandwidth":
                round(
                    statistics.mean(
                        bandwidths
                    ),
                    2
                ),

            "average_latency":
                round(
                    statistics.mean(
                        latencies
                    ),
                    2
                ),

            "validator_count":

                sum(
                    node["validator"]

                    for node in network
                )
        }

        return statistics_report

    # ====================================================
    # Export Network as JSON
    # ====================================================

    def export_json(
        self,
        network: List[Dict],
        filename: str
    ) -> None:

        with open(
            filename,
            "w"
        ) as file:

            json.dump(
                network,
                file,
                indent=4
            )

        self.logger.info(
            f"Network exported to "
            f"{filename}"
        )

    # ====================================================
    # Export Network as CSV
    # ====================================================

    def export_csv(
        self,
        network: List[Dict],
        filename: str
    ) -> None:

        if not network:

            return

        with open(
            filename,
            "w",
            newline=""
        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=
                network[0].keys()
            )

            writer.writeheader()

            writer.writerows(
                network
            )

        self.logger.info(
            f"Network exported to "
            f"{filename}"
        )

    # ====================================================
    # Generate Experimental Scenario
    # ====================================================

    def generate_experiment_network(
        self,
        network_size: int,
        validator_count: int
    ) -> Dict:

        network = self.generate_network(
            network_size
        )

        network = self.assign_validators(
            network,
            validator_count
        )

        stats = self.calculate_statistics(
            network
        )

        return {

            "network":
                network,

            "statistics":
                stats
        }


# ========================================================
# Main Execution
# ========================================================

if __name__ == "__main__":

    generator = NetworkGenerator()

    experiment = (

        generator
        .generate_experiment_network(

            network_size=100,

            validator_count=15
        )
    )

    print(
        "\nNetwork Statistics\n"
    )

    for key, value in (

        experiment[
            "statistics"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )

    generator.export_json(

        experiment["network"],

        "network.json"
    )

    generator.export_csv(

        experiment["network"],

        "network.csv"
    )

