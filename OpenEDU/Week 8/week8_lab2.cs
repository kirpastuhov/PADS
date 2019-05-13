using System;
using System.IO;
using System.Collections.Generic;
using System.Globalization;

namespace Openedu.Week8
{
    public class HashTable
    {
        Dictionary<string, LinkedListNode<string>> table;
        private LinkedList<string> history;

        public HashTable()
        {
            table = new Dictionary<string, LinkedListNode<string>>();
            history = new LinkedList<string>();
        }

        public void Insert(string key, string value)
        {
            if (table.ContainsKey(key))
            {
                table[key].Value = value;
            }
            else
            {
                history.AddLast(value);
                table.Add(key, history.Last);
            }
        }
        public bool TryGetValue(string key, out string value)
        {
            if (table.TryGetValue(key, out LinkedListNode<string> node))
            {
                value = node.Value;
                return true;
            }
            value = null;
            return false;
        }
        public bool TryGetNext(string key, out string value)
        {
            if (table.TryGetValue(key, out LinkedListNode<string> node) && node.Next != null)
            {
                value = table[key].Next.Value;
                return true;
            }
            value = null;
            return false;
        }
        public bool TryGetPrevious(string key, out string value)
        {
            if (table.TryGetValue(key, out LinkedListNode<string> node) && node.Previous != null)
            {
                value = table[key].Previous.Value;
                return true;
            }
            value = null;
            return false;
        }
        public void Remove(string key)
        {
            if (table.TryGetValue(key, out LinkedListNode<string> node))
            {
                table.Remove(key);
                history.Remove(node);
            }
        }
    }
    public class Task2
    {
        public static void Main(string[] args)
        {
            using (StreamReader streamReader = new StreamReader("input.txt"))
            using (StreamWriter streamWriter = new StreamWriter("output.txt"))
            {
                int n = int.Parse(streamReader.ReadLine());
                HashTable hashTable = new HashTable();
                for (int i = 0; i < n; i++)
                {
                    string[] str = streamReader.ReadLine().Split(' ');
                    switch(str[0])
                    {
                        case "get":
                            streamWriter.WriteLine(hashTable.TryGetValue(str[1], out string value1) ? value1 : "<none>");
                            break;
                        case "prev":
                            streamWriter.WriteLine(hashTable.TryGetPrevious(str[1], out string value2) ? value2 : "<none>");
                            break;
                        case "next":
                            streamWriter.WriteLine(hashTable.TryGetNext(str[1], out string value3) ? value3 : "<none>");
                            break;
                        case "put":
                            hashTable.Insert(str[1], str[2]);
                            break;
                        case "delete":
                            hashTable.Remove(str[1]);
                            break;
                    }
                }
            }
        }
    }
}
