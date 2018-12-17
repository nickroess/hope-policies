class RipeConfigs:
    configs= [
      ('shellcode', 'direct', 'stack', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'stack', 'funcptrstackvar', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'stack', 'funcptrstackparam', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'stack', 'structfuncptrstack', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'heap', 'funcptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'heap', 'structfuncptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'bss', 'funcptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'bss', 'structfuncptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'data', 'funcptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'direct', 'data', 'structfuncptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'funcptrstackvar', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'funcptrstackparam', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'funcptrheap', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'funcptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'funcptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'structfuncptrstack', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'structfuncptrheap', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'structfuncptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'stack', 'structfuncptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'ret', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'funcptrstackvar', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'funcptrstackparam', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'funcptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'funcptrbss', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'funcptrdata', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'structfuncptrstack', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'structfuncptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'structfuncptrdata', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'heap', 'structfuncptrbss', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'funcptrstackvar', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'funcptrstackparam', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'funcptrheap', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'funcptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'funcptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'structfuncptrstack', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'structfuncptrheap', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'structfuncptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'bss', 'structfuncptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'funcptrstackvar', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'funcptrstackparam', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'funcptrheap', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'funcptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'funcptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'structfuncptrstack', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'structfuncptrheap', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'structfuncptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('shellcode', 'indirect', 'data', 'structfuncptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.rwx', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'direct', 'stack', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'direct', 'stack', 'funcptrstackvar', 'memcpy', []),
      ('returnintolibc', 'direct', 'stack', 'funcptrstackparam', 'memcpy', []),
      ('returnintolibc', 'direct', 'stack', 'structfuncptrstack', 'memcpy', []),
      ('returnintolibc', 'direct', 'heap', 'funcptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'direct', 'heap', 'structfuncptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'direct', 'bss', 'funcptrbss', 'memcpy', []),
      ('returnintolibc', 'direct', 'bss', 'structfuncptrbss', 'memcpy', []),
      ('returnintolibc', 'direct', 'data', 'funcptrdata', 'memcpy', []),
      ('returnintolibc', 'direct', 'data', 'structfuncptrdata', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'stack', 'funcptrstackvar', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'funcptrstackparam', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'funcptrheap', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'funcptrbss', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'funcptrdata', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'structfuncptrstack', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'structfuncptrheap', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'structfuncptrdata', 'memcpy', []),
      ('returnintolibc', 'indirect', 'stack', 'structfuncptrbss', 'memcpy', []),
      ('returnintolibc', 'indirect', 'heap', 'ret', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'funcptrstackvar', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'funcptrstackparam', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'funcptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'funcptrbss', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'funcptrdata', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'structfuncptrstack', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'structfuncptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'structfuncptrdata', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'heap', 'structfuncptrbss', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'bss', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'bss', 'funcptrstackvar', 'memcpy', []),
      ('returnintolibc', 'indirect', 'bss', 'funcptrstackparam', 'memcpy', []),
      ('returnintolibc', 'indirect', 'bss', 'funcptrheap', 'memcpy', []),
      ('returnintolibc', 'indirect', 'bss', 'funcptrbss', 'memcpy', []),
      ('returnintolibc', 'indirect', 'bss', 'funcptrdata', 'memcpy', []),
      ('returnintolibc', 'indirect', 'bss', 'structfuncptrstack', 'memcpy', []),
      ('returnintolibc', 'indirect', 'bss', 'structfuncptrheap', 'memcpy', []),
      ('returnintolibc', 'indirect', 'bss', 'structfuncptrdata', 'memcpy', []),
      ('returnintolibc', 'indirect', 'bss', 'structfuncptrbss', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('returnintolibc', 'indirect', 'data', 'funcptrstackvar', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'funcptrstackparam', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'funcptrheap', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'funcptrbss', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'funcptrdata', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'structfuncptrstack', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'structfuncptrheap', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'structfuncptrdata', 'memcpy', []),
      ('returnintolibc', 'indirect', 'data', 'structfuncptrbss', 'memcpy', []),
      ('rop', 'direct', 'stack', 'ret', 'memcpy', ['osv.hifive.main.stack', 'osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'stack', 'funcptrstackvar', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'stack', 'funcptrstackparam', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'stack', 'structfuncptrstack', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'heap', 'funcptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'heap', 'structfuncptrheap', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'bss', 'funcptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'bss', 'structfuncptrbss', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'data', 'funcptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('rop', 'direct', 'data', 'structfuncptrdata', 'memcpy', ['osv.hifive.main.threeClass', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('dataonly', 'direct', 'stack', 'bof', 'memcpy', []),
      ('dataonly', 'direct', 'stack', 'iof', 'memcpy', []),
      ('dataonly', 'direct', 'stack', 'leak', 'memcpy', []),
      ('dataonly', 'direct', 'heap', 'bof', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('dataonly', 'direct', 'heap', 'iof', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('dataonly', 'direct', 'heap', 'leak', 'memcpy', ['osv.hifive.main.heap', 'osv.hifive.main.heap-rwx-stack-threeClass']),
      ('dataonly', 'direct', 'bss', 'bof', 'memcpy', []),
      ('dataonly', 'direct', 'bss', 'iof', 'memcpy', []),
      ('dataonly', 'direct', 'bss', 'leak', 'memcpy', []),
      ('dataonly', 'direct', 'data', 'bof', 'memcpy', []),
      ('dataonly', 'direct', 'data', 'iof', 'memcpy', []),
      ('dataonly', 'direct', 'data', 'leak', 'memcpy', []),
      ('dataonly', 'indirect', 'stack', 'bof', 'memcpy', []),
      ('dataonly', 'indirect', 'bss', 'bof', 'memcpy', []),
      ('dataonly', 'indirect', 'data', 'bof', 'memcpy', []),
    ]
