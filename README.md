# Bipartition Graph Livecode

This repository is the classroom activity for the Graphs Pt. 1 Roundtable in Unit 4.

## Learning Goals 
- Practice working with and traversing an adjacency dictionary in order to model and manipulate a graph structure.
  
## One-Time Activity Setup

Follow these directions once, at the beginning of the activity:


1. Navigate to the folder where you wish to save activities. This could be your `projects` folder, or you may want to create a new folder for all of your activities.

   If you followed Ada's recommended file system structure, you can navigate to your projects folder with the following command:

   ```bash
   $ cd ~/Developer/projects
   ```

   Or, if you want to create a new folder for all of your activities:

   ```bash
   $ cd ~/Developer
   $ mkdir activities
   $ cd activities
   ```

   If you've already created an activities directory, you can navigate to it with the following command:

   ```bash
   $ cd ~/Developer/activities
   ```

2. In Github click on the "Fork" button to fork the repository to your Github account.  This will make a copy of the activity in your Github account. 

3. "Clone" the activity into your working folder. This command makes a new folder named for the activity repository, and then puts the activity into this new folder.

   ```bash
   $ git clone <clone_url_for_the_activity>
   ```

   The `<>` syntax indicates a placeholder. You should replace `<clone_url_for_the_activity>` with the actual URL you'd use to clone this repository. If you click the green "Code" button on the GitHub page for this repository, you'll see a URL that you can copy to your clipboard.
 
   Use `ls` to confirm there's a new activity folder

4. Move your location into this activity folder

   ```bash
   $ cd <repository_directory>
   ```

   The `<repository_directory>` placeholder should be replaced with the name of the activity folder. If you're not sure what the folder is named, remember that you can use `ls` to list the contents of your current location.

5. Create a virtual environment named `venv` for this activity:

   ```bash
   $ python3 -m venv venv
   ```

6. Activate this environment:

   ```bash
   $ source venv/bin/activate
   ```

   Verify that you're in a python3 virtual environment by running:
   
   - `$ python --version` should output a Python 3 version
   - `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this activity with

   ```bash
   # Must be in activated virtual environment
   $ pip install -r requirements.txt
   ```

   Not all activities will have dependencies, but there will still be an included `requirements.txt` file.

Summary of one-time activity setup:
- [ ] Fork the activity repository
- [ ] `cd` into your working folder, such as your `projects` or `activities` folder
- [ ] Clone the activity onto your machine
- [ ] `cd` into the folder for the activity
- [ ] Create the virtual environment `venv`
- [ ] Activate the virtual environment `venv`
- [ ] Install the dependencies with `pip`

## Activity Development Workflow

1. When working on this activity, always ensure that your virtual environment is activated:

   ```bash
   $ source venv/bin/activate
   ```

2. If you want to work on another project from the same terminal window, you should deactivate the virtual environment when you are done working on the activity:

   ```bash
   $ deactivate
   ```

## Live Code

### Bipartition Graph
Problem Statement:

Create a function `possible_bipartition` which takes in an adjacency dictionary representing a graph of puppies, `dislikes`. The function should determine whether the puppies can be divided into two groups where no two puppies that dislike each other are in the same group. A graph that can be so partitioned is referred to as being bipartite (bye-par-TEET).

Given a set of N puppies, we would like to split them into two groups of any size to use two play areas.

Formally, `dislikes[i] = [a, b]` means puppy `i` cannot be in the same group as puppy `a` or puppy `b`.

Dislike is mutual. If puppy `a` dislikes puppy `b`, puppy `b` also dislikes puppy `a`. Two puppies that dislike each other will get into a tussle, which though adorable, could lead to puppy injury. We can't have that!

Return `True` if and only if it is possible to split the puppies into two groups where no tussling will occur. Otherwise, return `False`.

### Example 1
*Input*:

    dislikes = { 
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Cooper": ["Nala", "Bruno"],
        "Spot": ["Nala"],
        "Bruno": ["Cooper"]
    }
*Output*: `True`

Explanation:

- Fido can be placed in either group since Fido gets along with every pup.
- Nala can be placed in Group 1. Cooper and Spot will not be able to be placed in Group 1.
- Cooper can be placed in Group 2, avoiding Nala in Group 1. Bruno will not be able to be placed in Group 2.
- Spot can be placed in Group 2, avoiding Nala in Group 1.
- Bruno can be placed in Group 1, avoiding Cooper in Group 2.
-  None of the pups who would tussle with each other are placed in the same group.

### Example 2:
*Input*:

    dislikes = {
        "Fido": [],
        "Nala": ["Cooper", "Spot"],
        "Cooper": ["Nala", "Spot"],
        "Spot": ["Nala", "Cooper"]
    }

*Output*: `False`

Explanation:
- Fido can be placed in either group since Fido gets along with every pup.
- Nala can be placed in Group 1. Cooper and Spot will not be able to be placed in Group 1.
- Cooper can be placed in Group 2, avoiding Nala in Group 1. Spot will not be able to be placed in Group 2.
- Spot cannot be placed in Group 1 with Nala, nor can Spot be placed into Group 2 with Cooper.
- There is no way to place all of the pups into two separate groups such that no pups would tussle with each other.

### Resources
Bipartitioning is a special case of N-coloring a graph. A graph can be N-colored if we can color in the nodes of the graph with N colors such that no two adjacent nodes share the same color.

Graph coloring comes from the problem of coloring a map such that no two countries sharing a border are colored with the same color. Most real-world maps can be represented by a planar graph (a graph that can be drawn such that no edges cross). It has been shown that any planar graph can be colored with at most 4 colors!

Bipartite graphs

https://www.baeldung.com/cs/graphs-bipartite

Graph coloring

https://en.wikipedia.org/wiki/Graph_coloring

https://www.geeksforgeeks.org/graph-coloring-applications/

https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/


## Running Tests
Use the tests provided in the `test_kth_smallest.py` file to verify that your code is working correctly. You can verify the tests are working in one of two ways:

1. Run `pytest` in the terminal (make sure you are in the venv!)
2. Set up the testing environment in the VSCode Testing Pane
   1. Click on the beaker icon and click `Configure Python Tests`
   2. Select `pytest` from the list that appears
   3. Select `tests` from the new list that appears.
3. Verify the tests show up in the Testing Pane.
4. Run the tests to make sure they are all passing!