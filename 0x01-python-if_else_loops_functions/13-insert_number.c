/*
 * File: 13-insert_number.c
 * Auth: Brennan D Baraban
 */

#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new, *tmp;

	if (*head == NULL)
		return (NULL);

	node = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	while (node && node->next->n < number)
		node = node->next;

	tmp = node->next;
	node->next = new;
	new->next = tmp;

	return (new);
}
