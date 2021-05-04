#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * is_palindrome - check if palindrome
 * @head: pointer to structure
 * Return: 1 if true or 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int counter = 0, half, counter2 = 0;
	int *buffer = NULL;

	if (!head)
		return (0);

	if (!*head)
		return (1);
	tmp = *head;
	while (tmp && tmp->next)
	{
		tmp = tmp->next;
		counter++;
	}
	buffer = malloc(sizeof(int) * counter);
	if (tmp == NULL)
		return (0);
	tmp = *head;
	counter = 0;
	while (tmp)
	{
		buffer[counter] = tmp->n;
		counter++;
		tmp = tmp->next;
	}
	half = counter / 2;
	while (half)
	{
		if (buffer[counter2] != buffer[counter - 1])
			return (0);
		half--;
		counter2++;
		counter--;
	}
	free(tmp);
	return (1);
}
