# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_TestA_swig', [dirname(__file__)])
        except ImportError:
            import _TestA_swig
            return _TestA_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_TestA_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _TestA_swig = swig_import_helper()
    del swig_import_helper
else:
    import _TestA_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
  """high_res_timer_now() -> gr::high_res_timer_type"""
  return _TestA_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
  """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
  return _TestA_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
  """high_res_timer_tps() -> gr::high_res_timer_type"""
  return _TestA_swig.high_res_timer_tps()

def high_res_timer_epoch():
  """high_res_timer_epoch() -> gr::high_res_timer_type"""
  return _TestA_swig.high_res_timer_epoch()
class my_qpsk_demod_cb(object):
    """<+description of block+>"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def make(*args, **kwargs):
        """
        make(bool gray_code) -> my_qpsk_demod_cb_sptr

        Return a shared_ptr to a new instance of TestA::my_qpsk_demod_cb.

        To avoid accidental use of raw pointers, TestA::my_qpsk_demod_cb's constructor is in a private implementation class. TestA::my_qpsk_demod_cb::make is the public interface for creating new instances.

        Params: (gray_code)
        """
        return _TestA_swig.my_qpsk_demod_cb_make(*args, **kwargs)

    make = staticmethod(make)
    __swig_destroy__ = _TestA_swig.delete_my_qpsk_demod_cb
    __del__ = lambda self : None;
my_qpsk_demod_cb_swigregister = _TestA_swig.my_qpsk_demod_cb_swigregister
my_qpsk_demod_cb_swigregister(my_qpsk_demod_cb)

def my_qpsk_demod_cb_make(*args, **kwargs):
  """
    my_qpsk_demod_cb_make(bool gray_code) -> my_qpsk_demod_cb_sptr

    Return a shared_ptr to a new instance of TestA::my_qpsk_demod_cb.

    To avoid accidental use of raw pointers, TestA::my_qpsk_demod_cb's constructor is in a private implementation class. TestA::my_qpsk_demod_cb::make is the public interface for creating new instances.

    Params: (gray_code)
    """
  return _TestA_swig.my_qpsk_demod_cb_make(*args, **kwargs)

