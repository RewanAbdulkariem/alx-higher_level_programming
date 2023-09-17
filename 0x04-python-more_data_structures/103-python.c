#include "Python.h"
#include <stdlib.h>
void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
/**
 * print_python_list - Print information about a Python list.
 * @p: PyObject pointer to the list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Python List\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;

	PyObject **items = ((PyListObject *)p)->ob_item;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		PyObject *item = items[i];
		printf("Element %ld: %s\n", i, item->ob_type->tp_name);
	}
}
/**
 * print_python_bytes - Print information about a Python bytes object.
 * @p: PyObject pointer to the bytes object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);

	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);

	printf("  trying string: %s\n", str);

	printf("  first %d bytes:", size > 10 ? 10 : (int)size);
	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		printf(" %02x", str[i] & 0xff);
	}
	printf("\n");
}
