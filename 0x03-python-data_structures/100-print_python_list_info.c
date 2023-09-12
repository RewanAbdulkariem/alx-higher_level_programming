#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d", list_size);
	printf("[*] Allocated = %d\n", alloc);

	for (Py_ssize_t i = 0; i < list_size; i++)
	{
		obj = PyList_GetItem(p, i);
	    	printf("Element %d: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
