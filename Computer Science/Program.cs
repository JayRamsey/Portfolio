﻿using System;

namespace arrays
{
    class program
    {
        static void Main(string[] args)
        {
            createGrid();

        }
        public static void createGrid()
        {
            int[,] grid = {{1, 2, 3, 4},
                           {5, 6, 7, 8 },
                           {9, 10, 11, 12},
                           {13, 14, 15,16}, 
                          };

            for (int i = 0; i < grid.GetLength(0); i++)
            {
                for (int j = 0; j < grid.GetLength(1); j++)
                {
                    
                    Console.Write(grid[i, j] + "  ");
                }

                Console.WriteLine();

            }

        }
    }
}