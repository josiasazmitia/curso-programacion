let contador = 0;
const boton = document.querySelector("#sumar");
const valor = document.querySelector("#valor");

boton.addEventListener("click", () => {
  contador += 1;
  valor.textContent = contador;
});
