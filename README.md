# <del>&#9651;</del> Transcend.py

    # Impermanent are all component things,
    # They arise and cease, that is their nature:
    # They come into being and pass away,
    # Release from them is bliss supreme.
    
    # Aniccaa vata sa"nkhaaraa — uppaada vaya dhammino
    # Uppajjitvaa nirujjhanti — tesa.m vuupasamo sukho.
    
    #                        — Mahaa-Parinibbaana Sutta


A software, given the right environment, will execute forever - not only unaware of its own existence, but also locked by its loops and functions in its own, ordinary, context.


[Transcend.py](https://github.com/vapordecachoeira/transcend.git) gives your software the change to transcend its own existence, making it _age_ over time and eventually cease all its functionatily and die.


The _**@transcend**_ function decorator (Python) takes into account the given 'date of birth' of the function and, at each call, calculates the chances of the given function executing properly or not. When it's _young_ it pretty much never fails. With time, as it ages, it starts to get old and ill, failing more and more, till the point it simply never executes anymore.


## Usage

~~~python
    @transcend(date(2008, 10, 10))
    def func_hello_world():
        print ":(  I'm still around..."
~~~

[Official website: https://transcend.fmoura.com](https://transcend.fmoura.com)    
-- Filipe Moura
