#include "napi.h"
#include "foo.h"
#include <iostream>
using namespace std;
using namespace Napi;

Value do_foo_thing(const CallbackInfo& info) {
  Env env = info.Env();
  foo_thing();
  return env.Undefined();
}


Object Init(Env env, Object exports) {
  exports["do_foo_thing"] = Function::New(env, do_foo_thing);
  return exports;
}

NODE_API_MODULE(testlib, Init)
