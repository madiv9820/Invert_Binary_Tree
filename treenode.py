"""
🌳 Define the TreeNode class for representing binary tree structures.

Each node stores an integer value and maintains references to its left
and right children, allowing nodes to be connected into a binary tree.

The class serves as a reusable building block for tree-based algorithms,
supporting operations such as traversal, inversion, depth calculation,
and structural comparison across different binary tree problems.
"""

from typing import Optional

class TreeNode:
    """🪴 Represent a node with a value and two child references."""

    def __init__(
        self,
        val     : int = 0,
        left    : Optional[TreeNode] = None,
        right   : Optional[TreeNode] = None,
    ) -> None:
        self.val    : int = val                     # 🏷️ Store the value held by this node.
        self.left   : Optional[TreeNode] = left     # 👈 Link to the left subtree, if present.
        self.right  : Optional[TreeNode] = right    # 👉 Link to the right subtree, if present.
