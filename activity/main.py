def possible_bipartition(dislikes):
    pass
    group1 = set()
    group2 = set()

    # pending_comb = {}

    for puppy_a, puppy_b_list in dislikes.items():
        # print(puppy_a)
        # print(puppy_b_list)

        # if puppy_b_list is empty, puppy_a could be placed in both groups


        # if puppy_a exist in group1, 
            # if any puppy_b exist in group1, 
                # return false
            # put all puppy_b in group2 
        # if puppy_a exist in group2
            # if any puppy_b exist in group2, 
                # return false
            # put all puppy_b in group1
        
        # if puppy_a do not exist in both groups
            # if any puppy_b does not exist in both groups
                # put puppy_a in group1
                # put puppy_b in group2
            # if any puppy_b exist in group1
                # if other puppy_b exist in group2
                    # return false
                # if puppy_a exist in group1
                    # return false
                # put puppy a in group2
                # put puppy b in group1

            # if any puppy_b exist in group2
                # if other puppy_b exist in group1
                    # return false
                # if puppy_a exist in group2
                    # return false
                # put puppy a in group1

        if not puppy_b_list:
            group1.add(puppy_a)
            group2.add(puppy_a)
            continue

        if puppy_a in group1:
            if itemlist_exists_in_set(puppy_b_list, group1):
                return False
            group2.update(puppy_b_list)

        elif puppy_a in group2:
            if itemlist_exists_in_set(puppy_b_list, group2):
                return False
            group1.update(puppy_b_list)

        elif puppy_a not in group1 and puppy_a not in group2:
            # check if puppy_b_list appears in both groups
            if items_in_both_sets(puppy_b_list, group1, group2):
                return False
            
            if all_items_absent_from_two_sets(puppy_b_list, group1, group2):
                group1.add(puppy_a)
                group2.update(puppy_b_list)

                # pending_comb[puppy_a] = puppy_b_list
                continue

            for puppy_b in puppy_b_list:
                if puppy_b in group1:
                    group1.update(puppy_b_list)
                    group2.add(puppy_a)
                    break

                elif puppy_b in group2:
                    group1.add(puppy_a)
                    group2.update(puppy_b_list)

            # print(group1)
            # print(group2)


        # if pending_comb:
        #     for puppy_a, puppy_b_list in pending_comb.items():
        #         if puppy_a in group1:
        #             if itemlist_exists_in_set(puppy_b_list, group1):
        #                 return False
        #             group2.update(puppy_b_list)

        #         elif puppy_a in group2:
        #             if itemlist_exists_in_set(puppy_b_list, group2):
        #                 return False
        #             group1.update(puppy_b_list)

        #         elif puppy_a not in group1 and puppy_a not in group2:
        #             # check if puppy_b_list appears in both groups
        #             if items_in_both_sets(puppy_b_list, group1, group2):
        #                 return False
                    
        #             if all_items_absent_from_two_sets(puppy_b_list, group1, group2):
        #                 group1.add(puppy_a)
        #                 group2.update(puppy_b_list)
                
        #             for puppy_b in puppy_b_list:
        #                 if puppy_b in group1:
        #                     group1.update(puppy_b_list)
        #                     group2.add(puppy_a)
        #                     break

        #                 elif puppy_b in group2:
        #                     group1.add(puppy_a)
        #                     group2.update(puppy_b_list)


    return True


def itemlist_exists_in_set(itemlist, item_set):
    for item in itemlist:
        if item in item_set:
            return True

    return False

def items_in_both_sets(items, set1, set2):
    for puppy in items:
        if puppy in set1 and puppy in set2:
            return True
    
    return False

def all_items_absent_from_two_sets(items, set1, set2):
    for item in items:
        if item in set1 or item in set2:
            return False  # Found an item in either set
        
    return True  # All items are absent from both sets

# dislikes = { 
#     "Fido": [],
#     "Nala": ["Cooper", "Spot"],
#     "Cooper": ["Nala", "Bruno"],
#     "Spot": ["Nala"],
#     "Bruno": ["Cooper"]
# }

#Arrange
# dislikes = {
#     "Fido": [],
#     "Nala": ["Cooper", "Spot"],
#     "Cooper": ["Nala", "Spot"],
#     "Spot": ["Nala", "Cooper"]
# }

#Act/Assert
# assert possible_bipartition(dislikes) is False


dislikes = {
    "Alfie": ["T-Bone"],
    "Fido": ["James", "Rufus"],
    "James": ["Fido"],
    "Rufus": ["Fido", "Scruffy", "T-Bone"],
    "Scruffy": ["Rufus"],
    "T-Bone": ["Alfie", "Rufus"]
}

print(possible_bipartition(dislikes))