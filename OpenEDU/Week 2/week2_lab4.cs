using System.IO;

namespace week2_lab2
{
    internal static class Program
    {
        private static void quick_sort(int[] data, int left, int right, int k1, int k2)
        {
            while (true)
            {
                if (left > k2 || right < k1) return;
                int i = left, j = right;
                var x = data[(left + right) / 2];

                while (i <= j)
                {
                    while (data[i].CompareTo(x) < 0)
                    {
                        i++;
                    }

                    while (data[j].CompareTo(x) > 0)
                    {
                        j--;
                    }

                    if (i > j) continue;
                    var tmp = data[i];
                    data[i] = data[j];
                    data[j] = tmp;

                    i++;
                    j--;
                }

                if (left < j)
                {
                    quick_sort(data, left, j, k1, k2);
                }

                if (i < right)
                {
                    left = i;
                    continue;
                }

                break;
            }
        }


        private static void Main()
        {
            int n, k1, k2;
            int a, b, c;
            int[] data;
            using (var reader = new StreamReader("input.txt"))
            {
                var firstLine = reader.ReadLine()?.Split();
                n = int.Parse(firstLine?[0]);
                k1 = int.Parse(firstLine?[1]) - 1;
                k2 = int.Parse(firstLine?[2]) - 1;
                var secondLine = reader.ReadLine()?.Split();
                a = int.Parse(secondLine?[0]);
                b = int.Parse(secondLine?[1]);
                c = int.Parse(secondLine?[2]);
                data = new int[n];
                data[0] = (int.Parse(secondLine?[3]));
                data[1] = (int.Parse(secondLine?[4]));
            }
            for (var i = 2; i < n; i++)
            {
                data[i] = (a * data[i - 2] + b * data[i - 1] + c);
            }


            using (var writer = new StreamWriter("output.txt"))
            {
                quick_sort(data, 0, n - 1, k1, k2);
                for (var i = k1; i <= k2; i++)
                {
                    writer.Write($"{data[i]} ");
                }
            }
        }
    }
}
