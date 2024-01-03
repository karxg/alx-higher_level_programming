#include "lists.h"

/**
 * check_cycle - checks wheter a singly linked list has a cycle.
 * @list: pointer to the first node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *ptr;

	current = list;
	ptr = list;
	while (current != NULL && ptr && ptr->next)
	{
		current = current->next;
		ptr = ptr->next->next;
		if (ptr == current)
			return (1);
	}

	return (0);
}
