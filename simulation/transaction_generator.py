import uuid
import random
import json
import csv
import logging
import statistics

from datetime import datetime
from typing import Dict, List, Any


class TransactionGenerator:
    """
    Transaction Generator

    Generates synthetic blockchain transactions
    for healthcare blockchain simulations.

    Supports:

    - Standard transactions
    - High-value transactions
    - Smart contract transactions
    - Emergency transactions
    """

    TRANSACTION_TYPES = [

        "STANDARD",

        "HEALTHCARE_RECORD",

        "SMART_CONTRACT",

        "EMERGENCY_UPDATE",

        "AUDIT_LOG"
    ]

    PQC_SCHEMES = [

        "Dilithium",

        "Falcon",

        "SPHINCS+"
    ]

    def __init__(

        self,

        min_amount: int = 10,

        max_amount: int = 100000,

        random_seed: int = 42

    ):

        self.min_amount = min_amount
        self.max_amount = max_amount

        random.seed(random_seed)

        logging.basicConfig(

            level=logging.INFO,

            format="%(asctime)s - %(levelname)s - %(message)s"
        )

        self.logger = logging.getLogger(

            self.__class__.__name__
        )

        self.logger.info(

            "Transaction Generator Initialized"
        )

    # ===================================================
    # Generate Single Transaction
    # ===================================================

    def generate_transaction(

        self,

        transaction_id: int

    ) -> Dict[str, Any]:

        amount = random.randint(

            self.min_amount,

            self.max_amount
        )

        transaction = {

            "tx_id":

                f"TX{transaction_id}",

            "uuid":

                str(uuid.uuid4()),

            "sender":

                f"N{random.randint(1,200)}",

            "receiver":

                f"N{random.randint(1,200)}",

            "amount":

                amount,

            "transaction_type":

                random.choice(
                    self.TRANSACTION_TYPES
                ),

            "pqc_scheme":

                random.choice(
                    self.PQC_SCHEMES
                ),

            "signature_size":

                random.randint(
                    1000,
                    5000
                ),

            "verification_time_ms":

                round(
                    random.uniform(
                        0.5,
                        10.0
                    ),
                    3
                ),

            "gas_fee":

                round(
                    random.uniform(
                        0.01,
                        10.0
                    ),
                    3
                ),

            "priority":

                random.choice(
                    [
                        "LOW",
                        "MEDIUM",
                        "HIGH"
                    ]
                ),

            "status":

                "PENDING",

            "timestamp":

                datetime.now()
                .isoformat()
        }

        return transaction

    # ===================================================
    # Generate Transaction Pool
    # ===================================================

    def generate_transactions(

        self,

        num_transactions: int

    ) -> List[Dict]:

        self.logger.info(

            f"Generating "
            f"{num_transactions} transactions"
        )

        transactions = []

        for tx_id in range(

            1,

            num_transactions + 1
        ):

            transaction = (

                self.generate_transaction(
                    tx_id
                )
            )

            transactions.append(
                transaction
            )

        return transactions

    # ===================================================
    # Validate Transaction
    # ===================================================

    def validate_transaction(

        self,

        transaction: Dict

    ) -> bool:

        if transaction["amount"] <= 0:

            return False

        if transaction["sender"] == transaction["receiver"]:

            return False

        if transaction["signature_size"] <= 0:

            return False

        return True

    # ===================================================
    # Batch Validation
    # ===================================================

    def validate_transaction_pool(

        self,

        transactions: List[Dict]

    ) -> Dict:

        valid = 0
        invalid = 0

        for transaction in transactions:

            if self.validate_transaction(
                transaction
            ):

                transaction[
                    "status"
                ] = "VALID"

                valid += 1

            else:

                transaction[
                    "status"
                ] = "INVALID"

                invalid += 1

        return {

            "valid":

                valid,

            "invalid":

                invalid
        }

    # ===================================================
    # Throughput Calculation
    # ===================================================

    def calculate_throughput(

        self,

        transactions: List[Dict],

        block_time_seconds: int = 10

    ) -> float:

        throughput = (

            len(transactions)

            / block_time_seconds
        )

        return round(
            throughput,
            2
        )

    # ===================================================
    # Transaction Statistics
    # ===================================================

    def calculate_statistics(

        self,

        transactions: List[Dict]

    ) -> Dict:

        amounts = [

            tx["amount"]

            for tx in transactions
        ]

        verification_times = [

            tx[
                "verification_time_ms"
            ]

            for tx in transactions
        ]

        gas_fees = [

            tx["gas_fee"]

            for tx in transactions
        ]

        return {

            "total_transactions":

                len(transactions),

            "average_amount":

                round(
                    statistics.mean(
                        amounts
                    ),
                    2
                ),

            "average_verification_time":

                round(
                    statistics.mean(
                        verification_times
                    ),
                    3
                ),

            "average_gas_fee":

                round(
                    statistics.mean(
                        gas_fees
                    ),
                    3
                ),

            "throughput_tps":

                self.calculate_throughput(
                    transactions
                )
        }

    # ===================================================
    # PQC Scheme Analysis
    # ===================================================

    def analyze_pqc_usage(

        self,

        transactions: List[Dict]

    ) -> Dict:

        results = {

            "Dilithium": 0,

            "Falcon": 0,

            "SPHINCS+": 0
        }

        for tx in transactions:

            results[
                tx["pqc_scheme"]
            ] += 1

        return results

    # ===================================================
    # Export JSON
    # ===================================================

    def export_json(

        self,

        transactions: List[Dict],

        filename: str

    ):

        with open(

            filename,

            "w"
        ) as file:

            json.dump(

                transactions,

                file,

                indent=4
            )

    # ===================================================
    # Export CSV
    # ===================================================

    def export_csv(

        self,

        transactions: List[Dict],

        filename: str

    ):

        if not transactions:

            return

        with open(

            filename,

            "w",

            newline=""
        ) as file:

            writer = csv.DictWriter(

                file,

                fieldnames=
                transactions[0].keys()
            )

            writer.writeheader()

            writer.writerows(
                transactions
            )

    # ===================================================
    # Generate Experiment Dataset
    # ===================================================

    def generate_experiment_dataset(

        self,

        transaction_count: int

    ) -> Dict:

        transactions = (

            self.generate_transactions(
                transaction_count
            )
        )

        validation_report = (

            self.validate_transaction_pool(
                transactions
            )
        )

        statistics_report = (

            self.calculate_statistics(
                transactions
            )
        )

        pqc_report = (

            self.analyze_pqc_usage(
                transactions
            )
        )

        return {

            "transactions":

                transactions,

            "validation":

                validation_report,

            "statistics":

                statistics_report,

            "pqc_usage":

                pqc_report
        }


# =======================================================
# Main Execution
# =======================================================

if __name__ == "__main__":

    generator = TransactionGenerator()

    dataset = (

        generator.generate_experiment_dataset(
            500
        )
    )

    print("\nTransaction Statistics\n")

    for key, value in (

        dataset[
            "statistics"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )

    print("\nPQC Usage\n")

    for key, value in (

        dataset[
            "pqc_usage"
        ].items()
    ):

        print(
            f"{key}: {value}"
        )

    generator.export_json(

        dataset["transactions"],

        "transactions.json"
    )

    generator.export_csv(

        dataset["transactions"],

        "transactions.csv"
    )
