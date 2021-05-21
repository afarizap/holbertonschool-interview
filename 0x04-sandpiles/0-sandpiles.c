#include <stdlib.h>
#include <stdio.h>

#include "sandpiles.h"

/**
 * print_grid - Print 3x3 grid
 * @grid: 3x3 grid
 *
 */
static void print_grid(int grid[3][3])
{
	int i, j;

	for (i = 0; i < 3; i++)
	{
		for (j = 0; j < 3; j++)
		{
			if (j)
				printf(" ");
			printf("%d", grid[i][j]);
		}
		printf("\n");
	}
}

/**
 * sandpiles_sum - sum two 3x3 grid
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 */
void sandpiles_sum(int grid1[3][3], int grid2[3][3])
{
	int i, j, max, mgrid[3][3];

	max = 0;
	for (i = 0; i < 3; i++)
		for (j = 0; j < 3; j++)
		{
			grid1[i][j] += grid2[i][j];
			if (grid1[i][j] > 3)
				max = 1;
		}
	while (max != 0)
	{
		printf("=\n");
		print_grid(grid1);
		max = 0;
		for (i = 0; i < 3; i++)
			for (j = 0; j < 3; j++)
				mgrid[i][j] = grid1[i][j];
		for (i = 0; i < 3; i++)
		{
			for (j = 0; j < 3; j++)
				if (mgrid[i][j] > 3)
				{
					grid1[i][j] -= 4;
					if (i < 2)
						grid1[i + 1][j]++;
					if (i > 0)
						grid1[i - 1][j]++;
					if (j < 2)
						grid1[i][j + 1]++;
					if (j > 0)
						grid1[i][j - 1]++;
				}
		}
		for (i = 0; i < 3; i++)
			for (j = 0; j < 3; j++)
				if (grid1[i][j] > 3)
					max = 1;
	}
}
