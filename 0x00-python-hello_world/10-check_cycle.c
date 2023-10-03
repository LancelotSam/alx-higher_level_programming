#include "lists.h"
/**
 * check_cycle-this is the main function
 * it checks if a singly linked list has a cycle
 * @list: the struct
 * Return: 0 if there is no cycle, and 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;/*advance by node node*/
		fast = fast->next->next;/*advance by two nodes*/
		if (slow == fast)/*if pointing on the same node*/
			return (1);
	}

	return (0);
}
