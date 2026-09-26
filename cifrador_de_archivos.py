import os, time, glob

# --- FUNCIÓN PARA LIMPIAR LA PANTALLA ---
def limpiar():
    os.system('clear' if os.name == 'posix' else 'cls')

# --- FUNCIÓN PARA OBTENER ARCHIVOS ---
def obtener_archivos(extensiones):
    archivos = []
    for ext in extensiones:
        archivos.extend(glob.glob(f"*.{ext}"))
    return archivos

# --- FUNCIÓN DE RENOMBRADO ---
def renombrar_suite(ruta, extensiones, tipo_nombre):
    os.chdir(ruta)
    archivos = obtener_archivos(extensiones)

    if archivos:
        print(f"\n📁 Se encontraron {len(archivos)} archivos de tipo {tipo_nombre}.")
        nuevo_nombre_base = input("¿Cómo quieres que se llamen? (sin número ni extensión): ").strip()
        if nuevo_nombre_base == "":
            nuevo_nombre_base = "Archivo"
            print("Usando nombre por defecto: 'Archivo'")

        print(f"\n🔄 Renombrando a '{nuevo_nombre_base}_1', '{nuevo_nombre_base}_2'...\n")
        for i, archivo in enumerate(archivos):
            _, extension = os.path.splitext(archivo)
            nuevo_nombre = f"{nuevo_nombre_base}_{i + 1}{extension}"
            if os.path.exists(nuevo_nombre):
                print(f"⚠️  Ya existe {nuevo_nombre}, se salta {archivo}")
            else:
                os.rename(archivo, nuevo_nombre)
                print(f"✅ {archivo} --> {nuevo_nombre}")
            time.sleep(0.03)
        print("\n🎉 ¡Organización completada!")
    else:
        print(f"❌ No se encontraron archivos de tipo {tipo_nombre} en esa ruta.")

# --- FUNCIÓN PRINCIPAL DEL MENÚ ---
def menu():
    limpiar()
    print("=" * 40)
    print("   📂 SUITE DE ORGANIZACIÓN DE ARCHIVOS")
    print("=" * 40)
    print("1. 📸 Organizar Imágenes (jpg, png, jpeg, webp)")
    print("2. 🎵 Organizar Música (mp3, wav, flac, ogg)")
    print("3. 🎬 Organizar Videos (mp4, avi, mkv, mov)")
    print("4. 📄 Organizar Otros (selección personalizada)")
    print("5. ❌ Salir")
    print("=" * 40)
    
    opcion = input("Elige una opción (1-5): ").strip()
    
    if opcion == "1":
        ruta = os.path.expanduser(input("Pegue la ruta de imágenes: > ").strip())
        if os.path.exists(ruta):
            renombrar_suite(ruta, ["jpg", "jpeg", "png", "webp"], "imágenes")
        else:
            print("❌ Ruta no válida.")
    elif opcion == "2":
        ruta = os.path.expanduser(input("Pegue la ruta de música: > ").strip())
        if os.path.exists(ruta):
            renombrar_suite(ruta, ["mp3", "wav", "flac", "ogg"], "música")
        else:
            print("❌ Ruta no válida.")
    elif opcion == "3":
        ruta = os.path.expanduser(input("Pegue la ruta de videos: > ").strip())
        if os.path.exists(ruta):
            renombrar_suite(ruta, ["mp4", "avi", "mkv", "mov"], "videos")
        else:
            print("❌ Ruta no válida.")
    elif opcion == "4":
        ruta = os.path.expanduser(input("Pegue la ruta de archivos: > ").strip())
        if os.path.exists(ruta):
            print("Escribe las extensiones separadas por comas (ej: pdf,docx,txt)")
            extensiones = [e.strip() for e in input("Extensiones: > ").strip().split(",")]
            renombrar_suite(ruta, extensiones, "personalizados")
        else:
            print("❌ Ruta no válida.")
    elif opcion == "5":
        print("👋 ¡Hasta luego, Persona Agradablee!")
        exit()
    else:
        print("❌ Opción no válida.")
    
    print("\n⏳ Volviendo al menú en 3 segundos...")
    time.sleep(3)
    menu()

# --- EJECUTAR EL MENÚ ---
if __name__ == "__main__":
    menu()
