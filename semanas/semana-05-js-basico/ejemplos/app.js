const precios = [120, 80, 60];

function calcularTotal(lista) {
  let total = 0;
  for (const precio of lista) {
    total += precio;
  }
  return total;
}

console.log("Total:", calcularTotal(precios));
