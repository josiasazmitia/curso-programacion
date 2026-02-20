# Curso guiado: Programación web desde cero

## Enfoque del curso

Este curso está diseñado para personas que **nunca han programado** o que sienten miedo al código. Está pensado para poder compartirse con cualquier persona, incluso si no la conoces y parte completamente desde cero.

Aquí programarás con un método simple y práctico:

- Defines un proceso.
- Lo pruebas en pequeño.
- Mides resultados.
- Ajustas.

Duración sugerida: **8 semanas**  
Ritmo recomendado: **4 a 6 horas por semana**  
Sesión de dudas: **1 hora semanal o quincenal**

## Objetivo final

Al terminar tendrás:

1. Un sitio web estático profesional.
2. Un sitio dinámico que consume una API pública.
3. Un portafolio en GitHub con buenas prácticas de commits.
4. Una base transferible para Python, automatización y análisis de datos.

---

## Capítulo 0: Mentalidad y método (antes de escribir código)

### Mensaje clave

No necesitas ser un “genio de programación”. Necesitas practicar en ciclos cortos.

### Regla de estudio 60-30-10

- 60% práctica (escribir y ejecutar código).
- 30% lectura o video.
- 10% documentación de lo aprendido.

### Método anti-miedo

Cuando algo falle:

1. Lee el error completo.
2. Cambia una sola cosa.
3. Prueba de nuevo.
4. Si funciona, haz commit.

---

## Capítulo 1 (Semana 1): Setup profesional + primera web

### Objetivos

- Instalar herramientas.
- Entender qué es cliente, servidor y HTTP.
- Crear tu primer repositorio y primer commit.

### Herramientas

- Visual Studio Code
- Git
- Cuenta de GitHub
- Navegador web (Chrome/Edge/Firefox)

### Mini proyecto

Repositorio: `mi-primera-web`

Estructura:

```text
mi-primera-web/
	├─ index.html
	└─ README.md
```

Ejemplo básico de `index.html`:

```html
<!doctype html>
<html lang="es">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Mi primera web</title>
	</head>
	<body>
		<h1>Hola, mundo</h1>
		<p>Estoy empezando en programación y este es mi primer proyecto web.</p>
	</body>
</html>
```

---

## Capítulo 2 (Semana 2): HTML estructurado

### Conceptos

- Etiquetas semánticas: `header`, `main`, `section`, `footer`
- Listas, enlaces e imágenes
- Formularios simples

### Mini proyecto

Repositorio: `biografia-html`

Debe incluir:

- Sección “Sobre mí”
- Habilidades
- Proyectos
- Formulario de contacto

---

## Capítulo 3 (Semana 3): CSS para diseño limpio y ordenado

### Conceptos

- Selectores
- Modelo de caja
- Flexbox
- Responsive básico

### Mini proyecto

Agregar `styles.css` al proyecto de biografía.

Ejemplo básico de CSS:

```css
body {
	font-family: Arial, sans-serif;
	margin: 0;
	padding: 0;
}

header {
	background: #0b5fff;
	color: white;
	padding: 16px;
}

main {
	max-width: 900px;
	margin: 24px auto;
	padding: 0 16px;
}
```

---

## Capítulo 4 (Semana 4): Proyecto de cierre de mes 1

Repositorio: `ecommerce-maqueta`

Debe incluir:

- Navbar
- Hero principal
- Grid de productos
- Página de detalle
- Responsive básico

Resultado: web estática presentable para portafolio.

---

## Capítulo 5 (Semana 5): JavaScript básico

### Conceptos

- Variables (`let`, `const`)
- Tipos de datos
- Condicionales
- Funciones
- Arreglos y objetos

### Ejemplo básico

```js
const precios = [120, 80, 60];

function calcularTotal(listaPrecios) {
	let total = 0;
	for (const precio of listaPrecios) {
		total += precio;
	}
	return total;
}

console.log("Total:", calcularTotal(precios));
```

### Mini proyecto

Repositorio: `ecommerce-js-basico`  
Funcionalidad mínima:

- Agregar producto
- Calcular total
- Mostrar resultado

---

## Capítulo 6 (Semana 6): DOM y eventos

### Conceptos

- `document.querySelector`
- `addEventListener`
- `textContent`
- `value`

### Ejemplo básico

```html
<button id="btn">Sumar 1</button>
<p id="contador">0</p>

<script>
	let valor = 0;
	const btn = document.querySelector("#btn");
	const contador = document.querySelector("#contador");

	btn.addEventListener("click", () => {
		valor += 1;
		contador.textContent = valor;
	});
</script>
```

---

## Capítulo 7 (Semana 7): APIs y datos reales

### Conceptos

- JSON
- `fetch`
- `async/await`
- Manejo básico de errores

### APIs sugeridas

- Fake Store API
- JSONPlaceholder

### Ejemplo básico

```js
async function cargarProductos() {
	try {
		const respuesta = await fetch("https://fakestoreapi.com/products?limit=3");
		const productos = await respuesta.json();
		console.log(productos);
	} catch (error) {
		console.error("Error al cargar productos:", error);
	}
}

cargarProductos();
```

### Mini proyecto

Repositorio: `ecommerce-dinamico-api`

---

## Capítulo 8 (Semana 8): Portafolio y presentación profesional

Repositorio final: `portafolio-web`

Debe incluir:

- Proyecto biografía
- E-commerce estático
- E-commerce dinámico con API
- README profesional con tecnologías, capturas y aprendizajes

---

## Guía rápida de Git y commits (paso a paso)

## 1) Crear repositorio local

```bash
git init
```

## 2) Ver estado

```bash
git status
```

## 3) Agregar archivos

```bash
git add .
```

## 4) Hacer commit

```bash
git commit -m "feat: crear estructura inicial del proyecto"
```

## 5) Conectar a GitHub

```bash
git remote add origin https://github.com/tu-usuario/mi-primera-web.git
git branch -M main
git push -u origin main
```

## 6) Flujo diario recomendado

```bash
git status
git add .
git commit -m "feat: agregar sección de proyectos"
git push
```

### Ejemplos de mensajes de commit

- `feat: agregar formulario de contacto`
- `fix: corregir estilos en vista móvil`
- `docs: actualizar README con instrucciones`
- `refactor: simplificar función de total`

---

## Reglas del curso

1. Mínimo 3 a 5 commits por semana.
2. Actualizar README en cada entrega.
3. No copiar código que no entiendas.
4. Escribir un diario breve semanal: qué aprendí, qué falló, qué mejoré.
5. Pedir ayuda cuando un error tome más de 30 minutos.

---

## ¿Para qué te sirve aprender programación?

Programar te ayuda a:

- Automatizar tareas repetitivas.
- Crear herramientas simples para trabajo o estudio.
- Entender mejor cómo funcionan apps y sistemas.
- Resolver problemas de forma más estructurada.

---

## Referencias recomendadas (gratuitas)

- MDN Web Docs (HTML, CSS, JavaScript)
- GitHub Skills (aprendizaje guiado de Git/GitHub)
- freeCodeCamp (práctica por proyectos)
- JavaScript.info (explicaciones claras)

---

## Resultado esperado al finalizar

- 4 a 6 repositorios públicos sólidos.
- Portafolio inicial para prácticas profesionales.
- Confianza para continuar con React, backend o Python.
- Base técnica para aplicar programación en proyectos reales de cualquier área.
