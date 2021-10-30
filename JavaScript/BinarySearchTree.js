// Implementing Binary Search Tree in JavaScript
// Node class
class Node
{
    constructor(data)
    {
        this.data = data;
        this.left = null;
        this.right = null;
    }
}

// Binary Search tree class
class BinarySearchTree
{
	constructor()
	{
		// root of a binary search tree
		this.root = null;
	}

	// insert(data)
    insert(data)
    {
        var newNode = new Node(data);       // Creating a node and initialising with data
        if(this.root === null)              // root is null
            this.root = newNode;            // then node will be added to the tree and made root.
        else
            this.insertNode(this.root, newNode);    // find the correct position in the tree and add the node
    }

    insertNode(node, newNode)               // Method to insert a node in a tree, it moves over the tree to find the location to insert a node with a given data
    {
        // if the data is less than the node
        // data move left of the tree
        if(newNode.data < node.data)
        {
    
            if(node.left === null)          // if left is null
                node.left = newNode;        // insert node here
            else
                this.insertNode(node.left, newNode);    // if left is not null recur until null is found
        }

        // if the data is more than the node
        // data move right of the tree
        else
        {
            
            if(node.right === null)         // if right is null
                node.right = newNode;       // insert node here
            else
                this.insertNode(node.right,newNode);    // if right is not null recur until null is found
        }
    }

	// remove(data)
    remove(data)            // removeNode with a given data
    {
        this.root = this.removeNode(this.root, data);      // root is re-initialized with root of a modified tree.
    }

    removeNode(node, key)   // Method to remove node with a given data, it recur over the tree to find the data and removes it.
    {
        if(node === null)   // if the root is null then tree is empty
            return null;
        else if(key < node.data)    // if data to be delete is less than current node data
        {
            node.left = this.removeNode(node.left, key);   // then move to left subtree
            return node;
        }
        else if(key > node.data)    // if data to be delete is greater than current node data
        {
            node.right = this.removeNode(node.right, key);  // then move to right subtree
            return node;
        }
        else                        // if data is similar to the current node data, // then delete this node
        {
            // deleting node with no children
            if(node.left === null && node.right === null)
            {
                node = null;
                return node;
            }

            // deleting node with one children
            if(node.left === null)
            {
                node = node.right;
                return node;
            }
            
            else if(node.right === null)
            {
                node = node.left;
                return node;
            }

            // Deleting node with two children
            var aux = this.findMinNode(node.right);             // minimum node of the right subtree is stored in aux
            node.data = aux.data;

            node.right = this.removeNode(node.right, aux.data);
            return node;
        }

    }

	// findMinNode()
    findMinNode(node)           // finds the minimum node in tree searching starts from given node
    {

        if(node.left === null)          // if left of a node is null
            return node;                // then it must be minimum node, so returns the node.
        else
            return this.findMinNode(node.left);
    }

	// getRootNode()
    getRootNode()
    {
        return this.root;      // returns root of the tree
    }

	// inorder(node)
    
    inorder(node, list)
    {
        if(node !== null)
        {
            this.inorder(node.left, list);    // Performs inorder traversal of a left subtree
            list.push(node.data);             // push the current node data into list
            this.inorder(node.right, list);   // Performs inorder traversal of a right subtree
        }
    }

	// preorder(node)
    preorder(node)
    {
        if(node !== null)
        {
            list.push(node.data);                 // push the current node data into list
            this.preorder(node.left, list);       // Performs preorder traversal of a left subtree
            this.preorder(node.right, list);      // Performs preorder traversal of a right subtree
        }
    }
		
	// postorder(node)
    postorder(node, list)
    {
        if(node !== null)
        {
            this.postorder(node.left, list);      // Performs postorder traversal of a left subtree
            this.postorder(node.right, list);     // Performs postorder traversal of a right subtree
            list.push(node.data);               // push the current node data into list
        }
    }

	// search(node, data)
    
    search(node, data)                      // search for a node with given data
    {
    
        if(node === null)                   // if tree is empty return null
            return null;

        else if(data < node.data)           // if data is less than node's data
            return this.search(node.left, data);    // move left

        else if(data > node.data)           // if data is greater than node's data
            return this.search(node.right, data);   // move right

        else                                // if data is equal to the node data
            return node;                    // return node
    }

}

// create an object for the BinarySearchTree
var BST = new BinarySearchTree();
var list = [];      // initializing the list

// Inserting nodes to the BinarySearchTree
BST.insert(15);
BST.insert(25);
BST.insert(10);
BST.insert(7);
BST.insert(22);
BST.insert(17);
BST.insert(13);
BST.insert(5);
BST.insert(9);
BST.insert(27);
						
//		 15
//		 / \
//	    10 25
//	   / \ / \
//	  7 13 22 27
//   /\ /
//  5 9 17

var root = BST.getRootNode();       // getting root of BST

BST.inorder(root, list);
console.log("\nInorder of BST: ",list);   // prints [5, 7, 9, 10, 13, 15, 17, 22, 25, 27]
list = [];                 // re-initializing list to empty list

// Removing node with no children
console.log("\nRemove leaf node - (node with value '5')");
BST.remove(5);                      // Remove node with the value '5'
			
//		 15
//		 / \
//	 10 25
//	 / \ / \
//	 7 13 22 27
//	 \ /
//	 9 17


var root = BST.getRootNode();       // getting the root of BST

BST.inorder(root, list);
console.log("Inorder of BST: ",list);   // prints [7, 9, 10, 13, 15, 17, 22, 25, 27]
list = [];			                // re-initializing list to empty list

// Removing node with one child
console.log("\nRemove node with one child - (node with value '7')")
BST.remove(7);                      // Remove node with value '7'
			
//		 15
//		 / \
//	    10 25
//	   / \ / \
//	  9 13 22 27
//		  /
//		 17


var root = BST.getRootNode();           // get the root node and store it in "root" variable

BST.inorder(root, list);
console.log("Inorder of BST: ",list);   // prints [9, 10, 13, 15, 17, 22, 25, 27]
list = [];			                // re-initializing list to empty list
			
// Removing node with two children
console.log("\nRemove node with two children - (node with value '15')")
BST.remove(15);                     // Remove node with value '15'

//		 17
//		 / \
//	 10 25
//	 / \ / \
//	 9 13 22 27

var root = BST.getRootNode();      // get the root node and store in "root" variable

// inorder traversal
BST.inorder(root, list);
console.log("Inorder traversal of BST: ", list);        // prints [9 10 13 17 22 25 27]
list = [];              // re-initializing list to empty list

// preorder traversal
BST.preorder(root, list);
console.log("Preorder traversal of BST: ", list);
list = [];              // re-initializing list to empty list

//postorder traversal
BST.postorder(root, list);
console.log("Postorder traversal of BST: ", list);
