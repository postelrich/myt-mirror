
module_registry = {}

register_module = function (name, module) {
  module_registry[name] = module;
};
