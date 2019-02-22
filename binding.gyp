{
  "targets": [
    {
      "target_name": "testlib",
      "sources": [
        "jsbinding.cpp",
      ],
      "include_dirs": [
          "<!@(node -p \"require('node-addon-api').include\")",
          "<(module_root_dir)/clib",
      ],
      "link_settings": {
        "conditions": [
          ['OS=="win"',
            {
              'libraries': [
                "<(module_root_dir)\\clib\\foo.lib",
              ]
            },
            {
              'libraries': [
                "<(module_root_dir)/clib/libfoo.a"
              ],
            },
          ]
        ],
      },
      'dependencies': [
        "<!(node -p \"require('node-addon-api').gyp\")"
      ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'xcode_settings': {
        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
        'CLANG_CXX_LIBRARY': 'libc++',
        'MACOSX_DEPLOYMENT_TARGET': '10.7',
      },
      "conditions": [
        ['OS=="win"',
          {
            'cflags': [ "-m32" ],
            'ldflags': [ "-m elf_i386" ],
            'cflags_cc': [ "-fPIC -m32" ],
          },
        ]
      ],
      'msvs_settings': {
        'VCCLCompilerTool': { 'ExceptionHandling': 1 },
        "VCLinkerTool": {
          "LinkIncremental": 1,
        }
      },
    }
  ]
}