class my_qpsk_demod_cb_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::TestA::my_qpsk_demod_cb)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(boost::shared_ptr<(gr::TestA::my_qpsk_demod_cb)> self) -> my_qpsk_demod_cb_sptr
        __init__(boost::shared_ptr<(gr::TestA::my_qpsk_demod_cb)> self, my_qpsk_demod_cb p) -> my_qpsk_demod_cb_sptr
        """
        this = _TestA_swig.new_my_qpsk_demod_cb_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(my_qpsk_demod_cb_sptr self) -> my_qpsk_demod_cb"""
        return _TestA_swig.my_qpsk_demod_cb_sptr___deref__(self)

    __swig_destroy__ = _TestA_swig.delete_my_qpsk_demod_cb_sptr
    __del__ = lambda self : None;
    def make(self, *args, **kwargs):
        """
        make(my_qpsk_demod_cb_sptr self, bool gray_code) -> my_qpsk_demod_cb_sptr

        Return a shared_ptr to a new instance of TestA::my_qpsk_demod_cb.

        To avoid accidental use of raw pointers, TestA::my_qpsk_demod_cb's constructor is in a private implementation class. TestA::my_qpsk_demod_cb::make is the public interface for creating new instances.

        Params: (gray_code)
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_make(self, *args, **kwargs)

    def history(self):
        """history(my_qpsk_demod_cb_sptr self) -> unsigned int"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_history(self)

    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(my_qpsk_demod_cb_sptr self, int which, int delay)
        declare_sample_delay(my_qpsk_demod_cb_sptr self, unsigned int delay)
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_declare_sample_delay(self, *args)

    def sample_delay(self, *args, **kwargs):
        """sample_delay(my_qpsk_demod_cb_sptr self, int which) -> unsigned int"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_sample_delay(self, *args, **kwargs)

    def output_multiple(self):
        """output_multiple(my_qpsk_demod_cb_sptr self) -> int"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(my_qpsk_demod_cb_sptr self) -> double"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_relative_rate(self)

    def start(self):
        """start(my_qpsk_demod_cb_sptr self) -> bool"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_start(self)

    def stop(self):
        """stop(my_qpsk_demod_cb_sptr self) -> bool"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(my_qpsk_demod_cb_sptr self, unsigned int which_input) -> uint64_t"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(my_qpsk_demod_cb_sptr self, unsigned int which_output) -> uint64_t"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_nitems_written(self, *args, **kwargs)

    def max_noutput_items(self):
        """max_noutput_items(my_qpsk_demod_cb_sptr self) -> int"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, *args, **kwargs):
        """set_max_noutput_items(my_qpsk_demod_cb_sptr self, int m)"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_set_max_noutput_items(self, *args, **kwargs)

    def unset_max_noutput_items(self):
        """unset_max_noutput_items(my_qpsk_demod_cb_sptr self)"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(my_qpsk_demod_cb_sptr self) -> bool"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_is_set_max_noutput_items(self)

    def set_min_noutput_items(self, *args, **kwargs):
        """set_min_noutput_items(my_qpsk_demod_cb_sptr self, int m)"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_set_min_noutput_items(self, *args, **kwargs)

    def min_noutput_items(self):
        """min_noutput_items(my_qpsk_demod_cb_sptr self) -> int"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_min_noutput_items(self)

    def max_output_buffer(self, *args, **kwargs):
        """max_output_buffer(my_qpsk_demod_cb_sptr self, int i) -> long"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_max_output_buffer(self, *args, **kwargs)

    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(my_qpsk_demod_cb_sptr self, long max_output_buffer)
        set_max_output_buffer(my_qpsk_demod_cb_sptr self, int port, long max_output_buffer)
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, *args, **kwargs):
        """min_output_buffer(my_qpsk_demod_cb_sptr self, int i) -> long"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_min_output_buffer(self, *args, **kwargs)

    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(my_qpsk_demod_cb_sptr self, long min_output_buffer)
        set_min_output_buffer(my_qpsk_demod_cb_sptr self, int port, long min_output_buffer)
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self):
        """pc_noutput_items(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_noutput_items(self)

    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_noutput_items_avg(self)

    def pc_noutput_items_var(self):
        """pc_noutput_items_var(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self):
        """pc_nproduced(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_nproduced(self)

    def pc_nproduced_avg(self):
        """pc_nproduced_avg(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_nproduced_avg(self)

    def pc_nproduced_var(self):
        """pc_nproduced_var(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(my_qpsk_demod_cb_sptr self, int which) -> float
        pc_input_buffers_full(my_qpsk_demod_cb_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(my_qpsk_demod_cb_sptr self, int which) -> float
        pc_input_buffers_full_avg(my_qpsk_demod_cb_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_input_buffers_full_avg(self, *args)

    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(my_qpsk_demod_cb_sptr self, int which) -> float
        pc_input_buffers_full_var(my_qpsk_demod_cb_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(my_qpsk_demod_cb_sptr self, int which) -> float
        pc_output_buffers_full(my_qpsk_demod_cb_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(my_qpsk_demod_cb_sptr self, int which) -> float
        pc_output_buffers_full_avg(my_qpsk_demod_cb_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_output_buffers_full_avg(self, *args)

    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(my_qpsk_demod_cb_sptr self, int which) -> float
        pc_output_buffers_full_var(my_qpsk_demod_cb_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self):
        """pc_work_time(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_work_time(self)

    def pc_work_time_avg(self):
        """pc_work_time_avg(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_work_time_avg(self)

    def pc_work_time_var(self):
        """pc_work_time_var(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_work_time_var(self)

    def pc_work_time_total(self):
        """pc_work_time_total(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_work_time_total(self)

    def pc_throughput_avg(self):
        """pc_throughput_avg(my_qpsk_demod_cb_sptr self) -> float"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_pc_throughput_avg(self)

    def set_processor_affinity(self, *args, **kwargs):
        """set_processor_affinity(my_qpsk_demod_cb_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_set_processor_affinity(self, *args, **kwargs)

    def unset_processor_affinity(self):
        """unset_processor_affinity(my_qpsk_demod_cb_sptr self)"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_unset_processor_affinity(self)

    def processor_affinity(self):
        """processor_affinity(my_qpsk_demod_cb_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_processor_affinity(self)

    def active_thread_priority(self):
        """active_thread_priority(my_qpsk_demod_cb_sptr self) -> int"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_active_thread_priority(self)

    def thread_priority(self):
        """thread_priority(my_qpsk_demod_cb_sptr self) -> int"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_thread_priority(self)

    def set_thread_priority(self, *args, **kwargs):
        """set_thread_priority(my_qpsk_demod_cb_sptr self, int priority) -> int"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_set_thread_priority(self, *args, **kwargs)

    def name(self):
        """name(my_qpsk_demod_cb_sptr self) -> std::string"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_name(self)

    def symbol_name(self):
        """symbol_name(my_qpsk_demod_cb_sptr self) -> std::string"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_symbol_name(self)

    def input_signature(self):
        """input_signature(my_qpsk_demod_cb_sptr self) -> io_signature_sptr"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(my_qpsk_demod_cb_sptr self) -> io_signature_sptr"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(my_qpsk_demod_cb_sptr self) -> long"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(my_qpsk_demod_cb_sptr self) -> basic_block_sptr"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(my_qpsk_demod_cb_sptr self, int ninputs, int noutputs) -> bool"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_check_topology(self, *args, **kwargs)

    def alias(self):
        """alias(my_qpsk_demod_cb_sptr self) -> std::string"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_alias(self)

    def set_block_alias(self, *args, **kwargs):
        """set_block_alias(my_qpsk_demod_cb_sptr self, std::string name)"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_set_block_alias(self, *args, **kwargs)

    def _post(self, *args, **kwargs):
        """_post(my_qpsk_demod_cb_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _TestA_swig.my_qpsk_demod_cb_sptr__post(self, *args, **kwargs)

    def message_ports_in(self):
        """message_ports_in(my_qpsk_demod_cb_sptr self) -> swig_int_ptr"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_message_ports_in(self)

    def message_ports_out(self):
        """message_ports_out(my_qpsk_demod_cb_sptr self) -> swig_int_ptr"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_message_ports_out(self)

    def message_subscribers(self, *args, **kwargs):
        """message_subscribers(my_qpsk_demod_cb_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _TestA_swig.my_qpsk_demod_cb_sptr_message_subscribers(self, *args, **kwargs)

my_qpsk_demod_cb_sptr_swigregister = _TestA_swig.my_qpsk_demod_cb_sptr_swigregister
my_qpsk_demod_cb_sptr_swigregister(my_qpsk_demod_cb_sptr)

my_qpsk_demod_cb_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
my_qpsk_demod_cb = my_qpsk_demod_cb.make;

class cleanslate(object):
    """Proxy of C++ gr::TestA::cleanslate class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def make(*args, **kwargs):
        """make(bool test, int foo) -> cleanslate_sptr"""
        return _TestA_swig.cleanslate_make(*args, **kwargs)

    make = staticmethod(make)
    __swig_destroy__ = _TestA_swig.delete_cleanslate
    __del__ = lambda self : None;
cleanslate_swigregister = _TestA_swig.cleanslate_swigregister
cleanslate_swigregister(cleanslate)

def cleanslate_make(*args, **kwargs):
  """cleanslate_make(bool test, int foo) -> cleanslate_sptr"""
  return _TestA_swig.cleanslate_make(*args, **kwargs)

class cleanslate_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::TestA::cleanslate)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(boost::shared_ptr<(gr::TestA::cleanslate)> self) -> cleanslate_sptr
        __init__(boost::shared_ptr<(gr::TestA::cleanslate)> self, cleanslate p) -> cleanslate_sptr
        """
        this = _TestA_swig.new_cleanslate_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(cleanslate_sptr self) -> cleanslate"""
        return _TestA_swig.cleanslate_sptr___deref__(self)

    __swig_destroy__ = _TestA_swig.delete_cleanslate_sptr
    __del__ = lambda self : None;
    def make(self, *args, **kwargs):
        """make(cleanslate_sptr self, bool test, int foo) -> cleanslate_sptr"""
        return _TestA_swig.cleanslate_sptr_make(self, *args, **kwargs)

    def history(self):
        """history(cleanslate_sptr self) -> unsigned int"""
        return _TestA_swig.cleanslate_sptr_history(self)

    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(cleanslate_sptr self, int which, int delay)
        declare_sample_delay(cleanslate_sptr self, unsigned int delay)
        """
        return _TestA_swig.cleanslate_sptr_declare_sample_delay(self, *args)

    def sample_delay(self, *args, **kwargs):
        """sample_delay(cleanslate_sptr self, int which) -> unsigned int"""
        return _TestA_swig.cleanslate_sptr_sample_delay(self, *args, **kwargs)

    def output_multiple(self):
        """output_multiple(cleanslate_sptr self) -> int"""
        return _TestA_swig.cleanslate_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(cleanslate_sptr self) -> double"""
        return _TestA_swig.cleanslate_sptr_relative_rate(self)

    def start(self):
        """start(cleanslate_sptr self) -> bool"""
        return _TestA_swig.cleanslate_sptr_start(self)

    def stop(self):
        """stop(cleanslate_sptr self) -> bool"""
        return _TestA_swig.cleanslate_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(cleanslate_sptr self, unsigned int which_input) -> uint64_t"""
        return _TestA_swig.cleanslate_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(cleanslate_sptr self, unsigned int which_output) -> uint64_t"""
        return _TestA_swig.cleanslate_sptr_nitems_written(self, *args, **kwargs)

    def max_noutput_items(self):
        """max_noutput_items(cleanslate_sptr self) -> int"""
        return _TestA_swig.cleanslate_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, *args, **kwargs):
        """set_max_noutput_items(cleanslate_sptr self, int m)"""
        return _TestA_swig.cleanslate_sptr_set_max_noutput_items(self, *args, **kwargs)

    def unset_max_noutput_items(self):
        """unset_max_noutput_items(cleanslate_sptr self)"""
        return _TestA_swig.cleanslate_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(cleanslate_sptr self) -> bool"""
        return _TestA_swig.cleanslate_sptr_is_set_max_noutput_items(self)

    def set_min_noutput_items(self, *args, **kwargs):
        """set_min_noutput_items(cleanslate_sptr self, int m)"""
        return _TestA_swig.cleanslate_sptr_set_min_noutput_items(self, *args, **kwargs)

    def min_noutput_items(self):
        """min_noutput_items(cleanslate_sptr self) -> int"""
        return _TestA_swig.cleanslate_sptr_min_noutput_items(self)

    def max_output_buffer(self, *args, **kwargs):
        """max_output_buffer(cleanslate_sptr self, int i) -> long"""
        return _TestA_swig.cleanslate_sptr_max_output_buffer(self, *args, **kwargs)

    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(cleanslate_sptr self, long max_output_buffer)
        set_max_output_buffer(cleanslate_sptr self, int port, long max_output_buffer)
        """
        return _TestA_swig.cleanslate_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, *args, **kwargs):
        """min_output_buffer(cleanslate_sptr self, int i) -> long"""
        return _TestA_swig.cleanslate_sptr_min_output_buffer(self, *args, **kwargs)

    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(cleanslate_sptr self, long min_output_buffer)
        set_min_output_buffer(cleanslate_sptr self, int port, long min_output_buffer)
        """
        return _TestA_swig.cleanslate_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self):
        """pc_noutput_items(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_noutput_items(self)

    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_noutput_items_avg(self)

    def pc_noutput_items_var(self):
        """pc_noutput_items_var(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self):
        """pc_nproduced(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_nproduced(self)

    def pc_nproduced_avg(self):
        """pc_nproduced_avg(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_nproduced_avg(self)

    def pc_nproduced_var(self):
        """pc_nproduced_var(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(cleanslate_sptr self, int which) -> float
        pc_input_buffers_full(cleanslate_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.cleanslate_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(cleanslate_sptr self, int which) -> float
        pc_input_buffers_full_avg(cleanslate_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.cleanslate_sptr_pc_input_buffers_full_avg(self, *args)

    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(cleanslate_sptr self, int which) -> float
        pc_input_buffers_full_var(cleanslate_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.cleanslate_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(cleanslate_sptr self, int which) -> float
        pc_output_buffers_full(cleanslate_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.cleanslate_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(cleanslate_sptr self, int which) -> float
        pc_output_buffers_full_avg(cleanslate_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.cleanslate_sptr_pc_output_buffers_full_avg(self, *args)

    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(cleanslate_sptr self, int which) -> float
        pc_output_buffers_full_var(cleanslate_sptr self) -> pmt_vector_float
        """
        return _TestA_swig.cleanslate_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self):
        """pc_work_time(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_work_time(self)

    def pc_work_time_avg(self):
        """pc_work_time_avg(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_work_time_avg(self)

    def pc_work_time_var(self):
        """pc_work_time_var(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_work_time_var(self)

    def pc_work_time_total(self):
        """pc_work_time_total(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_work_time_total(self)

    def pc_throughput_avg(self):
        """pc_throughput_avg(cleanslate_sptr self) -> float"""
        return _TestA_swig.cleanslate_sptr_pc_throughput_avg(self)

    def set_processor_affinity(self, *args, **kwargs):
        """set_processor_affinity(cleanslate_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _TestA_swig.cleanslate_sptr_set_processor_affinity(self, *args, **kwargs)

    def unset_processor_affinity(self):
        """unset_processor_affinity(cleanslate_sptr self)"""
        return _TestA_swig.cleanslate_sptr_unset_processor_affinity(self)

    def processor_affinity(self):
        """processor_affinity(cleanslate_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _TestA_swig.cleanslate_sptr_processor_affinity(self)

    def active_thread_priority(self):
        """active_thread_priority(cleanslate_sptr self) -> int"""
        return _TestA_swig.cleanslate_sptr_active_thread_priority(self)

    def thread_priority(self):
        """thread_priority(cleanslate_sptr self) -> int"""
        return _TestA_swig.cleanslate_sptr_thread_priority(self)

    def set_thread_priority(self, *args, **kwargs):
        """set_thread_priority(cleanslate_sptr self, int priority) -> int"""
        return _TestA_swig.cleanslate_sptr_set_thread_priority(self, *args, **kwargs)

    def name(self):
        """name(cleanslate_sptr self) -> std::string"""
        return _TestA_swig.cleanslate_sptr_name(self)

    def symbol_name(self):
        """symbol_name(cleanslate_sptr self) -> std::string"""
        return _TestA_swig.cleanslate_sptr_symbol_name(self)

    def input_signature(self):
        """input_signature(cleanslate_sptr self) -> io_signature_sptr"""
        return _TestA_swig.cleanslate_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(cleanslate_sptr self) -> io_signature_sptr"""
        return _TestA_swig.cleanslate_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(cleanslate_sptr self) -> long"""
        return _TestA_swig.cleanslate_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(cleanslate_sptr self) -> basic_block_sptr"""
        return _TestA_swig.cleanslate_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(cleanslate_sptr self, int ninputs, int noutputs) -> bool"""
        return _TestA_swig.cleanslate_sptr_check_topology(self, *args, **kwargs)

    def alias(self):
        """alias(cleanslate_sptr self) -> std::string"""
        return _TestA_swig.cleanslate_sptr_alias(self)

    def set_block_alias(self, *args, **kwargs):
        """set_block_alias(cleanslate_sptr self, std::string name)"""
        return _TestA_swig.cleanslate_sptr_set_block_alias(self, *args, **kwargs)

    def _post(self, *args, **kwargs):
        """_post(cleanslate_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _TestA_swig.cleanslate_sptr__post(self, *args, **kwargs)

    def message_ports_in(self):
        """message_ports_in(cleanslate_sptr self) -> swig_int_ptr"""
        return _TestA_swig.cleanslate_sptr_message_ports_in(self)

    def message_ports_out(self):
        """message_ports_out(cleanslate_sptr self) -> swig_int_ptr"""
        return _TestA_swig.cleanslate_sptr_message_ports_out(self)

    def message_subscribers(self, *args, **kwargs):
        """message_subscribers(cleanslate_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _TestA_swig.cleanslate_sptr_message_subscribers(self, *args, **kwargs)

cleanslate_sptr_swigregister = _TestA_swig.cleanslate_sptr_swigregister
cleanslate_sptr_swigregister(cleanslate_sptr)

cleanslate_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
cleanslate = cleanslate.make;



