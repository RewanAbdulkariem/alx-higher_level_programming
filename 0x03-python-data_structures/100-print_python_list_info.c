#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - Prints information about a Python list.
 * @p: Pointer to a Python list object.
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = PyList_Size(p);
	Py_ssize_t alloc = ((PyListObject *)p)->allocated;
	Py_ssize_t i;
	PyObject *obj;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", alloc);

	for (i = 0; i < list_size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
