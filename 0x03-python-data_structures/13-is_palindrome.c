/*
 * File: 13-is_palindrome.c
 * Auth: Brennan D Baraban
 */

#include "lists.h"

int recursive_is_palindrome(listint_t *head, listint_t *check, size_t idx);
int is_palindrome(listint_t **head);

/**
 * recursive_is_palindrome - Recursively checks if a singly-linked
 *                           list is a palindrome.
 * @head: The head of the singly-linked list.
 * @check: The next node of the list to compare.
 * @idx: The indexed node from head to compare to check.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int recursive_is_palindrome(listint_t *head, listint_t *check, size_t idx)
{
	listint_t *tmp = head;
	size_t i;

	if (idx == 0)
		return (1);

	for (i = 0; i < idx; i++)
		tmp = tmp->next;

	if (tmp->n != check->n)
		return (0);

	return (recursive_is_palindrome(head, check->next, idx - 1));
}

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: A pointer to the head of the linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	size_t size = 0, i;

	if (*head == NULL)
		return (1);

	tmp = *head;
	while (tmp)
	{
		size++;
		tmp = tmp->next;
	}

	tmp = *head;
	for (i = 0; i < (size / 2) - 1; i++)
		tmp = tmp->next;

	if ((size % 2) == 0 && tmp->n != tmp->next->n)
		return (0);

	if ((size % 2) != 0)
		size = (size / 2) - 1;
	else
		size = (size / 2) - 2;

	tmp = tmp->next->next;

	return (recursive_is_palindrome(*head, tmp, size));
}
