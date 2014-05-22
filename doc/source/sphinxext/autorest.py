
import collections
import inspect
import json

from sphinxcontrib.autohttp.tornado import AutoTornadoDirective, import_object, \
                                           prepare_docstring, http_directive, normalize_path

# use get_routes from tip, the version in PyPI doesn't work with Python 3
def get_routes(app):
    for spec in app.handlers[0][1]:
        handler = spec.handler_class
        doc_methods = list(handler.SUPPORTED_METHODS)
        if 'HEAD' in doc_methods:
            doc_methods.remove('HEAD')
        if 'OPTIONS' in doc_methods:
            doc_methods.remove('OPTIONS')

        for method in doc_methods:
            maybe_method = getattr(handler, method.lower(), None)
            if (inspect.isfunction(maybe_method) or
                    inspect.ismethod(maybe_method)):
                yield method.lower(), spec.regex.pattern, handler

class AutoRestDirective(AutoTornadoDirective):

    def make_rst(self):
        app = import_object(self.arguments[0])
        for method, path, handler in get_routes(app):
            class_name = handler.__name__
            method_name = getattr(handler, method).__name__
            endpoint = '.'.join((class_name, method_name))

            if self.endpoints and endpoint not in self.endpoints:
                continue
            if endpoint in self.undoc_endpoints:
                continue

            docstring = getattr(handler, method).__doc__ or ''
            json_schema = getattr(getattr(handler, method), '_json_schema', None)

            #if not isinstance(docstring, unicode):
            #    analyzer = ModuleAnalyzer.for_module(view.__module__)
            #    docstring = force_decode(docstring, analyzer.encoding)
            if not docstring and 'include-empty-docstring' not in self.options:
                continue


            docstring = prepare_docstring(docstring)

            # automatically fetch JSON schema and append to docstring
            try:
                index = docstring.index(":request-format:")
                if json_schema is not None:
                    # sort dict keys to ensure ordering is deterministic
                    def sort_dict(d):
                        if isinstance(d, dict):
                            return collections.OrderedDict(
                                sorted((k, sort_dict(v)) for k, v in d.items()))
                        else:
                            return d
                    json_schema = sort_dict(json_schema)

                    docstring[index:index+1] = ['', "**Expected JSON format**::", ''] + \
                        ['    ' + line for line in json.dumps(json_schema, indent=4).split('\n')]
                else:
                    docstring[index:index+1] = ['', "*The request body is ignored by this method.*"]
            except ValueError:
                pass

            for line in http_directive(method, normalize_path(path), docstring):
                yield line

def setup(app):
    app.add_directive('autorest', AutoRestDirective)
