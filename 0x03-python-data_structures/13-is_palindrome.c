/*
 * File: 13-is_palindrome.c
 * Auth: Brennan D Baraban
 */

#include "lists.h"

int recursive_is_palindrome(listint_t *h, size_t size);
int is_palindrome(listint_t **head);

/**
 * recursive_is_palindrome - Recursively checks if a singly-linked
 *                           list is a palindrome.
 * @h: The head of the singly-linked list.
 * @size: The size of the singly linked list.
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int recursive_is_palindrome(listint_t *h, size_t size)
{
	listint_t *tmp = h;
	size_t i;

	for (i = 0; i < size; i++)
		tmp = tmp->next;

	if (h == tmp || h->next == tmp)
		return (1);

	if (h->n != tmp->n)
		return (0);

	return (recursive_is_palindrome(h->next, size - 2));
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
	size_t size = 0;

	if (*head == NULL)
		return (1);

	tmp = *head;
	while (tmp->next)
	{
		size++;
		tmp = tmp->next;
	}

	return (recursive_is_palindrome(*head, size));
}
