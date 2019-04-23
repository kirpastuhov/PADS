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
            public bool Exists { get; set; }

            public Node(int key, int left, int right)
            {
                Key = key;
                Left = left;
                Right = right;
                Exists = true;
            }
        }
        private Node[] nodes;
        private int root;
        private int capacity;


        List<int> childs;
        List<int> newChilds;

        public int Size { get; private set; }

        public BinaryTree(int capacity)
        {
            nodes = new Node[capacity];
            childs = new List<int>(0);
            newChilds = new List<int>(0);
        }
        public void Add(int key, int left, int right)
        {
            nodes[capacity] = new Node(key, left, right);
            if (nodes[capacity].Left == root || nodes[capacity].Right == root)
                root = capacity;
            capacity++;
            Size++;
        }

        public int GetSize(int root)
        {
            childs.Clear();
            newChilds.Clear();
            newChilds.Add(root);
            int count = 0;
            while (newChilds.Count > 0)
            {
                count += newChilds.Count;
                List<int> temp = childs;
                childs = newChilds;
                newChilds = temp;
                newChilds.Clear();
                for (int i = 0; i < childs.Count; i++)
                {
                    if (nodes[childs[i]].Left != -1 && nodes[nodes[childs[i]].Left].Exists)
                        newChilds.Add(nodes[childs[i]].Left);
                    if (nodes[childs[i]].Right != -1 && nodes[nodes[childs[i]].Right].Exists)
                        newChilds.Add(nodes[childs[i]].Right);
                }
            }
            return count;
        }
        public void Delete(int key)
        {
            int node = Find(key);
            if (node != -1)
            {
                Size -= GetSize(node);
                nodes[node].Exists = false;
            }
        }
        public int Find(int key)
        {
            int node = root;
            while (node != -1 && nodes[node].Key != key && nodes[node].Exists)
            {
                if (key <= nodes[node].Key)
                    node = nodes[node].Left;
                else
                    node = nodes[node].Right;
            }
            if (node != -1 && (nodes[node].Key != key || !nodes[node].Exists))
                node = -1;
            return node;
        }
    }
    public class week6_lab4
    {
        public static void Main(string[] args)
        {
            using (StreamReader streamReader = new StreamReader("input.txt"))
            using (StreamWriter streamWriter = new StreamWriter("output.txt"))
            {
                int n = int.Parse(streamReader.ReadLine());
                BinaryTree tree = new BinaryTree(n);
                string[] str;
                for (int i = 0; i < n; i++)
                {
                    str = streamReader.ReadLine().Split(' ');
                    tree.Add(int.Parse(str[0]), int.Parse(str[1]) - 1, int.Parse(str[2]) - 1);
                }
                int m = int.Parse(streamReader.ReadLine());
                str = streamReader.ReadLine().Split(' ');
                for (int i = 0; i < m; i++)
                {
                    tree.Delete(int.Parse(str[i]));
                    streamWriter.WriteLine(tree.Size);
                }
            }
        }
    }
}
