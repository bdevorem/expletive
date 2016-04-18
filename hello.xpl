* Hello.xpl
* Prints "helloworld"

@|?h {1 2 3 4 5 6 7 8 a b c d e f g h i j k l m n o p q r s t u v w x y z}
h@|+ {#}
r#|3 {1} {aeiou}
r#|3 {2} {xyz}
r#|3 {3} {klm}
r#|3 {5} {opq}
r#|3 {4} {hij}
r#|3 {x} {yy#}
r#|3 {z} {h}
r#|3 {m} {m}
r#|3 {e} {e}
r#|3 {6} {ooll}
r#|3 {o} {l}
r#|3 {l} {ow}
r#|3 {7} {ab}
r#|3 {b} {bcd}
r#|3 {a} {or}
r#|3 {8} {1234567}
r#|3 {y} {ld}
n?#+ {23126578}

*23126578
*xyzaeiouoollab
*yy#hellowor
*#helloworld
