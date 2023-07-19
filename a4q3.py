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
def copy(node_chain):
    """
    Make a completely new copy of the given node chain.
    :param node_chain: The node chain
    :return: A copy of the new node chain
    """
    if node_chain is None:
        return None
    elif node_chain.get_next() is None:
        return n.Node(node_chain.get_data())
    else:
        new_node_chain = n.Node(node_chain.get_data())
        new_chain_next = copy(node_chain.get_next())
        new_node_chain.set_next(new_chain_next)
        return new_node_chain
def replace(node_chain, target, replacement):
    """
    Replace every occurrence of the data target in node_chain with replacement.
    :param node_chain: The node chain
    :param target: The target value to replace
    :param replacement: The replacement value
    :return: The reference to the first node in the chain
    """
    if node_chain is None:
        return None
    else:
        if node_chain.get_data() == target:
            node_chain.set_data(replacement)
        replace(node_chain.get_next(), target, replacement)
        return node_chain