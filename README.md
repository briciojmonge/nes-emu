# NES Emulator in Rust

Proyecto personal en Rust que implementa una CPU estilo 6502 y ejecuta un mini juego Snake renderizado con SDL2.

El objetivo del proyecto es practicar emulacion, manejo de memoria y ciclo de ejecucion de instrucciones.

## Requisitos

- Rust y Cargo instalados
- SDL2 para Windows (DLL disponible en la carpeta del proyecto)

Estructura esperada para SDL2:

- external/SDL2/lib/x64/SDL2.dll

## Compilar

Compilacion en modo debug:

```powershell
cargo build
```

Compilacion en modo release (genera ejecutable optimizado):

```powershell
cargo build --release
```

## Ejecutar

Ejecucion en debug:

```powershell
cargo run
```

Ejecucion del binario release:

```powershell
./target/release/nes-emu.exe
```

## Notas

- Si el programa no abre ventana o se cierra inmediatamente, verifica que SDL2.dll exista en external/SDL2/lib/x64/.
- El script scripts/run-with-sdl2.ps1 agrega automaticamente esa ruta al PATH cuando ejecutas con cargo run.
