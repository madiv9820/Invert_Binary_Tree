"""🌳 Invert a binary tree using an iterative Breadth-First Search (BFS) approach."""

from collections import deque
from typing import Optional, Deque
from treenode import TreeNode

class IterativeBFS:
    """🔄 Mirror a binary tree using a queue and level-order traversal."""

    @staticmethod
    def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert a binary tree by swapping the children of every node.

        Args:
            root: 🌱 The root node of the binary tree, or None if the tree is empty.

        Returns:
            🌳 The root of the inverted binary tree.
        """
        if root:
            # 📋 Initialize a queue with the root to begin level-order traversal.
            nodeQ: Deque[TreeNode] = deque([root])

            while nodeQ:
                # 🔍 Remove the front node to process it in BFS order.
                currentNode: TreeNode = nodeQ.popleft()

                # 🪞 Swap the left and right children to mirror the current node.
                currentNode.left, currentNode.right = (
                    currentNode.right,
                    currentNode.left,
                )

                # ⬅️ Add the left child to the queue if it exists.
                if currentNode.left:
                    nodeQ.append(currentNode.left)

                # ➡️ Add the right child to the queue if it exists.
                if currentNode.right:
                    nodeQ.append(currentNode.right)

        # ✅ Return the original root, which now represents the inverted tree.
        return root