#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define SIZE 8

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/

int max_element_index(int *array, size_t size)
{
    int i;
    int idx;
    int max;

    max = 0;
    for (i = 0; i < size; i++)
    {
        if (max < array[i])
        {
            max = array[i];
            idx = i;
        }
    }
    return (idx);
}

int main()
{
    int mountain_h[SIZE];
    int position = 10;
    int i;

    while (true)
    {
        for (i = 0; i < SIZE; i++)
        {
            scanf("%d", &mountain_h[i]);
        }
        fprintf(stdout, "%i\n", max_element_index(mountain_h, SIZE));
    }
    return (0);
}
