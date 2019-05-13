using System;
using System.IO;
using System.Collections.Generic;
using System.Globalization;

namespace Openedu.Week8
{
    public class HashTable
    {
        private int tableSize;
        private LinkedList<long>[] table;

        public HashTable(int size = 1500)
        {
            tableSize = size;
            table = new LinkedList<long>[size];
            for (int i = 0; i < size; i++)
                table[i] = new LinkedList<long>();
        }

        public void Insert(long key)
        {
            int hash = GetHash(key);
            if (!table[hash].Contains(key))
                table[hash].AddLast(key);
        }
        public void Remove(long key)
        {
            int hash = GetHash(key);
            table[hash].Remove(key);
        }

        public bool ContainsKey(long key)
        {
            int hash = GetHash(key);
            return table[hash].Contains(key);
        }

        private int GetHash(long key)
        {
            return Math.Abs((((int)key).GetHashCode() + (key >> 32).GetHashCode()) % tableSize);
        }
    }
    public class Task1
    {
        public static void Main(string[] args)
        {
            using (StreamReader streamReader = new StreamReader("input.txt"))
            using (StreamWriter streamWriter = new StreamWriter("output.txt"))
            {
                int n = int.Parse(streamReader.ReadLine());
                HashTable hashTable = new HashTable(n);
                for (int i = 0; i < n; i++)
                {
                    string[] str = streamReader.ReadLine().Split(' ');
                    switch(str[0][0])
                    {
                        case 'A':
                            hashTable.Insert(long.Parse(str[1]));
                            break;
                        case 'D':
                            hashTable.Remove(long.Parse(str[1]));
                            break;
                        case '?':
                            streamWriter.WriteLine(hashTable.ContainsKey(long.Parse(str[1])) ? "Y" : "N");
                            break;
                    }
                }
            }
        }
    }
}
