"""🌳 Define the binary tree node used to build and manipulate trees."""
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
