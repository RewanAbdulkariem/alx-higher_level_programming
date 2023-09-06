#include "lists.h"
#include <stdlib.h>


/**
 * insert_node - Inserts a new node with the given number into a sorted
 * singly linked list.
 * @head: A pointer to a pointer to the head of the list.
 * @number: The value to be inserted into the new node.
 * Return: A pointer to the newly inserted node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL && current->next->n < number)
			current = current->next;
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
