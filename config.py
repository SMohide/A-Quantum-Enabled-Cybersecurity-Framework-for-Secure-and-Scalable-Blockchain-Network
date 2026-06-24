"""
QECF Configuration File

A Quantum-Enabled Cybersecurity Framework
for Secure and Scalable Blockchain Networks
"""

import os
from pathlib import Path

# ============================================================================
# PROJECT PATHS
# ============================================================================

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

MODELS_DIR = BASE_DIR / "models"
RESULTS_DIR = BASE_DIR / "results"
LOGS_DIR = BASE_DIR / "logs"

for directory in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    RESULTS_DIR,
    LOGS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

# ============================================================================
# BLOCKCHAIN NETWORK CONFIGURATION
# ============================================================================

NETWORK_CONFIG = {
    "network_type": "permissioned",
    "min_nodes": 20,
    "max_nodes": 200,
    "validators": 25,
    "block_size": 200,
    "transaction_rate": 200,
    "consensus": "quantum_bft",
    "random_seed": 42
}

# ============================================================================
# QUANTUM THREAT CONFIGURATION
# ============================================================================

THREAT_CONFIG = {
    "threat_levels": {
        0: "No Threat",
        1: "Emerging Quantum Capability",
        2: "Quantum Attack Detected"
    },

    "low_threshold": 0.30,
    "medium_threshold": 0.70,
    "high_threshold": 1.00
}

# ============================================================================
# POST QUANTUM CRYPTOGRAPHY
# ============================================================================

PQC_CONFIG = {
    "algorithms": [
        "Dilithium",
        "Falcon",
        "SPHINCS+"
    ],

    "default_scheme": "Dilithium",

    "signature_validation": True,

    "nist_compliance": True
}

# ============================================================================
# QUANTUM KEY DISTRIBUTION
# ============================================================================

QKD_CONFIG = {

    "enabled": True,

    "key_rates_kbps": [
        5,
        10,
        25,
        50
    ],

    "eavesdropping_detection": True,

    "key_refresh_interval": 300,

    "communication_security": "information_theoretic"
}

# ============================================================================
# QRNG CONFIGURATION
# ============================================================================

QRNG_CONFIG = {

    "enabled": True,

    "entropy_threshold": 0.95,

    "leader_selection": "quantum_random",

    "validator_selection": "quantum_random"
}

# ============================================================================
# ADAPTIVE SECURITY CONFIGURATION
# ============================================================================

ADAPTIVE_SECURITY_CONFIG = {

    "enabled": True,

    "latency_threshold_ms": 1000,

    "consensus_round_threshold": 10,

    "dynamic_validator_scaling": True,

    "adaptive_key_rotation": True
}

# ============================================================================
# QUANTUM RESILIENCE INDEX (QRI)
# ============================================================================

QRI_CONFIG = {

    "authentication_weight": 0.25,

    "communication_weight": 0.25,

    "consensus_weight": 0.25,

    "adaptability_weight": 0.25
}

# ============================================================================
# SECURITY STATE MODEL
# ============================================================================

SECURITY_STATE_CONFIG = {

    "communication_security_weight": 0.30,

    "authentication_weight": 0.35,

    "consensus_integrity_weight": 0.35
}

# ============================================================================
# EXPERIMENT CONFIGURATION
# ============================================================================

EXPERIMENT_CONFIG = {

    "simulation_runs": 10,

    "cross_validation": False,

    "generate_plots": True,

    "save_results": True,

    "save_logs": True
}

# ============================================================================
# EVALUATION METRICS
# ============================================================================

EVALUATION_CONFIG = {

    "metrics": [

        "security_coverage",

        "qkd_latency",

        "pqc_validation_time",

        "consensus_entropy",

        "block_confirmation_time",

        "qri_score"
    ]
}

# ============================================================================
# COMPUTATIONAL RESOURCES
# ============================================================================

COMPUTE_CONFIG = {

    "device": "cpu",

    "num_workers": 4,

    "deterministic": True
}

# ============================================================================
# LOGGING
# ============================================================================

LOGGING_CONFIG = {

    "level": "INFO",

    "log_file": LOGS_DIR / "qecf.log",

    "log_to_file": True
}

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_config(config_name):

    config_map = {

        "network": NETWORK_CONFIG,

        "threat": THREAT_CONFIG,

        "pqc": PQC_CONFIG,

        "qkd": QKD_CONFIG,

        "qrng": QRNG_CONFIG,

        "adaptive": ADAPTIVE_SECURITY_CONFIG,

        "qri": QRI_CONFIG,

        "security": SECURITY_STATE_CONFIG,

        "evaluation": EVALUATION_CONFIG,

        "experiment": EXPERIMENT_CONFIG,

        "compute": COMPUTE_CONFIG,

        "logging": LOGGING_CONFIG
    }

    return config_map.get(config_name, {})


def print_config():

    print("=" * 80)
    print("QECF FRAMEWORK CONFIGURATION")
    print("=" * 80)

    print(f"Base Directory: {BASE_DIR}")
    print(f"Data Directory: {DATA_DIR}")

    print(f"Network Size: {NETWORK_CONFIG['min_nodes']} - {NETWORK_CONFIG['max_nodes']}")

    print(f"PQC Scheme: {PQC_CONFIG['default_scheme']}")

    print(f"QKD Enabled: {QKD_CONFIG['enabled']}")

    print(f"QRNG Enabled: {QRNG_CONFIG['enabled']}")

    print("=" * 80)


if __name__ == "__main__":
    print_config()
