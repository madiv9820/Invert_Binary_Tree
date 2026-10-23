"""
🌳 Invert a binary tree by swapping the left and right children of every node.

This module defines the Solution class for the Invert Binary Tree problem.
The inversion must preserve all node values while transforming the tree
into the mirror image of its original structure.
"""

from typing import Optional
from treenode import TreeNode
from .approaches import Recursion, IterativeDFS

class Solution:
    """🪞 Provide the solution for mirroring a binary tree."""

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 🍃 An empty tree has nothing to invert; return its root as-is.
        recursion: Recursion = Recursion()
        iterativeDFS: IterativeDFS = IterativeDFS()
        
        return iterativeDFS.invertTree(root)
