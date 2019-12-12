"""
-------------------------------------------------------
Linked version of the BST ADT.
-------------------------------------------------------
Author:  Evan Attfield
ID:      180817010
Email:   attf7010@mylaurier.ca
__updated__ = "Mar 12, 2019"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy
from Queue_array import Queue

class _BST_Node:

    def __init__(self, value):
        """
        -------------------------------------------------------
        Initializes a BST node containing value. Child pointers 
        are None, height is 1.
        Use: node = _BST_Node(value)
        -------------------------------------------------------
        Parameters:
            value - value for the node (?)
        Returns:
            A _BST_Node object (_BST_Node)            
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._left = None
        self._right = None
        self._height = 1

    def _update_height(self):
        """
        -------------------------------------------------------
        Updates the height of the current node.
        Use: node._update_height()
        -------------------------------------------------------
        Returns:
            _height is 1 plus the maximum of the node's two children.
        -------------------------------------------------------
        """
        if self._left is None:
            left_height = 0
        else:
            left_height = self._left._height

        if self._right is None:
            right_height = 0
        else:
            right_height = self._right._height

        self._height = max(left_height, right_height) + 1
        
        return

    def __str__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Returns node height and value as a string - for debugging.
        -------------------------------------------------------
        """
        return "h: {}, v: {}".format(self._height, self._value)


class BST:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty BST.
        Use: bst = BST()
        -------------------------------------------------------
        Returns:
            A BST object (BST)
        -------------------------------------------------------
        """
        self._root = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if bst is empty.
        Use: b = bst.is_empty()
        -------------------------------------------------------
        Returns:
            True if bst is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._root is None

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the BST.
        Use: n = len(bst)
        -------------------------------------------------------
        Returns:
            the number of nodes in the BST.
        -------------------------------------------------------
        """
        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Use: b = bst.insert(value)
        -------------------------------------------------------
        Parameters:
            value - data to be inserted into the bst (?)
        Returns:
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        self._root, inserted = self._insert_aux(self._root, value)
        return inserted

    def _insert_aux(self, node, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the bst. Values may appear 
        only once in a tree.
        Private recursive operation called only by insert.
        Use: node, inserted = self._insert_aux(node, value)
        -------------------------------------------------------
        Parameters:
            node - a bst node (_BST_Node)
            value - data to be inserted into the node (?)
        Returns:
            node - the current node (_BST_Node)
            inserted - True if value is inserted into the BST,
                False otherwise. (boolean)
        -------------------------------------------------------
        """
        if node is None:
            # Base case: add a new node containing the value.
            node = _BST_Node(value)
            self._count += 1
            inserted = True
        elif node._value > value:
            # General case: check the left subtree.
            node._left, inserted = self._insert_aux(node._left, value)
        elif node._value < value:
            # General case: check the right subtree.
            node._right, inserted = self._insert_aux(node._right, value)
        else:
            # Base case: value is already in the BST.
            inserted = False

        if inserted:
            # Update the node height if any of its children have been changed.
            node._update_height()
        return node, inserted

    def retrieve(self, key):
        """
        -------------------------------------------------------
        Retrieves a copy of a value matching key in a BST. (Iterative)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value in the node containing key, otherwise None (?)
        -------------------------------------------------------
        """
        node = self._root
        value = None

        while node is not None and value is None:
            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                # for comparison counting
                value = deepcopy(node._value)
                
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Removes a node with a value matching key from the bst.
        Returns the value matched. Updates structure of bst as 
        required.
        Use: value = bst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - value matching key if found, otherwise None.
        -------------------------------------------------------
        """
        self._root, value = self._remove_aux(self._root, key)
        
        return value

    def _remove_aux(self, node, key):
        """
        -------------------------------------------------------
        Attempts to find a value matching key in a BST node. Deletes the node
        if found and returns the sub-tree root.
        Private recursive operation called only by remove.
        Use: node, value = self._remove_aux(node, key)
        -------------------------------------------------------
        Parameters:
            node - a bst node to search for key (_BST_Node)
            key - data to search for (?)
        Returns:
            node - the current node or its replacement (_BST_Node)
            value - value in node containing key, None otherwise.
        -------------------------------------------------------
        """
        if node is None:
            # Base Case: the key is not in the tree.
            value = None
        elif key < node._value:
            # Search the left subtree.
            node._left, value = self._remove_aux(node._left, key)
        elif key > node._value:
            # Search the right subtree.
            node._right, value = self._remove_aux(node._right, key)
        else:
            # Value has been found.
            value = node._value
            self._count -= 1
            # Replace this node with another node.
            if node._left is None and node._right is None:
                # node has no children.
                node = None

            elif node._left is None:
                # node has no left child.
                node = node._right

            elif node._right is None:
                # node has no right child.
                node = node._left

            else:
                # Node has two children
                repl_node = self._delete_node_left(node)
                repl_value = repl_node._value
                
                node._value = repl_value
                repl_node = None

        if node is not None and value is not None:
            # If the value was found, update the ancestor heights.
            node._update_height()
        return node, value

    def _delete_node_left(self, parent):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            parent - node to search for largest value (_BST_Node)
        Returns:
            repl_node - the node that replaces the deleted node. This node 
                is the node with the maximum value in the deleted node's left
                subtree (_BST_Node)
        -------------------------------------------------------
        """

        return self._delete_node_left_aux(parent._left)
    
    def _delete_node_left_aux(self, node):
        """
        -------------------------------------------------------
        Finds a replacement node for a node to be removed from the tree.
        Private operation called only by _remove_aux.
        Use: repl_node = self._delete_node_left(node, node._right)
        -------------------------------------------------------
        Parameters:
            node - a node (_BST_Node)
        Returns:
            node - the node to the right of the starting node (_BST_Node)
        -------------------------------------------------------
        """
        if node._right is not None:
            node = self._delete_node_left_aux(node._right)
        
        return node

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the bst contains key.
        Use: b = key in bst
        -------------------------------------------------------
        Parameters:
            key - a comparable data element (?)
        Returns:
            True if the bst contains key, False otherwise.
        -------------------------------------------------------
        """
        node = self._root
        contains = False

        while node is not None:
            if node._value > key:
                node = node._left
            elif node._value < key:
                node = node._right
            elif node._value == key:
                contains = True
                node = None
                
        return contains


    def height(self):
        """
        -------------------------------------------------------
        Returns the maximum height of a BST, i.e. the length of the
        largest path from root to a leaf node in the tree.
        Use: h = bst.height()
        -------------------------------------------------------
        Returns:
            maximum height of bst (int)
        -------------------------------------------------------
        """

        return self._root._height


    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two BSTs are identical.
        Use: b = bst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another bst (BST)
        Returns:
            identical - True if this bst contains the same values
            in the same order as other, otherwise returns False (boolean)
        -------------------------------------------------------
        """
        identical = True
        a = self.levelorder()
        b = other.levelorder()
        
        if a != b:
            identical = False

        return identical

    def parent(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node of a key node in a bst.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found. (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        current = self._root
        prev = None
        value = None

        while current is not None and value is None:
            if current._value > key:
                #goes left if current > key
                prev = current
                current = current._left
            elif current._value < key:
                #goes right if current < key
                prev = current
                current = current._right
            elif current._value == key:
                #if the key is found, the previous value is returned
                value = deepcopy(prev._value)
        return value


    def parent_r(self, key):
        """
        ---------------------------------------------------------
        Returns the value of the parent node in a bst given a key.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot locate a parent in an empty BST"

        current = self._root
        value = None
        
        if self._root is not None:
            value = self._parent_r_aux(key, current, None)
            
        return value
    
    def _parent_r_aux(self, key, current, prev):
        """
        Recursive aux method for parent_r.
        ---------------------------------------------------------
        Parameters:
            key - a key value (?)
            current - the current node (_BST_Node)
            prev - the previous node (_BST_Node)
        Returns:
            value - a copy of the value in a node that is the parent of the
            key node, None if the key is not found.
        """
        value = None 
        
        if current is not None and current._value > key:
            #goes left if current > key
            value = self._parent_r_aux(key, current._left, current)
        elif current is not None and current._value < key:
            #goes right if current < key
            value = self._parent_r_aux(key, current._right, current)
        elif current is not None and current._value == key:
            #if the key is found, the previous value is returned
            value = deepcopy(prev._value)
        
        return value

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in BST. (Iterative algorithm)
        Use: value = bst.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"

        node = self._root
        
        while node._right != None:
            node = node._right
        
        return node._value


    def max_r(self):
        """
        ---------------------------------------------------------
        Returns the largest value in a bst. (Recursive algorithm)
        Use: value = bst.max_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find maximum of an empty BST"


        value = self._max_r_aux(self._root)
        
        return value
    
    def _max_r_aux(self, node):
        """
        Aux method for min_r.
        ---------------------------------------------------------
        Returns:
            value - a copy of the max value in the tree (?)
        """
        if node._right != None:
            #traverses the right tree
            value = self._max_r_aux(node._right)
        else:
            value = node._value
        
        return value


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in BST. (Iterative algorithm)
        Use: value = bst.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        -------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        node = self._root
        
        while node._left != None:
            node = node._left
        
        return node._value

    def min_r(self):
        """
        ---------------------------------------------------------
        Returns the minimum value in a bst. (Recursive algorithm)
        Use: value = bst.min_r()
        ---------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the BST (?)
        ---------------------------------------------------------
        """
        assert self._root is not None, "Cannot find minimum of an empty BST"

        value = self._min_r_aux(self._root)
        
        return value
    
    def _min_r_aux(self, node):
        """
        Aux method for min_r.
        """
        if node._left != None:
            value = self._min_r_aux(node._left)
        else:
            value = node._value
        
        return value


    def leaf_count(self):
        """
        ---------------------------------------------------------
        Returns the number of leaves (nodes with no children) in bst.
        Use: count = bst.leaf_count()
        ---------------------------------------------------------
        Returns:
            count - number of nodes with no children in bst (int)
        ---------------------------------------------------------
        """
        count = 0
        
        if self._root is not None:
            count += self._leaf_count_aux(self._root)
        
        return count
    
    def _leaf_count_aux(self, node):
        """
        Recursive aux method for leaf_count.
        ---------------------------------------------------------
        Parameters:
            node - a BST node
        Returns:
            count - number of nodes with no children in the node's branch (int)

        """
        count = 0
        
        if node._left is None and node._right is None:
            #node is a leaf, add 1 to count
            count += 1
        else:
            if node._left is not None:
                #if it exists, checks the left node for children
                count += self._leaf_count_aux(node._left)
            if node._right is not None:
                #if it exists, checks the right node for children
                count += self._leaf_count_aux(node._right)
        
        return count
        
    def two_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.two_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with two children in bst (int)
        ----------------------------------------------------------
        """
        count = 0 
        
        if self._root is not None:
            count += self._two_child_count_aux(self._root)
            
        return count

    def _two_child_count_aux(self, node):
        """
        Recursive aux method for two_child_count.
        ---------------------------------------------------------
        Parameters:
            node - a BST node
        Returns:
            count - number of nodes with two children in the node's branch (int)

        """
        count = 0
        
        if node._left is not None or node._right is not None:
            if node._left is not None and node._right is not None:
                #if node has two children, adds 1 to count and executes the aux on both children
                count += 1 + self._two_child_count_aux(node._left) + self._two_child_count_aux(node._right)
            elif node._left is not None:
                #if node only has a left child, executes aux with left
                count += self._two_child_count_aux(node._left)
            elif node._right is not None:
                #if node only has a right child, executes aux with right
                count += self._two_child_count_aux(node._right)

        return count

    def one_child_count(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: count = bst.one_child_count()
        -------------------------------------------------------
        Returns:
            count - number of nodes with one child in bst (int)
        ----------------------------------------------------------
        """
        count = 0
        
        if self._root is not None:
            count += self._one_child_count_aux(self._root)
        
        return count

    def _one_child_count_aux(self, node):
        """
        Recursive aux method for one_child_count.
        ---------------------------------------------------------
        Parameters:
            node - a BST node
        Returns:
            count - number of nodes with one children in the node's branch (int)

        """
        count = 0
        
        if node._left is not None or node._right is not None:
            if node._left is not None and node._right is not None:
                count += self._one_child_count_aux(node._left) + self._one_child_count_aux(node._right)
            elif node._left is not None:
                count += 1 + self._one_child_count_aux(node._left)
            elif node._right is not None:
                count += 1 + self._one_child_count_aux(node._right)
                
        return count

    def node_counts(self):
        """
        ---------------------------------------------------------
        Returns the number of the three types of nodes in a BST.
        Use: zero, one, two = bst.node_counts()
        -------------------------------------------------------
        Returns:
            zero - number of nodes with zero children (int)
            one - number of nodes with one child (int)
            two - number of nodes with two children (int)
        ----------------------------------------------------------
        """
        #this method utilizes the three count assist methods to avoid calling higher order methods
        zero = 0
        one = 0
        two = 0
        
        if self._root is not None:
            zero = self._leaf_count_aux(self._root)
            one = self._one_child_count_aux(self._root)
            two = self._two_child_count_aux(self._root)

        return zero, one, two
        
    def total_depth(self):
        """
        ---------------------------------------------------------
        Returns the total depth of a bst.
        ---------------------------------------------------------
        Returns:
            the total depth count - i.e. the sum of all the node depths
            in the tree (int)
        ---------------------------------------------------------
        """

        # your code here


    def mirror(self):
        """
        ---------------------------------------------------------
        Creates a mirror version of a BST. All nodes are swapped with nodes on
        the other side the tree. Nodes may take the place of an empty spot.
        The resulting tree is a mirror image of the original tree. (Note that
        the mirrored tree is not a BST.) The original BST is unchanged.
        Use: tree = bst.mirror()
        ---------------------------------------------------------
        Returns:
            tree - a mirror version of subtree of node.
        ---------------------------------------------------------
        """

        # your code here

    def _node_height(self, node):
        """
        ---------------------------------------------------------
        Helper function to determine the height of node - handles empty node.
        Private operation called only by _is_valid_aux.
        Use: h = self._node_height(node)
        ---------------------------------------------------------
        Parameters:
            node - the node to get the height of (_BST_Node)
        Returns:
            height - 0 if node is None, node._height otherwise (int)
        ---------------------------------------------------------
        """
        if node is None:
            height = 0
        else:
            height = node._height
        return height

    def retrieve_r(self, key):
        """
        -------------------------------------------------------
        Retrieves a _value in a BST. (Recursive)
        Use: v = bst.retrieve(key)
        -------------------------------------------------------
        Parameters:
            key - data to search for (?)
        Returns:
            value - If bst contains key, returns value, else returns None.
        -------------------------------------------------------
        """

        # your code here


    def average_depth(self):
        """
        ---------------------------------------------------------
        Returns the average depth of a bst.
        ---------------------------------------------------------
        Returns:
            avg-depth - total depth count divided by the number of nodes
                in the tree (int)
        ---------------------------------------------------------
        """

        # your code here

    def is_balanced(self):
        """
        ---------------------------------------------------------
        Returns whether a bst is balanced, i.e. the difference in
        height between all the bst's node's left and right subtrees is <= 1.
        Use: b = bst.is_balanced()
        ---------------------------------------------------------
        Returns:
            balanced - True if the bst is balanced, False otherwise (boolean)
        ---------------------------------------------------------
        """
        balanced = False
        
        if self._root is None:
            balanced = True
        elif self._root._left is None and self._root._right is None:
            balanced = True
        elif self._root._left is None or self._root._right is None:
            #catches None errors for the following elif
            balanced = False
        elif (self._root._left._height - self._root._right._height) <= 1:
            balanced = True
    
        return balanced
    
    def is_valid(self):
        """
        ---------------------------------------------------------
        Determines if a tree is a valid BST, i.e. the values in all left nodes
        are smaller than their parent, and the values in all right nodes are
        larger than their parent, and height of any node is 1 + max height of
        its children.
        Use: b = bst.is_valid()
        ---------------------------------------------------------
        Returns:
            valid - True if tree is a BST, False otherwise (boolean)
        ---------------------------------------------------------
        """
        valid = True
        
        if self._root is not None:
            valid = self._is_valid_aux(self._root)
        
        return valid
    
    def _is_valid_aux(self, node):
        """
        Recursive aux method to is_valid.
        ---------------------------------------------------------
        Parameters:
            node - a node from a tree
        Returns:
            valid - True if tree is a BST, False otherwise
        """
        valid = True
        
        if node is not None:
            #left check
            if node._left is not None:
                left = self._is_valid_aux(node._left)
            else:
                left = True
                
            #right check
            if node._right is not None:
                right = self._is_valid_aux(node._right)
            else:
                right = True
                
            #confirms that both returned True
            if left != True or right != True:
                valid = False
        
        #if the node is None, no issues were found in that branch, and True is returned
            
        return valid

    def update(self, value, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Iterative algorithm.)
        --------------------------------------------------------- -
        """

        # your code here


    def update_r(self, key, update):
        """
        ---------------------------------------------------------
        Updates a value in a bst by applying a function to it.
        Use: bst.update(value, func)
        ---------------------------------------------------------
        Parameters:
            value - a comparable part of a data element (?)
            update - an update function compatible with value (function)
        Returns:
            updated - True if value is in bst and is updated, False if
            value is not in bst, but adds value to bst in that case.
            (Recursive algorithm.)
        --------------------------------------------------------- -
        """

        # your code here


    def inorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in inorder order.
        Left, node, right.
        Use: a = bst.inorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in inorder (list of ?)
        -------------------------------------------------------
        """
        a = []

        if self._root is not None:
            a.extend(self._inorder_aux(self._root))
            
            """this method makes use of the extend function.
            This function individually appends each item in 
            a given list to the target list, making it very 
            useful for recursion."""

        return a

    def _inorder_aux(self, node):
        """
        Recursive aux method for inorder. Left, node, right.
        -------------------------------------------------------
        Parameters:
            node - a BST node
        Returns:
            a - a list of inordered node values (list of ?)
        """
        a = []
        
        if node._left is not None:
            #calls the aux on any existing left node...
            a.extend(self._inorder_aux(node._left))
            #...which extends a
            
        a.append(node._value)
        #a is then appended with the node's value
        
        if node._right is not None:
            #the aux is then called for any existing right node...
            a.extend(self._inorder_aux(node._right))
            #...but for the sort to work it is called last
        return a
        
    def preorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in preorder order.
        Node, left, right.
        Use: a = bst.preorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in preorder (list of ?)
        -------------------------------------------------------
        """
        a = []

        if self._root is not None:
            a.extend(self._preorder_aux(self._root))
        
        return a

    def _preorder_aux(self, node):
        """
        Recursive aux method for preorder. Node, left, right.
        -------------------------------------------------------
        Parameters:
            node - a BST node
        Returns:
            a - a list of preordered node values (list of ?)
        """
        a = []
        
        a.append(node._value)
        #appends the node's value first
        
        if node._left is not None:
            #calls the aux for the left node, if it exists, second
            a.extend(self._preorder_aux(node._left))
        
        if node._right is not None:
            #calls the aux for the right node, if it exists, last
            a.extend(self._preorder_aux(node._right))
            
        return a

    def postorder(self):
        """
        -------------------------------------------------------
        Generates a list of the contents of the tree in postorder order.
        Left, right, node
        Use: a = bst.postorder()
        -------------------------------------------------------
        Returns:
            a - copy of the contents of the tree in postorder (list of ?)
        -------------------------------------------------------
        """
        a = []

        if self._root is not None:
            a.extend(self._postorder_aux(self._root))
        
        return a

    def _postorder_aux(self, node):
        """
        Recursive aux method for postorder. Left, right, node
        -------------------------------------------------------
        Parameters:
            node - a BST node
        Returns:
            a - a list of postordered node values (list of ?)
        """
        a = []
        
        if node._left is not None:
            #calls the aux for the left node, if it exists, first
            a.extend(self._postorder_aux(node._left))
        
        if node._right is not None:
            #calls the aux for the right node, if it exists, second
            a.extend(self._postorder_aux(node._right))
            
        a.append(node._value)
        #appends the node last
        
        return a

    def levelorder(self):
        """
        -------------------------------------------------------
        Copies the contents of the tree in levelorder order to a list.
        Returns a list of the nodes in order of level from the top.
        Use: values = bst.levelorder()
        -------------------------------------------------------
        Returns:
            values - a list containing the values of bst in levelorder.
            (list of ?)
        -------------------------------------------------------
        """
        a = []
        
        if self._root is not None:
            queue = Queue()
            queue.insert(self._root._value)
            
            a, _ = self._levelorder_aux(self._root, queue)
            
        return a

    def _levelorder_aux(self, node, queue):
        """
        Recursive aux method for postorder. Left, right, node
        -------------------------------------------------------
        Algorithm:
            If the root node is not None:
            Create a queue for nodes. Add the root node to this queue.
            As long as the queue is not empty:
                Remove the front node from the queue.
                Extract / print the data in the extracted node
                If not None, add node's left child to the rear of the queue
                If not None, add node's right child to the rear of the queue
        -------------------------------------------------------
        Parameters:
            node - a BST node
            queue - a queue of nodes (queue of _BST_nodes)
        Returns:
            a - a list of postordered node values (list of ?)
            queue
        
        """
        a = []
        
        if queue.is_empty() == False:
            a.append(queue.remove())
            #appends a with the first item in the queue
            
            if node._left is not None:
                #adds the left node to the queue, if it exists
                queue.insert(node._left._value)
            if node._right is not None:
                #adds the right node to the queue, if it exists
                queue.insert(node._right._value)
            
            if node._left is not None:
                #if it exists, calls the aux with the left node, updating the queue and providing temp
                temp, queue = self._levelorder_aux(node._left, queue)
                #extends a using the provided temp
                a.extend(temp)
            if node._right is not None:
                #if it exists, calls the aux with the right node, updating the queue and providing temp
                temp, queue = self._levelorder_aux(node._right, queue)
                a.extend(temp)
                
        return a, queue

    def count(self):
        """
        ---------------------------------------------------------
        Returns the number of nodes in a BST.
        Use: number = bst.count()
        -------------------------------------------------------
        Returns:
            number - count of nodes in tree (int)
        ----------------------------------------------------------
        """

        # your code here


    def __iter__(self):
        """
        -------------------------------------------------------
        Generates a Python iterator. Iterates through a BST node
        in level order.
        Use: for v in bst:
        -------------------------------------------------------
        Returns:
            yields
            value - the values in the BST node and its children (?)
        -------------------------------------------------------
        """
        if self._root is not None:
            # Put the nodes for one level into a queue.
            queue = []
            queue.append(self._root)

            while len(queue) > 0:
                # Add a copy of the data to the sublist
                node = queue.pop(0)
                yield node._value

                if node._left is not None:
                    queue.append(node._left)
                if node._right is not None:
                    queue.append(node._right)