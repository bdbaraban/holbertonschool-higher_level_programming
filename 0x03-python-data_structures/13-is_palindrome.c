/*
 * File: 13-is_palindrome.c
 * Auth: Brennan D Baraban
 */

#include "lists.h"

listint_t *add_nodeint_beginning(listint_t **head, const int n);
listint_t *reverse_listint(listint_t *node);
int is_palindrome(listint_t **head);

/**
 * add_nodeint_beginning - Adds a new node at the beginning
 *                         of a linstint_t linked list.
 * @head: A pointer to the head of the listint_t list.
 * @n: The value for the new node to contain.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - the address of the new node.
 */
listint_t *add_nodeint_beginning(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = *head;

	return (new);
}

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @node: The starting node of the list to reverse.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the head of the reversed list.
 */
listint_t *reverse_listint(listint_t *node)
{
	listint_t *new = NULL, *h = new;

	while (node)
	{
		h = add_nodeint_beginning(&h, node->n);
		if (h == NULL)
			return (NULL);
		node = node->next;
	}

	return (h);
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
	listint_t *tmp, *reverse;
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

	tmp = tmp->next->next;
	reverse = reverse_listint(tmp);

	while (reverse)
	{
		if ((*head)->n != reverse->n)
			return (0);
		*head = (*head)->next;
		reverse = reverse->next;
	}

	free(reverse);

	return (1);
}
