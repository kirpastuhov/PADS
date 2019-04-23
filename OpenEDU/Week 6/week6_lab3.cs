using System;
using System.IO;
using System.Collections.Generic;
using System.Globalization;

namespace Openedu.Week6
{

    public class BinaryTree
    {
        private struct Node
        {
            public int Key { get; set; }
            public int Left { get; set; }
            public int Right { get; set; }

            public Node(int key, int left, int right)
            {
                Key = key;
                Left = left;
                Right = right;
            }
        }
        private Node[] nodes;
        private int root;
        private int size;

        public BinaryTree(int size)
        {
            nodes = new Node[size];
            root = 0;
            size = 0;
        }
        public void Add(int key, int left, int right)
        {
            nodes[size] = new Node(key, left, right);
            if (nodes[size].Left == root || nodes[size].Right == root)
                root = size;
            size++;
        }

        public int GetDepth()
        {
            List<int> childs = new List<int>(nodes.Length);
            List<int> newChilds = new List<int>(nodes.Length);
            newChilds.Add(root);
            int depth = 0;
            while (newChilds.Count > 0)
            {
                List<int> temp = childs;
                childs = newChilds;
                newChilds = temp;
                newChilds.Clear();
                for (int i = 0; i < childs.Count; i++)
                {
                    if (nodes[childs[i]].Left != -1)
                        newChilds.Add(nodes[childs[i]].Left);
                    if (nodes[childs[i]].Right != -1)
                        newChilds.Add(nodes[childs[i]].Right);
                }
                depth++;
            }
            return depth;
        }
    }
    public class week6_lab3
    {
        public static void Main(string[] args)
        {
            using (StreamReader streamReader = new StreamReader("input.txt"))
            using (StreamWriter streamWriter = new StreamWriter("output.txt"))
            {
                int n = int.Parse(streamReader.ReadLine());
                BinaryTree tree = new BinaryTree(n);
                for (int i = 0; i < n; i++)
                {
                    string[] str = streamReader.ReadLine().Split(' ');
                    tree.Add(int.Parse(str[0]), int.Parse(str[1]) - 1, int.Parse(str[2]) - 1);
                }
                streamWriter.WriteLine(n == 0 ? 0 : tree.GetDepth());
            }
        }
    }
}
