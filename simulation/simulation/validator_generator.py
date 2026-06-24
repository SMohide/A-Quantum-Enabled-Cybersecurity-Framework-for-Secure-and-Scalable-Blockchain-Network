import random
import uuid
import logging
import statistics
import json
import csv

from datetime import datetime
from typing import List, Dict, Any


class ValidatorGenerator:
    """
    Validator Generator

    Creates validators with realistic
    blockchain attributes.

    Used in:

    - Consensus experiments
    - QRNG leader election
    - Validator fairness analysis
    - Scalability experiments
    """

    def __init__(

        self,

        min_stake: int = 100,

        max_stake: int = 10000,

        random_seed: int = 42

    ):

        self.min_stake = min_stake
        self.max_stake = max_stake

        random.seed(random_seed)

        logging.basicConfig(

            level=logging.INFO,

            format="%(asctime)s - %(levelname)s - %(message)s"
        )

        self.logger = logging.getLogger(

            self.__class__.__name__
        )

        self.logger.info(

            "Validator Generator Initialized"
        )

    # ===================================================
    # Generate Single Validator
    # ===================================================

    def generate_validator(

        self,

        validator_id: int

    ) -> Dict[str, Any]:

        stake = random.randint(

            self.min_stake,

            self.max_stake
        )

        validator = {

            "validator_id":

                f"V{validator_id}",

            "uuid":

                str(uuid.uuid4()),

            "stake":

                stake,

            "reputation":

                round(
                    random.uniform(
                        0.60,
                        1.00
                    ),
                    3
                ),

            "uptime":

                round(
                    random.uniform(
                        90.0,
                        100.0
                    ),
                    2
                ),

            "response_time_ms":

                round(
                    random.uniform(
                        1,
                        50
                    ),
                    2
                ),

            "successful_blocks":

                random.randint(
                    0,
                    500
                ),

            "malicious_activity":

                random.choice(
                    [False, False, False, True]
                ),

            "active":

                True,

            "created_at":

                datetime.now()
                .isoformat()
        }

        return validator

    # ===================================================
    # Generate Validator Pool
    # ===================================================

    def generate_validators(

        self,

        num_validators: int

    ) -> List[Dict]:

        validators = []

        self.logger.info(

            f"Generating "
            f"{num_validators} validators"
        )

        for validator_id in range(

            1,

            num_validators + 1
        ):

            validator = (

                self.generate_validator(
                    validator_id
                )
            )

            validators.append(
                validator
            )

        self.logger.info(

            "Validator pool generated"
        )

        return validators

    # ===================================================
    # Validator Eligibility
    # ===================================================

    def evaluate_eligibility(

        self,

        validator: Dict

    ) -> bool:

        if validator["stake"] < 500:

            return False

        if validator["reputation"] < 0.70:

            return False

        if validator["uptime"] < 95:

            return False

        if validator["malicious_activity"]:

            return False

        return True

    # ===================================================
    # Eligible Validator Pool
    # ===================================================

    def get_eligible_validators(

        self,

        validators: List[Dict]

    ) -> List[Dict]:

        eligible = []

        for validator in validators:

            if self.evaluate_eligibility(
                validator
            ):

                eligible.append(
                    validator
                )

        return eligible

    # ===================================================
    # QRNG-Based Validator Selection
    # ===================================================

    def select_validator_qrng(

        self,

        validators: List[Dict]

    ) -> Dict:

        eligible = (

            self.get_eligible_validators(
                validators
            )
        )

        if not eligible:

            raise ValueError(

                "No eligible validators"
            )

        selected = random.choice(
            eligible
        )

        return selected

    # ===================================================
    # QRNG Leader Election
    # ===================================================

    def elect_leader(

        self,

        validators: List[Dict]

    ) -> Dict:

        leader = (

            self.select_validator_qrng(
                validators
            )
        )

        return {

            "leader_id":

                leader[
                    "validator_id"
                ],

            "stake":

                leader["stake"],

            "reputation":

                leader[
                    "reputation"
                ]
        }

    # ===================================================
    # Validator Statistics
    # ===================================================

    def calculate_statistics(

        self,

        validators: List[Dict]

    ) -> Dict:

        stakes = [

            v["stake"]

            for v in validators
        ]

        reputations = [

            v["reputation"]

            for v in validators
        ]

        uptimes = [

            v["uptime"]

            for v in validators
        ]

        return {

            "total_validators":

                len(validators),

            "average_stake":

                round(
                    statistics.mean(
                        stakes
                    ),
                    2
                ),

            "average_reputation":

                round(
                    statistics.mean(
                        reputations
                    ),
                    3
                ),

            "average_uptime":

                round(
                    statistics.mean(
                        uptimes
                    ),
                    2
                ),

            "eligible_validators":

                len(
                    self.get_eligible_validators(
                        validators
                    )
                )
        }

    # ===================================================
    # Export JSON
    # ===================================================

    def export_json(

        self,

        validators: List[Dict],

        filename: str

    ):

        with open(

            filename,

            "w"
        ) as file:

            json.dump(

                validators,

                file,

                indent=4
            )

        self.logger.info(

            f"Saved {filename}"
        )

    # ===================================================
    # Export CSV
    # ===================================================

    def export_csv(

        self,

        validators: List[Dict],

        filename: str

    ):

        if not validators:

            return

        with open(

            filename,

            "w",

            newline=""
        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=
                validators[0].keys()
            )

            writer.writeheader()

            writer.writerows(
                validators
            )

        self.logger.info(

            f"Saved {filename}"
        )


# =======================================================
# Main Execution
# =======================================================

if __name__ == "__main__":

    generator = ValidatorGenerator()

    validators = (

        generator.generate_validators(
            25
        )
    )

    stats = (

        generator.calculate_statistics(
            validators
        )
    )

    leader = (

        generator.elect_leader(
            validators
        )
    )

    print("\nValidator Statistics\n")

    for key, value in stats.items():

        print(
            f"{key}: {value}"
        )

    print("\nSelected Leader\n")

    for key, value in leader.items():

        print(
            f"{key}: {value}"
        )

    generator.export_json(

        validators,

        "validators.json"
    )

    generator.export_csv(

        validators,

        "validators.csv"
    )
