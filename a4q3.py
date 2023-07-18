#Name - Harry Patel
#NSID-ozc189
#course-CMPT145
#Instructor Name-Laurissa Stilling

import node as n


def to_string(node_chain):
    """
       Create a string presentation of the node chain.
       :param node_chain: The node chain
       :return: A string representation of the nodes
       """
    if node_chain is None:
        return "EMPTY"
    elif node_chain.get_next() is None:
        return "[ " + str(node_chain.get_data()) + " | / ]"
    else:
        current_chain_data = "[ " + str(node_chain.get_data()) + " | *-]-->"
        return current_chain_data + to_string(node_chain.get_next())

