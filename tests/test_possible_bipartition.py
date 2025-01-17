from activity.main import possible_bipartition
# Uncomment the line below and comment the line above to try out the tests using the color based solution!
# from activity.color_based_solution import possible_bipartition
import pytest 

def test_possible_bipartition_with_acyclic_graph_and_island():
    #Arrange
    dislikes = { 
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Cooper": ["Nala", "Bruno"],
        "Spot": ["Nala"],
        "Bruno": ["Cooper"]
    }

    #Act/Assert
    assert possible_bipartition(dislikes) is True

def test_possible_bipartition_three_cycle_graph_and_island():
    #Arrange
    dislikes = {
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Cooper": ["Nala", "Spot"],
        "Spot": ["Nala", "Cooper"]
    }

    #Act/Assert
    assert possible_bipartition(dislikes) is False

def test_possible_bipartition_four_cycle_graph():
    dislikes = {
        "Fido": ["Spot", "Nala"],
        "Nala": ["Fido", "Cooper"],
        "Cooper": ["Nala", "Spot"],
        "Spot": ["Cooper", "Fido"]
    }

    #Act/Assert
    assert possible_bipartition(dislikes) is True

def test_possible_bipartition_five_cycle_graph():
    dislikes = {
        "Rufus": ["James", "Scruffy"],
        "James": ["Rufus", "Alfie"],
        "Alfie": ["T-Bone", "James"],
        "T-Bone": ["Alfie", "Scruffy"],
        "Scruffy": ["Rufus", "T-Bone"]
    }

    #Act/Assert
    assert possible_bipartition(dislikes) is False

def test_possible_bipartition_acyclic_graph():
    dislikes = {
        "Fido": ["Alfie", "Bruno"],
        "Rufus": ["James", "Scruffy"],
        "James": ["Rufus", "Alfie"],
        "Alfie": ["Fido", "James"],
        "T-Bone": ["Scruffy"],
        "Scruffy": ["Rufus", "T-Bone"],
        "Bruno": ["Fido"]
    }

    #Act/Assert
    assert possible_bipartition(dislikes) is True

def test_possible_bipartition_empty_graph():
    #Arrange/Act/Assert
    assert possible_bipartition({}) is True

def test_possible_bipartition_five_cycle_with_island():
    #Arrange
    dislikes = {
        "Fido": ["Alfie", "Bruno"],
        "Rufus": ["James", "Scruffy"],
        "James": ["Rufus", "Alfie"],
        "Alfie": ["Fido", "James", "T-Bone"],
        "T-Bone": ["Alfie", "Scruffy"],
        "Scruffy": ["Rufus", "T-Bone"],
        "Bruno": ["Fido"],
        "Spot": ["Nala"],
        "Nala": ["Spot"]
    }

    #Act/Assert
    assert possible_bipartition(dislikes) is False

def test_possible_bipartition_acyclic_graph_with_island():
    #Arrange
    dislikes = {
        "Fido": [],
        "Rufus": [],
        "James": [],
        "Alfie": ["T-Bone"],
        "T-Bone": ["Alfie", "Scruffy"],
        "Scruffy": ["T-Bone"],
        "Bruno": ["Nala"],
        "Spot": ["Nala"],
        "Nala": ["Bruno", "Spot"]
    }
        
    #Act/Assert
    assert possible_bipartition(dislikes) is True

def test_possible_bipartition_acyclic_graph_with_ordering():
    dislikes = {
        "Alfie": ["T-Bone"], 
        "Fido": ["James", "Rufus"], 
        "James": ["Fido"], 
        "Rufus": ["Fido", "Scruffy", "T-Bone"], 
        "Scruffy": ["Rufus"], 
        "T-Bone": ["Alfie", "Rufus"]
    }

    #Act/Assert
    assert possible_bipartition(dislikes) is True
