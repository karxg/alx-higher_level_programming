#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list.
* @head: list head
* @number: number to store in the new node
* Return: pointer to the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
		listint_t *current;
		listint_t *new;

		current = *head;

		new = malloc(sizeof(listint_t));
		if (new == NULL)
			return (NULL);
		new->n = number;

		if (*head == NULL || (*head)->n > number)
		{
			new->next = *head;
			*head = new;
			return (new);
		}

		while (current->next != NULL)
		{
			if ((current->next)->n >= number)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
				current = current->next;
		}

		new->next = NULL;
		current->next = new;
		return (new);
}
