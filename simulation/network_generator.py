class NetworkGenerator:

    def __init__(
        self,
        min_nodes=20,
        max_nodes=200
    ):
        self.min_nodes = min_nodes
        self.max_nodes = max_nodes

    def generate_network(self, num_nodes):

        nodes = []

        for i in range(num_nodes):

            node = {
                "node_id": f"N{i+1}",
                "status": "active",
                "reputation": 1.0
            }

            nodes.append(node)

        return nodes
