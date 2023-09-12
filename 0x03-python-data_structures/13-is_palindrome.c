#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* is_palindrome - Check if a singly-linked list of integers is a palindrome.
* @head: Pointer to the head of the linked list.
*
* Return: 1 if it is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (*head == NULL)
		return (1);

	while (fast && fast->next && fast->next->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	slow = reverseList(&slow);
	fast = *head;
	while (slow && fast)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}

	return (1);
}

/**
* reverse_list - Reverse a linked list
* @head: The list
*
* Return: Pointer to the new head
*/
listint_t *reverseList(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}
