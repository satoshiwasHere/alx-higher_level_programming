#include "hash_tables.h"
#include <stdlib.h>
/**
 * hash_table_create - Creates a hash table
 * @size : The size of the array
 *
 * Return: incase of error - NULL
 *   	alternatively - a pointer to the new hash table
 */


hash_table_t *hash_table_create(unsigned long int size)
{
    unsigned long int i = 0;
    hash_table_t *new_table = NULL;

    """Allocate mem for the new table"""
    new_table = malloc(sizeof(hash_table_t));
    if (!new_table)
        return (NULL);

    """Set table size"""
    new_table->size = size;

    """Allocate mem for the nodes"""
    new_table->array = malloc(sizeof(hash_node_t *) * size);
    if (!new_table->array)
    {
        free(new_table);
        return (NULL);
    }

	""""Initialize all nodes to NULL""""
    for (; i < size; i++)
        (new_table->array)[i] = NULL;

    return (new_table);
}
