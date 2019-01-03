/*
 * File: 103-python.c
 * Auth: Brennan D Baraban
 */

#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int size, alloc, i;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size = var->ob_size;
	alloc = list->allocated;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		fflush(stdout);
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	fflush(stdout);
	printf("[*] Size of the Python List = %d\n", size);
	fflush(stdout);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		fflush(stdout);
		printf("Element %d: %s\n", i, type);
		fflush(stdout);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		fflush(stdout);
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	fflush(stdout);
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	fflush(stdout);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;

	fflush(stdout);
	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		fflush(stdout);
		printf("%02hhx", bytes->ob_sval[i]);
		fflush(stdout);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	int round;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		fflush(stdout);
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	fflush(stdout);
	printf("  value: %.15g", float_obj->ob_fval);
	round = (int)float_obj->ob_fval;
	if (float_obj->ob_fval - round == 0 ||
	    round - float_obj->ob_fval == 0)
	{
		fflush(stdout);
		printf(".0");
	}
	fflush(stdout);
	printf("\n");
}
