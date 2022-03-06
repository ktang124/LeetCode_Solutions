# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def insert_into_bst(root, val)
    #first case
    if(root == nil)
        return TreeNode.new(val, nil, nil)
    elsif(val < root.val)
        root.left = insert_into_bst(root.left, val)
    else
        root.right = insert_into_bst(root.right, val) 
    end
    root
end