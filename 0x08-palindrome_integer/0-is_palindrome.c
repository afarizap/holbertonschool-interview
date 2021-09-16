#include "palindrome.h"

/**
 * is_palindrome - checks whether or not
 *  a given unsigned integer is a palindrome
 *
 * @n: number to be checked
 *
 * Return: 1 if n is a palindrome, and 0 otherwise
 */
int is_palindrome(unsigned long n)
{
	unsigned long temp, sum;

	temp = n;
	sum = 0;
	while (temp > 0)
	{
	sum = (sum * 10) + (temp % 10);
	temp /= 10;
	}

	if (n == sum)
		return (1);
	return (0);
}
