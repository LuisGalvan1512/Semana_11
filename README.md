# 🌳 Estructura de Datos y Algoritmos – Semana 11

> 📚 **Tema:** Binary Search Trees (BST)  
> 📅 **Fecha:** 26/05/2025  
> 🏫 **Institución:** Tecsup  
> 👨‍🏫 **Profesor:** Garamendi Sarmiento, Elliot Leo

---

## 🎬 ¿Qué aprendimos esta semana?

Esta semana profundizamos en la estructura de **Binary Search Tree (BST)** y resolvimos cinco retos técnicos que cubren:

- 🔍 **Range Query**: cómo extraer todos los valores dentro de un rango dado usando un recorrido in-order condicional.  
- 🌲 **Lowest Common Ancestor (LCA)**: cómo encontrar el ancestro común más bajo de dos nodos aprovechando la propiedad de orden del BST.  
- ✅ **Validate BST**: cómo comprobar si un árbol binario respeta las reglas de un BST usando cotas mínimas y máximas.  
- 🎯 **Kth Smallest Element**: cómo identificar el k-ésimo elemento más pequeño mediante un recorrido in-order iterativo con pila.  
- 🔄 **BST → Circular DLL**: cómo convertir en sitio un BST en una lista doblemente enlazada circular ordenada.

---

## 👥 Integrante del equipo

- Luis Enrique Galván Morales

---

## ⚙️ Herramientas utilizadas

- 🐍 Python  
- 💻 Visual Studio Code  
- 🌐 GitHub para control de versiones

---

## 📂 Archivos del laboratorio

| Archivo               | Descripción                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `challenge_1.py`      | `range_query(root, min_val, max_val)` — valores en un rango en BST          |
| `challenge_2.py`      | `find_lca(root, val1, val2)` — ancestro común más bajo en BST               |
| `challenge_3.py`      | `is_valid_bst(root)` — validación de la propiedad BST                       |
| `challenge_4.py`      | `kth_smallest(root, k)` — k-ésimo elemento más pequeño en BST               |
| `challenge_5.py`      | `bst_to_dll(root)` — conversión de BST a lista doblemente enlazada circular |

---

## ✅ Conclusiones

- 🌳 Un BST permite búsquedas dinámicas y ordenadas en **O(log n)** en el caso balanceado, aprovechando su estructura jerárquica.  
- 🔄 Recorridos in-order, pre-orden y post-orden son la clave para implementar consultas como rango, k-ésimo elemento y conversión a otras estructuras.  
- ⚖️ Mantener un BST balanceado (o usar variantes AVL/Red-Black) es esencial para evitar el caso degenerado que reduce la eficiencia a O(n).

---

## 🚀 Bonus

> Un dominio sólido de los BST es la base para entender y diseñar estructuras avanzadas (AVL, Red-Black, B-Trees) y optimizar índices en bases de datos y sistemas de archivos en memoria.
