__all__ = ['jsaudio']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['s', 'o', 'a', 'r'])
@Js
def PyJsHoisted_s_(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['t', 's', 'e', 'o', 'l', 'i'])
    if Js(True):
        var.put('e', var.get('t').callprop('split', Js('?extra=')).get('1').callprop('split', Js('#')))
        var.put('i', (Js('') if PyJsStrictEq(Js(''),var.get('e').get('1')) else var.get('r')(var.get('e').get('1'))))
        if PyJsComma(var.put('e', var.get('r')(var.get('e').get('0'))),((Js('string')!=var.get('i',throw=False).typeof()) or var.get('e').neg())):
            return var.get('t')
        #for JS loop
        var.put('l', var.put('i', (var.get('i').callprop('split', var.get('String').callprop('fromCharCode', Js(9.0))) if var.get('i') else Js([]))).get('length'))
        while (var.put('l',Js(var.get('l').to_number())-Js(1))+Js(1)):
            if PyJsComma(var.put('o', var.put('s', var.get('i').get(var.get('l')).callprop('split', var.get('String').callprop('fromCharCode', Js(11.0)))).callprop('splice', Js(0.0), Js(1.0), var.get('e')).get('0')),var.get('a').get(var.get('o')).neg()):
                return var.get('t')
            var.put('e', var.get('a').get(var.get('o')).callprop('apply', var.get(u"null"), var.get('s')))
        
        if (var.get('e') and PyJsStrictEq(Js('http'),var.get('e').callprop('substr', Js(0.0), Js(4.0)))):
            return var.get('e')
    return var.get('t')
PyJsHoisted_s_.func_name = 's'
var.put('s', PyJsHoisted_s_)
@Js
def PyJsHoisted_r_(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 't', 's', 'e', 'i', 'r'])
    if (var.get('t').neg() or ((var.get('t').get('length')%Js(4.0))==Js(1.0))):
        return Js(1.0).neg()
    #for JS loop
    var.put('a', Js(0.0))
    var.put('s', Js(0.0))
    var.put('r', Js(''))
    while var.put('i', var.get('t').callprop('charAt', (var.put('s',Js(var.get('s').to_number())+Js(1))-Js(1)))):
        (((~var.put('i', var.get('o').callprop('indexOf', var.get('i')))) and PyJsComma(var.put('e', (((Js(64.0)*var.get('e'))+var.get('i')) if (var.get('a')%Js(4.0)) else var.get('i'))),((var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))%Js(4.0)))) and var.put('r', var.get('String').callprop('fromCharCode', (Js(255.0)&(var.get('e')>>(((-Js(2.0))*var.get('a'))&Js(6.0))))), '+'))
    
    return var.get('r')
PyJsHoisted_r_.func_name = 'r'
var.put('r', PyJsHoisted_r_)
var.put('o', Js('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN0PQRSTUVWXYZO123456789+/='))
@Js
def PyJs_anonymous_1_(t, this, arguments, var=var):
    var = Scope({'t':t, 'this':this, 'arguments':arguments}, var)
    var.registers(['t'])
    return var.get('t').callprop('split', Js('')).callprop('reverse').callprop('join', Js(''))
PyJs_anonymous_1_._set_name('anonymous')
@Js
def PyJs_anonymous_2_(t, e, this, arguments, var=var):
    var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 't', 's', 'e', 'i'])
    var.put('t', var.get('t').callprop('split', Js('')))
    #for JS loop
    var.put('a', (var.get('o')+var.get('o')))
    var.put('s', var.get('t').get('length'))
    while (var.put('s',Js(var.get('s').to_number())-Js(1))+Js(1)):
        ((~var.put('i', var.get('a').callprop('indexOf', var.get('t').get(var.get('s'))))) and var.get('t').put(var.get('s'), var.get('a').callprop('substr', (var.get('i')-var.get('e')), Js(1.0))))
    
    return var.get('t').callprop('join', Js(''))
