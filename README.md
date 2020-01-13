## LeetCode刷题记录

### 链表部分
**目前涉及题目**
2 19 21 
对于链表的操作，为多链表融合为一个链表，单个链表的插入操作
核心的功能为插入，插入时不要忘记因为插入导致整个链表被无法继续链接
其中插入分为头插法和尾插法，这俩个插入方法的使用具体情况具体分析
**头插法**
```python
## a 原链表中的节点的头结点 s为需要插入的节点
s.next = a.next 
a.next = a


```
**尾插法**
```python
## a 原链表中的节点的尾结点 s为需要插入的节点
a.next = s
a = s
```
#### 19题
思路： 使用连个指针进行遍历链表，其中pre指针要先与curr指针N个位置即可

### 树部分（二叉树）

#### 定义节点：

* java

  ```java
  public class TreeNode{
  	int val;
  	TreeNode left;
  	TreeNode right;
  	TreeNode(int x){ val = x; }
  }
  ```

  

* python

  ```python
  class TreeNode:
  	def __init__(sefl, x);
  		self.val = x
  		self.right = None
  		self.left = None
  ```

* 根据定义的数据结构创建一个树

  ```
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(6)
  root.left.right = TreeNode(5)
  ```

#### 二叉搜索树的查询是否有该值

```python
def search(root, x):
    if not root:
        return False
    if x == root.val:
        return True
    if x < root.val:
        search(root.left, x)
    else x > root.val:
        search(root.right, x)

```

#### 平衡二叉树

* 定义: 左右子树的高度差的绝对值≤1

* 判断是否平衡(110题)

  ```python
  def balanced(root):
  	"""
  	判断是否平衡
  	"""
  	if not root:
  		return True
      return abs(height(root.left) - height(root.right)) <=1 and balanced(root.left) and balanced(root.right)
  ```

  <img src="https://raw.githubusercontent.com/KongWiki/cloudImg/master/%E4%BA%8C%E5%8F%89%E6%A0%91.png" alt="image" style="zoom: 50%;" />
  
* 求二叉树的高度（递归方式）

  ```python
  def height(root):
  	"""
  	求二叉树的高度
  	"""
      if not root:
          return 0
      left_height = height(root.left)
      right_height = height(root.right)
      return max(left_height, right_hegith) + 1
  ```

  

  

#### 二叉树的前中后遍历

* 前序遍历

  ```python
  def pre_order(root):
  	if not root: 
  		return 
  	print(root.val)
  	pre_order(root.left)
  	pre_order(root.right)		
  ```

* 中序遍历

  ```python
  def in_order(root):
  	if not root:
  		return 
  	in_order(root.left)
  	print(root.val)
  	in_order(root.right)
  ```

  

* 后序遍历

  ```python
  def post_order(root):
      	if not root: 
              return 
          post_order(root.left)
          post_order(root.right)
          print(root.val)
  ```

n     