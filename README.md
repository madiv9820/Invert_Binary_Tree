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