PyJs_anonymous_2_._set_name('anonymous')
@Js
def PyJs_anonymous_3_(t, e, this, arguments, var=var):
    var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 't', 'e', 'o', 'i'])
    var.put('i', var.get('t').get('length'))
    if var.get('i'):
        @Js
        def PyJs_anonymous_4_(t, e, this, arguments, var=var):
            var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
            var.registers(['a', 't', 'e', 'o', 'i'])
            var.put('i', var.get('t').get('length'))
            var.put('o', Js([]))
            if var.get('i'):
                var.put('a', var.get('i'))
                #for JS loop
                var.put('e', var.get('Math').callprop('abs', var.get('e')))
                while (var.put('a',Js(var.get('a').to_number())-Js(1))+Js(1)):
                    PyJsComma(var.put('e', (((var.get('i')*(var.get('a')+Js(1.0)))^(var.get('e')+var.get('a')))%var.get('i'))),var.get('o').put(var.get('a'), var.get('e')))
                
            return var.get('o')
        PyJs_anonymous_4_._set_name('anonymous')
        var.put('o', PyJs_anonymous_4_(var.get('t'), var.get('e')))
        var.put('a', Js(0.0))
        #for JS loop
        var.put('t', var.get('t').callprop('split', Js('')))
        while (var.put('a',Js(var.get('a').to_number())+Js(1))<var.get('i')):
            var.get('t').put(var.get('a'), var.get('t').callprop('splice', var.get('o').get(((var.get('i')-Js(1.0))-var.get('a'))), Js(1.0), var.get('t').get(var.get('a'))).get('0'))
        
        var.put('t', var.get('t').callprop('join', Js('')))
    return var.get('t')
PyJs_anonymous_3_._set_name('anonymous')
@Js
def PyJs_anonymous_5_(t, e, this, arguments, var=var):
    var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['e', 't'])
    return var.get('a').callprop('s', var.get('t'), (var.get('e')^Js(138308279.0)))
PyJs_anonymous_5_._set_name('anonymous')
@Js
def PyJs_anonymous_6_(t, e, this, arguments, var=var):
    var = Scope({'t':t, 'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'e', 't'])
    var.put('i', Js([]))
    @Js
    def PyJs_anonymous_7_(t, o, this, arguments, var=var):
        var = Scope({'t':t, 'o':o, 'this':this, 'arguments':arguments}, var)
        var.registers(['o', 't'])
        var.get('i').callprop('push', var.get('String').callprop('fromCharCode', (var.get('o').callprop('charCodeAt', Js(0.0))^var.get('e'))))
    PyJs_anonymous_7_._set_name('anonymous')
    return PyJsComma(PyJsComma(var.put('e', var.get('e').callprop('charCodeAt', Js(0.0))),var.get('each')(var.get('t').callprop('split', Js('')), PyJs_anonymous_7_)),var.get('i').callprop('join', Js('')))
PyJs_anonymous_6_._set_name('anonymous')
PyJs_Object_0_ = Js({'v':PyJs_anonymous_1_,'r':PyJs_anonymous_2_,'s':PyJs_anonymous_3_,'i':PyJs_anonymous_5_,'x':PyJs_anonymous_6_})
var.put('a', PyJs_Object_0_)
pass
pass
var.put('t', Js('https://vk.com/mp3/audio_api_unavailable.mp3?extra=nZ9WquDJuO1Rze5Tsc4WwtD3tOrAy3vItvuXAwGUtwfLmwm3z3rOBJrjzZvRA2vOzLDXswj2m2vHztzhsfm5yxjklLnKAfftCuXMBZzjBhzSouWZzumXAtfYDhbRAg5RzwnemhKXtZnbx1jKExHOAKT5ptDYsMO3sgLZwt0Vz3v1Cg9PytzRAuv1Cc9dyxHewNHSzgnYC29nmdDTtdrLthu4DI1RmhzVDuTmAJvYAMLoAhv4l2zKDhy5vfHnC2fZxY9HlxvjnNq5zv04#AqS4nZG'))
var.get('console').callprop('log', var.get('s')(var.get('t')))


# Add lib to the module scope
jsaudio = var.to_python()