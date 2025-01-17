# The "traversal-based" solution to bipartitioning is much more effecient than the graph coloring approach, 
# but the graph coloring approach can solve a more general set of problems. We can notice 
# that there are in fact only 2 solutions to a biparitionable graph, and they are mirrors of each 
# other. Further, once we pick the group for any single node, we are locked into the potential
# solution. This reduces the amount of work SIGNIFICANTLY. But if there are more than 2 groups, 
# then the number of possible solutions increases quickly, and we can't just bounce back and 
# forth between 2 groups. It turns out, we must essentially try every possible coloring and then 
# see whether the coloring is valid.
#
# The number of colorings of any graph is the number of colors (C) raised to the power of the number
# of nodes (N) or C^N. This is because for the first node, we can pick any of C colors. For the 
# second node, we can again pick any of C colors, and so on. Thus C * C * C * ... * C, where there 
# are N Cs. Most of those colorings are not valid. Indeed, we could prune some possibilities if we 
# used the edge relationships and ruled out previously assigned colors from surrounding nodes 
# from those being considered, since the actual number of choices of color for a node is 
# C - (# of surrounding colors). In practice, we will end up checking closer to C colors, since 
# when we first arrive at a node, most of the surrounding colors have not been set, and even the 
# color of the node we came from could have been chosen in error. It turns out that we _will_ make 
# use of the adjacent colors as we are building out possible coloring to help us reject invalid 
# colorings as soon as possible, though without the complication of following edges to determine 
# the next nodes to color. Avoiding the edge following will also simplify our backtracking code when
#  we unroll previously made erroneous decisions.
#
# To return to the complexity anaylsis, we must keep in mind that while there are C^N coloring 
# combinations (note the edge independency in that calculation, since the total number of colorings 
# doesn't depend on the graph connectivity), conceptually, for each combination, we then need to 
# validate the coloring by checking that each of the N nodes does not have the same color as any of 
# its E neighbors. This is our familiar O(N+E) term. So to fully generate all combinations and find 
# a correct coloring could be as high as O((N+E)C^N). In practice, the C^N term alone is so much
# more important, that we generally characterize the entire run time as the exponential O(C^N). 
# This is convenient, since our approach below blends the combination generation and the checking. 
# Rather than assigning every possible color combination to every node, then checking the validity 
# of each, instead we only continue color assignments that _could_ still be valid. That is, we stop 
# exploring a combination that becomes invalid, where we cannot assign a color because it would 
# conflict with an already assigned adjacent color. In the worst case, we could still end up 
# generatinng every possible combination (try to imagine a graph where it continues to look possible
# until we reach the final node), so we must still consider this aproach to be O(C^N), but on average, 
# we will be able to prune large numbers of combinations from every being considered or validated.
#
# This is still TERRIBLE! For "reasonably" sized graphs it will be manageable, but the required 
# time grows very quickly with the number of nodes (less so with the number of colors). Graph coloring 
# is an "NP-complete" problem. It has no known solution better than exponential time, but given a 
# valid solution, we can verify it in polynomial time, O(N+E). We don't know for certain that there 
# is no solution better than exponential, but another interesting property of NP-complete problems 
# is that all members of the class are equivalent, in that if we found a better approach for one, 
# it could be aplied to all. And there are many problems in the class that we are pretty sure have 
# no better solutions than exponential! This remains an area of very important research in Computer 
# Science.
#
# The space complexity grows the same as the "traversal-based" solution. We will recurse at most N 
# calls deep (O(N)), we add colors to the dictionary as we recurse (O(N)), and for each call frame, 
# the size of the adjacent color set depends on the number of edges, with at most 2E edges being in 
# memory at once (for the nodes on each end of each edge, so O(E)). This gives us space complexity 
# of O(N+E).
#
# Therefore, this approach to determining whether there is a bipartition has exponential time 
# complexity O(C^N) and linear space complexity O(N+E). As a result, we should prefer the "traversal-based" 
# approach if we are only interested in bipartioning, but if we have a problem involving a larger 
# number of groups (colors), then a graph coloration approach is unavoidable.

