/*
 * File: 13-is_palindrome.c
 * Auth: Brennan D Baraban
 */

#include "lists.h"

listint_t *get_node_at_index(listint_t *head, unsigned int index);
int is_palindrome(listint_t **head);

/**
 * get_node_at_index - Locates a given node in a singly linked list.
 * @head: The head of the linked list.
 * @index: The index of the node to locate.
 *
 * Return: The address of the located node.
 */
listint_t *get_node_at_index(listint_t *head, unsigned int index)
{
	for (; index != 0; index--)
		head = head->next;

	return (head);
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
	listint_t *tmp, *h;
	unsigned int nodes = 0, i;

	if (*head == NULL)
		return (1);

	tmp = *head;
	while (tmp->next)
	{
		nodes++;
		tmp = tmp->next;
	}

	h = *head;
	for (i = 0; i < (nodes / 2); i++)
	{
		tmp = get_node_at_index(*head, nodes - i);
		if (h->n != tmp->n)
			return (0);
		h = h->next;
	}

	return (1);
}
