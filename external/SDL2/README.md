# Local SDL2 setup (Windows + MSVC)

This project is configured to load SDL2 from this local folder:

- external/SDL2/lib/x64/SDL2.lib
- external/SDL2/lib/x64/SDL2.dll
- external/SDL2/include/*

Recommended version: SDL2 2.32.10

## Install

1. Download SDL2-devel-2.32.10-VC.zip from SDL releases.
2. Extract it.
3. Copy these files/folders into this project:
   - extracted/SDL2-2.32.10/lib/x64/SDL2.lib -> external/SDL2/lib/x64/SDL2.lib
   - extracted/SDL2-2.32.10/lib/x64/SDL2.dll -> external/SDL2/lib/x64/SDL2.dll
   - extracted/SDL2-2.32.10/include/* -> external/SDL2/include/

After this, use cargo build/cargo run from the project root.