def possible_coloration(dislikes, node_idx, nodes, colors, num_colors):
    # If we've processed all the nodes, then we have found a coloring
    if node_idx == len(nodes):
        return colors

    # Notice that we are not using the edge information AT ALL for working our way through the 
    # nodes. We are simply visiting them in the order they appeared as keys in the adjacency data 
    # (our recursive calls just step to the next index number). This means that we will never walk 
    # back around to the same node as we could with BFS/DFS. While the adjacency data is NOT used 
    # to determine the order we visit nodes, we DO use it to find the neighbors to figure out which 
    # colors are available for use to try coloring the current node.

    node = nodes[node_idx]
    neighbors = dislikes[node]

    # Get a set of all the colors currently used by the neighbors. We use `get` to look up each 
    # node, since it will not error if the neighbor has not yet been colored. Instead it will return
    # whatever value we set as the default (here -1). Since our iteration over possible colors 
    # start from 0, any -1 appearing in the set of neighbor colors will not restrict the colors we 
    # try.

    adj_colors = {colors.get(n, -1) for n in neighbors}
    for color in range(num_colors):
        # Skip this color if a neighbor is already using it
        if color in adj_colors:
            continue

        # Color the node with this candidate color
        colors[node] = color

        # Recursively try to color the remaining nodes having used the current candidate color, 
        # starting with the next node (the current node index + 1)
        coloring = possible_coloration(dislikes=dislikes, node_idx=node_idx + 1, nodes=nodes, colors=colors, num_colors=num_colors)

        # If we were able to color the remaining nodes, then the attempted coloring of the current 
        # node worked. We have found a valid coloring for the current node, so return it.
        if coloring is not None:
            return coloring

        # Otherwise, we were unable to color the remaining nodes, so we'll loop to the next color 
        # and try again.

    # We tried all possible colors and could not find a valid coloration, so coloring this node 
    # failed. If this was a recursive call, then the parent call will try picking a different color, 
    # then try coloring this node again. However, we need to remove the attempted coloring for the 
    # current node, since picked colors are used by adjacent nodes to see which colors to skip, if 
    # we leave this color in place, then return far up enough, it's possible the color we leave 
    # behind could make it impossible to find a valid coloring. We might not have even attempted to 
    # color this node (if all neighbors already used all colors), so use the version of `pop` that 
    # takes a default value so that no error occurs when we try to remove the key. The value doesn't 
    # matter since we're not using it for anything (-1 used for consistency with the previous `get` 
    # call).

    colors.pop(node, -1)

    # Return None (rather than the color data) to indicate that no valid coloring was found for this node.
    return None


# Check for bipartionability by trying to color the dislikes graph with 2 colors such that no 
# adjacent node uses the same color. We call this graph coloring as it is related to the idea of c
# oloring regions on a map, where each region that shares a border is connected by an edge. We can 
# color the map regions such that no two adjacent regions share the same color if and only if we 
# are able to assign colors to each of the nodes such that no two adjacent nodes share the same 
# color. While this approach is not required to determine biparitionability, if we have more than 
# two groupings, then this becomes the correct approach.
#
# Learn mentioned the example of scheduling class exams for students given a number of available 
# schedule slots, such that no two exams taken by a single student occur at the same time. We could 
# could use a graph where classes share an edge if the same student is taking them. We could then 
# try to color the graph with the number of colors corresponding to the available schedule slots. 
# If a coloring exists, that will give us a schedule in which no student will have two tests during 
# the same slot. Interestingly, such a coloring is not guaranteed to the be the _minimum_ coloring 
# (using the fewest possible colors). That is, just because we can find a 4-coloring (a coloring 
# using 4 colors) does not mean there doesn't also exist a 3-coloring. The only way currently known 
# to find the minimum coloring is to try all possible number of colors.

def possible_bipartition(dislikes):
    nodes = list(dislikes.keys())
    colors = {}
    return None is not possible_coloration(dislikes=dislikes, nodes=nodes, node_idx=0, colors=colors, num_colors=2)
