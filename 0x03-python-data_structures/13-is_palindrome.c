#include <stddef.h>
#include "lists.h"
/**
 * reverseList - Reverse a singly-linked list in place.
 * @head: Pointer to the head of the linked list.
 *
 * Return: Pointer to the new head of the reversed list.
 */
listint_t *reverseList(listint_t *head)
{
	listint_t *current = head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
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

	if (!head || !(*head)->next)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *secondHalf = reverseList(slow);

	listint_t *firstHalf = *head;

	while (secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
			return (0);
		firstHalf = firstHalf->next;
		secondHalf = secondHalf->next;
	}
	return (1);
}
