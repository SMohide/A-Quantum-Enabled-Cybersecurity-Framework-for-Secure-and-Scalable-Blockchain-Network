class ThreatGenerator:

    THREAT_LEVELS = {

        0: "No Threat",

        1: "Emerging Quantum Capability",

        2: "Quantum Attack"
    }

    def generate_threat(self, level):

        return {

            "level": level,

            "description":
                self.THREAT_LEVELS[level]
        }
