#include "lists.h"
/**
 * insert_node-this is the main function
 * it inserts a number/node into a sorted linked list
 * @head: the head of the list
 * @number: the integer number to be inserted
 * Return:address of the new node, Null if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *prev;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return NULL;
	return (new_node);

}
