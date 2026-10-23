# [🌳 The Great Binary Tree Mirror Flip! 🪞](https://leetcode.com/problems/invert-binary-tree/?envType=study-plan-v2&envId=top-interview-150)

Imagine a magical tree standing in front of a mirror! ✨ Every branch appears on the opposite side, and every node's left and right children exchange places. Your mission is to recreate this mirrored tree while preserving every node and its value. 🔄

### 🎯 Your Challenge

Given the **`root`** of a binary tree, **invert the entire tree** by swapping the left and right children of every node, including all its subtrees. Return the root of the resulting inverted tree. The tree's structure should become a mirror image of the original, while all node values remain unchanged.

#### 🧪 Examples

- **Example 1: 🌲 Mirroring a Complete Tree**

    ![](https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg)
    - **Input: `root = [4,2,7,1,3,6,9]`**
    - **Output: `[4,7,2,9,6,3,1]`**
    - **Explanation:** Node **`4`** swaps children **`2`** and **`7`**. Node **`2`** swaps children **`1`** and **`3`**, while node **`7`** swaps children **`6`** and **`9`**. The same swapping process applies throughout the tree, producing its mirror image.

- **Example 2: 🌿 Flipping a Simple Tree**
    ![](https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg)
    - **Input: `root = [2,1,3]`**
    - **Output: `[2,3,1]`**
    - **Explanation:** The root **`2`** swaps its left child **`1`** with its right child **`3`**. Since both children are leaf nodes, no further swaps are needed.

- **Example 3: 🍃 The Empty Tree**
    - **Input: `root = []`**
    - **Output: `[]`**
    - **Explanation:** The tree contains no nodes, so there is nothing to invert. The result remains an empty tree.

#### 📌 Constraints
- The number of nodes in the tree is between **`0`** and **`100`**, inclusive.
- Each node's value satisfies **`-100 <= Node.val <= 100`**.

**💡 Remember:** Inverting a binary tree changes its structure, not its values. Every node's left and right subtrees must switch sides to form the complete mirror image! 🪞🌳

---

### 🌳 Invert Binary Tree — Solution Approaches

A binary tree is inverted by swapping the left and right children of every node. The same process is applied throughout the tree until every subtree is mirrored. 🪞

All three approaches take **O(n) time**, since every node must be visited at least once. They differ in how they traverse the tree: recursion, an explicit stack, or a queue.

- #### 🔄 Recursive DFS

    - **💡 Intuition**
    Think of every node as a tiny mirror 🪞. Swap its left and right children, then recursively invert both resulting subtrees. The process naturally stops when it reaches a **`None`** node.

    - **🪜 Steps**
        1. 🌱 If the root is **`None`**, return **`None`**.
        2. 🪞 Swap the root's left and right children.
        3. 🔁 Recursively invert the left subtree.
        4. 🔁 Recursively invert the right subtree.
        5. ✅ Return the original root of the inverted tree.

    - **📝 Pseudocode**
        ```text
        INVERT(root):
            IF root is None:
                RETURN None

            SWAP root.left AND root.right
            INVERT(root.left)
            INVERT(root.right)

            RETURN root
        ```

    - **⏱️ Complexity**
        - **Time:** **`O(n)`** — each node is processed once.
        - **Auxiliary Space:** **`O(h)`** — recursive call stack, where `h` is the tree height; worst case **`O(n)`**.

        **🌟 Best for:** A clean, concise, and easy-to-understand solution.


- #### 📚 Iterative DFS — Stack

    - **💡 Intuition**
    Use an explicit stack to perform depth-first traversal instead of relying on recursive calls. Pop a node, swap its children, and push its non-null children onto the stack for later processing.

    - **🪜 Steps**
        1. 🌱 Return **`None`** if the tree is empty.
        2. 📚 Initialize a stack containing the root.
        3. 🔍 Pop a node from the stack.
        4. 🪞 Swap its left and right children.
        5. ⬇️ Push its non-null children onto the stack.
        6. 🔁 Repeat until the stack is empty.
        7. ✅ Return the original root.

    - **📝 Pseudocode**
        ```text
        INVERT(root):
            IF root is None:
                RETURN None

            stack = [root]

            WHILE stack is not empty:
                node = stack.pop()
                SWAP node.left AND node.right

                IF node.left exists:
                    PUSH node.left onto stack

                IF node.right exists:
                    PUSH node.right onto stack

            RETURN root
        ```

    - **⏱️ Complexity**
        - **Time:** **`O(n)`** — each node is visited once.
        - **Auxiliary Space:** **`O(h)`** for a balanced tree's DFS stack; worst case **`O(n)`**.

        **🌟 Best for:** Avoiding recursion while retaining depth-first traversal.

- #### 🚦 Iterative BFS — Queue

    - **💡 Intuition**
    Invert the tree level by level. A queue processes nodes in first-in, first-out order: remove a node, swap its children, and enqueue its non-null children.

    - **🪜 Steps**
        1. 🌱 Return **`None`** if the tree is empty.
        2. 🚦 Initialize a queue with the root.
        3. 🔍 Remove the front node from the queue.
        4. 🪞 Swap its left and right children.
        5. ➕ Enqueue its non-null children.
        6. 🔁 Repeat until the queue is empty.
        7. ✅ Return the original root.

    - **📝 Pseudocode**
        ```text
        INVERT(root):
            IF root is None:
                RETURN None

            queue = [root]

            WHILE queue is not empty:
                node = REMOVE_FRONT(queue)
                SWAP node.left AND node.right

                IF node.left exists:
                    ENQUEUE node.left

                IF node.right exists:
                    ENQUEUE node.right

            RETURN root
        ```

    - **⏱️ Complexity**
        - **Time:** **`O(n)`** — each node is visited once.
        - **Auxiliary Space:** **`O(w)`** — queue space depends on the maximum width `w` of the tree; worst case **`O(n)`**.

        **🌟 Best for:** Level-order traversal and an intuitive, non-recursive solution.


### 🏆 Quick Comparison

| Feature | 🔄 Recursive DFS | 📚 Iterative DFS | 🚦 Iterative BFS |
|---|---|---|---|
| Traversal | Depth-first | Depth-first | Level-order |
| Data structure | Call stack | Explicit stack | Queue |
| Time | `O(n)` | `O(n)` | `O(n)` |
| Auxiliary space | `O(h)` | `O(h)` typical for balanced trees | `O(w)` |
| Recursion used | Yes | No | No |

### 🎯 Final Takeaway

All three approaches are optimal in time complexity. Every node must be visited to swap its children, giving a lower bound of **O(n)**.

- 🥇 **Recursive DFS:** Simplest and most concise.
- 📚 **Iterative DFS:** Useful when you want to avoid recursive calls.
- 🚦 **Iterative BFS:** Ideal for demonstrating level-order traversal.

**Key insight:** Invert a binary tree by swapping the children of every node exactly once. The traversal strategy changes, but the core operation stays the same! 🪞🌳

---
