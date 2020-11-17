var o = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN0PQRSTUVWXYZO123456789+/="
      , a = {
        v: function(t) {
            return t.split("").reverse().join("")
        },
        r: function(t, e) {
            t = t.split("");
            for (var i, a = o + o, s = t.length; s--; )
                ~(i = a.indexOf(t[s])) && (t[s] = a.substr(i - e, 1));
            return t.join("")
        },
        s: function(t, e) {
            var i = t.length;
            if (i) {
                var o = function(t, e) {
                    var i = t.length
                      , o = [];
                    if (i) {
                        var a = i;
                        for (e = Math.abs(e); a--; )
                            e = (i * (a + 1) ^ e + a) % i,
                            o[a] = e
                    }
                    return o
                }(t, e)
                  , a = 0;
                for (t = t.split(""); ++a < i; )
                    t[a] = t.splice(o[i - 1 - a], 1, t[a])[0];
                t = t.join("")
            }
            return t
        },
        i: function(t, e) {
            return a.s(t, e ^ 138308279)
        },
        x: function(t, e) {
            var i = [];
            return e = e.charCodeAt(0),
            each(t.split(""), function(t, o) {
                i.push(String.fromCharCode(o.charCodeAt(0) ^ e))
            }),
            i.join("")
        }
    };
function s(t) {
        if (true) {
            var e = t.split("?extra=")[1].split("#")
              , i = "" === e[1] ? "" : r(e[1]);
            if (e = r(e[0]),
            "string" != typeof i || !e)
                return t;
            for (var o, s, l = (i = i ? i.split(String.fromCharCode(9)) : []).length; l--; ) {
                if (o = (s = i[l].split(String.fromCharCode(11))).splice(0, 1, e)[0],
                !a[o])
                    return t;
                e = a[o].apply(null, s)
            }
            if (e && "http" === e.substr(0, 4))
                return e
        }
        return t
    }
    function r(t) {
        if (!t || t.length % 4 == 1)
            return !1;
        for (var e, i, a = 0, s = 0, r = ""; i = t.charAt(s++); )
            ~(i = o.indexOf(i)) && (e = a % 4 ? 64 * e + i : i,
            a++ % 4) && (r += String.fromCharCode(255 & e >> (-2 * a & 6)));
        return r
    }
console.log(s(process.argv[2]))