

# macOS

    npm i node-addon-api
    clang -c -o foo.o foo.c
    ar rcs clib/libfoo.a foo.o
    node-gyp clean configure build --verbose

# Windows

    npm i node-addon-api
    gcc -c -o foo.o foo.c
    ar rcs clib/foo.lib foo.o
    node-gyp clean configure build --arch=ia32 --verbose

# cleanup

    rm *.o
    node-gyp clean
