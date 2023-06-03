#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    modulo = importlib.util.spec_from_file_location('datos', './hidden_4.pyc')
    datos = importlib.util.module_from_spec(modulo)
    modulo.loader.exec_module(datos)
    for nombre in sorted(dir(datos)):
        if not nombre.startswith('__'):
            print(nombre)
