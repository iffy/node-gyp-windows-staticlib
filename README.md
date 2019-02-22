I'm trying to make a native addon that links against a static library.  On macOS it creates the `testlib.node` file without error, but on Windows I get the following error:

```
jsbinding.obj : error LNK2001: unresolved external symbol "void __cdecl foo_thing(void)" (?foo_thing@@YAXXZ) [C:\sample\build\testlib.vcxproj]
C:\sample\build\Release\testlib.node : fatal error LNK1120: 1 unresolved externals [C:\sample\build\testlib.vcxproj]
```

## Building

Below are the commands I ran to build the addon using node-gyp.  Each *also* includes commands for building a static library, but that's just so I can demonstrate the linking error.

# macOS

```
npm i node-addon-api
clang -c -o foo.o foo.c
ar rcs clib/libfoo.a foo.o
node-gyp clean configure build --verbose
```

# Windows

I'm using Mingw on my machine to build the static lib.

```
npm i node-addon-api
gcc -c -o foo.o foo.c
ar rcs clib/foo.lib foo.o
node-gyp clean configure build --arch=ia32 --verbose
```
