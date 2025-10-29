# Resumen rápido: `if __name__ == "__main__"`

Una línea para recordar:

`if __name__ == "__main__":` hace que el código dentro solo se ejecute cuando el archivo se ejecuta directamente (por ejemplo `python main.py`), y no cuando el archivo se importa como módulo.

Ejemplo mínimo

`modulo.py`:
```python
def saludar():
    print("Hola desde saludar()")
```

`main.py`:
```python
import modulo

print("Esto se imprime siempre al importar/ejecutar main")

if __name__ == "__main__":
    print("Esto solo se ejecuta si corro: python main.py")
    modulo.saludar()
```

Comportamiento:
- `python main.py` → se imprimen ambos mensajes y se llama a `saludar()`.
- `import main`   → solo se ejecuta el `print` fuera del `if`; el bloque dentro de `if __name__ == "__main__"` no se ejecuta.

Por qué es útil

- Evita efectos secundarios (como crear archivos o iniciar procesos) cuando tu archivo se importa desde otro módulo.
- Permite que el mismo archivo sea ejecutable (script) y reutilizable (módulo) a la vez.

Uso recomendado

- Coloca la lógica de ejecución (ej.: `main()` o `run()`) dentro de una función y llámala desde el bloque `if __name__ == "__main__":`.
- Así puedes importar funciones sin ejecutar la parte «activa» automáticamente.

Pequeña plantilla (recomendado):
```python
def main():
    # lógica principal
    pass

if __name__ == "__main__":
    main()
```

---

