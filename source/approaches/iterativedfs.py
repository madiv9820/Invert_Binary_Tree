"""🌳 Invert a binary tree using an iterative Depth-First Search (DFS) approach."""

from typing import Optional, List
from treenode import TreeNode

class IterativeDFS:
    """🔄 Mirror a binary tree using a stack instead of recursion."""

    @staticmethod
    def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree by swapping the left and right children of every node.

        Args:
            root: 🌱 The root node of the binary tree, or None if the tree is empty.

        Returns:
            🌳 The root of the inverted binary tree.
        """
        if root:
            # 📚 Start DFS with the root node on the stack.
            nodeStack: List[TreeNode] = [root]

            while nodeStack:
                # 🔍 Pop the top node to process it before exploring its descendants.
                currentNode: TreeNode = nodeStack.pop()

                # 🪞 Swap the left and right children to mirror the current node.
                currentNode.left, currentNode.right = (
                    currentNode.right,
                    currentNode.left,
                )

                # ⬅️ Schedule the left child for inversion, if it exists.
                if currentNode.left:
                    nodeStack.append(currentNode.left)

                # ➡️ Schedule the right child for inversion, if it exists.
                if currentNode.right:
                    nodeStack.append(currentNode.right)

        # ✅ Return the original root, now representing the inverted tree.
        return root
