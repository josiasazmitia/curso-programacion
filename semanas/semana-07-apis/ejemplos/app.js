const lista = document.querySelector("#lista");

async function cargarProductos() {
  try {
    const respuesta = await fetch("https://fakestoreapi.com/products?limit=5");
    const productos = await respuesta.json();

    for (const producto of productos) {
      const item = document.createElement("li");
      item.textContent = producto.title;
      lista.appendChild(item);
    }
  } catch (error) {
    console.error("Error al cargar productos:", error);
  }
}

cargarProductos();
