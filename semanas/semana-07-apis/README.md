# Semana 07: APIs y datos reales

## Objetivo

Consumir datos externos con `fetch` y mostrar resultados.

### What you will learn

- Qué es una API y qué es JSON.
- Cómo hacer peticiones con `fetch`.
- Uso básico de `async/await` y `try/catch`.

### What you will build

Una página que consulta productos de una API pública y los muestra en una lista.

## Archivos de ejemplo

- `ejemplos/index.html`
- `ejemplos/app.js`

## Conceptos

- JSON
- `fetch`
- `async/await`
- Manejo básico de errores

## Paso a paso

1. Haz una petición a una API pública.
2. Convierte la respuesta a JSON.
3. Muestra datos en consola o pantalla.
4. Maneja errores con `try/catch`.

### Step-by-step checklist

- [ ] Crear estructura HTML para mostrar resultados.
- [ ] Implementar función `async`.
- [ ] Consumir API con `fetch`.
- [ ] Renderizar datos en el DOM.
- [ ] Manejar errores de red.
- [ ] Commit y push de la funcionalidad.

## Mini reto

- Mostrar en pantalla el título de 5 productos.

### Deliverable

By the end of this week you should have: una página que consume una API y muestra datos reales.

### Common mistakes

- Olvidar `await` en `fetch` o en `response.json()`.
- No controlar errores y romper la ejecución.
- Asumir que la API siempre responde igual.
