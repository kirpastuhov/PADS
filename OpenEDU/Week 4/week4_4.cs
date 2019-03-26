using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace Week4_4 {
    public sealed class Program {
        private static StreamReader _in;
        private static StreamWriter _out;

        private static void Main(string[] args) {
            if (!args.Contains("console")) {
                SetupIO();
            }

            Run();

            if (args.Contains("console")) {
                Console.ReadLine();
            }

            DisposeIO();
        }

        private static void Run() {
            var n = int.Parse(Console.ReadLine());
            var queue = new Queue<int>();

            var mins = new LinkedList<int>();

            for (var i = 0; i < n; i++) {
                var line = ReadLineArray();

                switch (line[0]) {
                    case "+":
                        var a = int.Parse(line[1]);
                        queue.Enqueue(a);

                        while (mins.Count > 0 && mins.First.Value > a) {
                            mins.RemoveFirst();
                        }

                        mins.AddFirst(a);
                        break;
                    case "-":
                        var b = queue.Dequeue();

                        if (mins.Last.Value == b) {
                            mins.RemoveLast();
                        }

                        break;
                    default:
                        Console.WriteLine(mins.Last.Value);
                        break;
                }
            }
        }

        private static string[] ReadLineArray() {
            return Console.ReadLine()
                .Split(' ')
                .ToArray();
        }

        private static void SetupIO() {
            _in = new StreamReader("input.txt");
            _out = new StreamWriter("output.txt");

            Console.SetIn(_in);
            Console.SetOut(_out);
        }

        private static void DisposeIO() {
            _in?.Dispose();
            _out?.Dispose();
        }
    }
}
