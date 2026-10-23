"""
🌳 Invert a binary tree using a recursive depth-first approach.

This module defines the Recursion class, which transforms a binary tree
into its mirror image by swapping the left and right children of every
node. The process recursively inverts both subtrees until all nodes
have been visited.

Time Complexity: O(n), where n is the number of nodes.
Space Complexity: O(h), where h is the height of the tree due to the
                   recursive call stack.
"""

from typing import Optional
from treenode import TreeNode

class Recursion:
    """🪞 Mirror a binary tree by recursively swapping its children."""

    @staticmethod
    def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 🍃 An empty subtree requires no changes.
        if root:
            # 🔄 Swap the left and right children to mirror this node.
            root.left, root.right = root.right, root.left

            # 👈 Recursively invert the left subtree.
            root.left = Recursion.invertTree(root.left)

            # 👉 Recursively invert the right subtree.
            root.right = Recursion.invertTree(root.right)

        # 🌳 Return the root of the inverted subtree.
        return root
