from _typeshed import Self
from collections.abc import Callable
from typing import Any, Generic, TypeVar, overload

from . import compat

_R = TypeVar("_R")

def md5_hex(x): ...

class safe_reraise:
    warn_only: Any
    def __init__(self, warn_only: bool = ...) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type_, value, traceback) -> None: ...

def walk_subclasses(cls) -> None: ...
def string_or_unprintable(element): ...
def clsname_as_plain_name(cls): ...
def method_is_overridden(instance_or_cls, against_method): ...
def decode_slice(slc): ...
def map_bits(fn, n) -> None: ...
def decorator(target): ...
def public_factory(target, location, class_location: Any | None = ...): ...

class PluginLoader:
    group: Any
    impls: Any
    auto_fn: Any
    def __init__(self, group, auto_fn: Any | None = ...) -> None: ...
    def clear(self) -> None: ...
    def load(self, name): ...
    def register(self, name, modulepath, objname): ...

def get_cls_kwargs(cls, _set: Any | None = ...): ...
def get_func_kwargs(func): ...
def get_callable_argspec(fn, no_self: bool = ..., _is_init: bool = ...): ...
def format_argspec_plus(fn, grouped: bool = ...): ...
def format_argspec_init(method, grouped: bool = ...): ...
def create_proxy_methods(
    target_cls, target_cls_sphinx_name, proxy_cls_sphinx_name, classmethods=..., methods=..., attributes=...
): ...
def getargspec_init(method): ...
def unbound_method_to_callable(func_or_cls): ...
def generic_repr(obj, additional_kw=..., to_inspect: Any | None = ..., omit_kwarg=...): ...

class portable_instancemethod:
    target: Any
    name: Any
    kwargs: Any
    def __init__(self, meth, kwargs=...) -> None: ...
    def __call__(self, *arg, **kw): ...

def class_hierarchy(cls): ...
def iterate_attributes(cls) -> None: ...
def monkeypatch_proxied_specials(
    into_cls, from_cls, skip: Any | None = ..., only: Any | None = ..., name: str = ..., from_instance: Any | None = ...
) -> None: ...
def methods_equivalent(meth1, meth2): ...
def as_interface(obj, cls: Any | None = ..., methods: Any | None = ..., required: Any | None = ...): ...

class memoized_property(Generic[_R]):
    fget: Callable[..., _R]
    __doc__: str
    __name__: str
    def __init__(self, fget: Callable[..., _R], doc: str | None = ...) -> None: ...
    @overload
    def __get__(self: Self, obj: None, cls: object) -> Self: ...
    @overload
    def __get__(self, obj: object, cls: object) -> _R: ...
    @classmethod
    def reset(cls, obj: object, name: str) -> None: ...

def memoized_instancemethod(fn): ...

class HasMemoized:
    class memoized_attribute(Generic[_R]):
        fget: Callable[..., _R]
        __doc__: str
        __name__: str
        def __init__(self, fget: Callable[..., _R], doc: str | None = ...) -> None: ...
        @overload
        def __get__(self: Self, obj: None, cls: object) -> Self: ...
        @overload
        def __get__(self, obj: object, cls: object) -> _R: ...
    @classmethod
    def memoized_instancemethod(cls, fn): ...

class MemoizedSlots:
    def __getattr__(self, key): ...

def asbool(obj): ...
def bool_or_str(*text): ...
def asint(value): ...
def coerce_kw_type(kw, key, type_, flexi_bool: bool = ..., dest: Any | None = ...) -> None: ...
def constructor_key(obj, cls): ...
def constructor_copy(obj, cls, *args, **kw): ...
def counter(): ...
def duck_type_collection(specimen, default: Any | None = ...): ...
def assert_arg_type(arg, argtype, name): ...
def dictlike_iteritems(dictlike): ...

class classproperty(property):
    __doc__: Any
    def __init__(self, fget, *arg, **kw) -> None: ...
    def __get__(self, self_, cls): ...

class hybridproperty(Generic[_R]):
    func: Callable[..., _R]
    clslevel: Callable[..., _R]
    def __init__(self, func: Callable[..., _R]) -> None: ...
    @overload
    def __get__(self, instance: None, owner: Any) -> _R: ...
    @overload
    def __get__(self, instance: object, owner: object) -> _R: ...
    def classlevel(self: Self, func: Callable[..., _R]) -> Self: ...

class hybridmethod:
    func: Any
    clslevel: Any
    def __init__(self, func) -> None: ...
    def __get__(self, instance, owner): ...
    def classlevel(self, func): ...

class _symbol(int):
    def __new__(cls, name, doc: Any | None = ..., canonical: Any | None = ...): ...
    def __reduce__(self): ...

class symbol:
    symbols: Any
    def __new__(cls, name, doc: Any | None = ..., canonical: Any | None = ...): ...
    @classmethod
    def parse_user_argument(cls, arg, choices, name, resolve_symbol_names: bool = ...): ...

def set_creation_order(instance) -> None: ...
def warn_exception(func, *args, **kwargs): ...
def ellipses_string(value, len_: int = ...): ...

class _hash_limit_string(compat.text_type):
    def __new__(cls, value, num, args): ...
    def __hash__(self): ...
    def __eq__(self, other): ...

def warn(msg, code: Any | None = ...) -> None: ...
def warn_limited(msg, args) -> None: ...
def only_once(fn, retry_on_exception): ...
def chop_traceback(tb, exclude_prefix=..., exclude_suffix=...): ...

NoneType: Any

def attrsetter(attrname): ...

class EnsureKWArgType(type):
    def __init__(cls, clsname, bases, clsdict) -> None: ...

def wrap_callable(wrapper, fn): ...
def quoted_token_parser(value): ...
def add_parameter_text(params, text): ...
def inject_docstring_text(doctext, injecttext, pos): ...
def inject_param_text(doctext, inject_params): ...
def repr_tuple_names(names): ...
def has_compiled_ext(): ...
