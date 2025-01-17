NUM_GROUPS = 2

# In place of the visited list, dfs tracks where it's been in the graph  using the groups dictionary. When a node has been placed in a group, it is added to groups as a key, with its group as the value. Thus, once grouped, a node will not be visited again (we may perform a recursive call, again, but we won't fully "process" the node again). So we will visit each of the N nodes, and iterate over each node's edges. Because each node is visited only once, each edge is examined at most twice (from the nodes on either end of the edge) for at most 2E total edge visits. This is the same argument for regular DFS time complexity, resulting in the expected O(N+E) time complexity.
#
# Space complexity has the same growth concerns as recursive dfs. We can recurse no deeper than there are nodes. The only variable-sized data we create is the groups dictionary, which will have an entry for each of the N nodes. So the overall space complexity will remain O(N).
def dfs(dislikes, current_node, groups, current_group):
    # Check whether this node has been placed already
    if current_node in groups:
        # We already placed it, so it had better match or we're in trouble, since if they don't match, it means that one adjacent node requires this node to be in group 0, but another requires this node to be in group 1, which is impossible!
        return groups[current_node] == current_group

    # This node is not placed (visited) so place it and check neighbors
    groups[current_node] = current_group

    # Any adjacent node CANNOT go in the same group. Flip the current group to the next one (0 -> 1, 1 -> 0). Modulo lets us write an expression as follows since 0 + 1 (1) mod 2 is still 1, while 1 + 1 (2) mod 2 wraps back around to 0. Recall that mod is essentially the remainder after division. 1 divided by 2 = 0R1, while 2 divided by 2 = 1R0
    next_group = (current_group + 1) % NUM_GROUPS

    neighbors = dislikes[current_node]
    for neighbor in neighbors:
        # Try to place each neighbor in the group not containing the current node.
        if not dfs(dislikes=dislikes, current_node=neighbor, groups=groups, current_group=next_group):
            return False

    return True


# While it may appear that we are calling a O(N-ish) method (dfs) inside  a loop over the N nodes, the overall time complexity remains O(N+E), the complexity of the dfs call itself. We only call dfs directly on a single node per island. So if the graph is connected, we will only call dfs a single time. On the other extreme, if every node is an island, then we will call dfs N times, but each call will visit only a single node (and E would be 0). The net result is that we will only visit N nodes total (but still can account for the number of edges E), leading to this approach overall having a time complexity of O(N+E).
#
# Space complexity is also determined by the dfs call. While we allocate the groups dictionary here, it's the dfs call that will add the pairs into it. So the only space considerations come from the dfs call, with the overall approach having a space complexity of O(N).
def possible_bipartition(dislikes):
    groups = {}

    # Loop over all the nodes in case there are islands
    for node in dislikes.keys():
        # If this node is already placed (if we reached it by traversing from some other node) then we don't need to try placing it again. Skip it.
        if groups.get(node):
            continue

        # The node wasn't placed yet (we reached the first node in an island of nodes), so try to place this node by traversing it. It's always safe to start with group 0 (no need to alternate between 0 and 1) since any valid placement of connected nodes would be equally valid if all the 0s were 1s and all the 1s were 0s. We pass the same group information so that we continue to accumulate grouping data in the initial dictionary of grouping data so that we can still detect later nodes being already placed.
        if not dfs(dislikes=dislikes, current_node=node, groups=groups, current_group=0):

            return False
    return True