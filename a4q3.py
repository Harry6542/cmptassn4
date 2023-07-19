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
def test_to_string():
    print("Testing to_string function:")

    # An empty chain
    chain1 = None
    print("Chain 1:", to_string(chain1))

    # A chain with one node
    chain2 = n.Node(5)
    print("Chain 2:", to_string(chain2))

    # A chain with multiple nodes
    chain3 = n.Node(1, n.Node(2, n.Node(3)))
    print("Chain 3:", to_string(chain3))


def test_copy():
    print("Testing copy function:")

    # An empty chain
    chain1 = None
    copied_chain1 = copy(chain1)
    print("Copied Chain 1:", to_string(copied_chain1))

    # A chain with one node
    chain2 = n.Node(5)
    copied_chain2 = copy(chain2)
    print("Copied Chain 2:", to_string(copied_chain2))

    # A chain with multiple nodes
    chain3 = n.Node(1, n.Node(2, n.Node(3)))
    copied_chain3 = copy(chain3)
    print("Copied Chain 3:", to_string(copied_chain3))
def test_replace():
    print("Testing replace function:")

    # An empty chain
    chain1 = None
    replaced_chain1 = replace(chain1, 0, 9)
    print("Replaced Chain 1:", to_string(replaced_chain1))

    # A chain with no replacements
    chain2 = n.Node(1, n.Node(2, n.Node(3)))
    replaced_chain2 = replace(chain2, 0, 9)
    print("Replaced Chain 2:", to_string(replaced_chain2))

    # A chain with several replacements
    chain3 = n.Node(1, n.Node(2, n.Node(3, n.Node(1, n.Node(4)))))
    replaced_chain3 = replace(chain3, 1, 9)
    print("Replaced Chain 3:", to_string(replaced_chain3))

# Run the test cases
test_to_string()
test_copy()
test_replace()