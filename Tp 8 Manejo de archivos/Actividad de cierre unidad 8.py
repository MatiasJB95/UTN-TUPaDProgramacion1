from pathlib import Path

ARCHIVO = "productos.txt"

def parsear_linea(linea: str):
    partes = linea.strip().split(",")
    if len(partes) != 3:
        return None
    nombre = partes[0].strip()
    try:
        precio = float(partes[1].strip())
        cantidad = int(partes[2].strip())
    except ValueError:
        return None
    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}

def formatear_linea(prod: dict) -> str:
    return f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n"

def mostrar_producto(prod: dict):
    print(f"Producto: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Cantidad: {prod['cantidad']}")

def crear_archivo_inicial_si_falta():
    ruta = Path(ARCHIVO)
    if not ruta.exists():
        lineas = [
            "Lapicera,120.5,30\n",
            "Cuaderno,850.0,12\n",
            "Goma,90.0,50\n",
        ]
        with open(ARCHIVO, "w", encoding="utf-8") as f:
            f.writelines(lineas)
        print(f"Se creó {ARCHIVO} con 3 productos iniciales.")

def leer_productos():
    productos = []
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        for linea in f:
            if not linea.strip():
                continue
            prod = parsear_linea(linea)
            if prod is None:
                print(f"Línea inválida: {linea.strip()}")
                continue
            productos.append(prod)
    return productos

def agregar_producto_append():
    print("\nFormato: nombre, precio, cantidad")
    nombre = input("Nombre: ").strip()
    if not nombre:
        print("Nombre vacío, cancelado.")
        return None

    try:
        precio = float(input("Precio: ").strip().replace(",", "."))
        cantidad = int(input("Cantidad: ").strip())
    except ValueError:
        print("Datos invalidos. Deben ser numericos")
        return None

    nuevo = {"nombre": nombre, "precio": precio, "cantidad": cantidad}

    with open(ARCHIVO, "a", encoding="utf-8") as f:
        f.write(formatear_linea(nuevo))

    print("Producto agregado al archivo.")
    return nuevo

def buscar_por_nombre(productos):
    objetivo = input("\n Ingresa el nombre a buscar: ").strip()
    if not objetivo:
        print("Busqueda vacía.")
        return
    objetivo_norm = objetivo.casefold()
    encontrados = [p for p in productos if p["nombre"].casefold() == objetivo_norm]
    if encontrados:
        print(f"Se encontraron {len(encontrados)} productos:")
        for p in encontrados:
            mostrar_producto(p)
    else:
        print("No existe un producto con ese nombre.")


def guardar_productos(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        for p in productos:
            f.write(formatear_linea(p))
    print("Archivo sobrescrito con los productos actualizados.")

def main():
    crear_archivo_inicial_si_falta()

    productos = leer_productos()

    print("\nListado actual")
    for p in productos:
        mostrar_producto(p)

    while True:
        resp = input("\n¿Querés agregar un producto?: ").strip().lower()
        if resp == "s":
            nuevo = agregar_producto_append()
            if nuevo:
                productos.append(nuevo)
        elif resp == "n":
            break
        else:
            print("Opción no válida.")

    buscar_por_nombre(productos)

    guardar_productos(productos)

    print("\nVerificación final")
    for p in leer_productos():
        mostrar_producto(p)


if __name__ == "__main__":
    main()