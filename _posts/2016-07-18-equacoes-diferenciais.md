---
layout: post
title:  "equações diferenciais"
description: anotações sobre equações diferenciais
img: /img/t_mecanica-classica.png
date:   2016-07-18 00:12:42 +0300
tags: física notas
toc: true
---

{% comment %}
<!-- Aqui é Body Builder Ipsum PORRA! É verão o ano todo vem cumpadi. Vem porra! É nóis caraio é trapezera buscando caraio! Tá comigo porra. Aqui nóis constrói fibra, não é água com músculo.
 -->
{% endcomment %} 

**Disclaimer**<br/>Essas anotações são excertos de um texto sobre equações diferenciais escrito em 2016 e publicado para fins de divulgação científica. Agora, 6 anos depois eu não tenho ideia do que eu queria desenvolver ou concluir com ele. Vão-se os conhecimentos, ficam os registros.

<br/><br/>

## equação diferencial exata

_Uma equação diferencial da forma_

$$ I(x,y)dx + J(x,y)dy=0$$

_é exata se existe uma função $\phi(x,y)$ -- chamada função "potencial" -- tal que_

$$
\begin{aligned}
\frac{\partial \phi}{\partial x}&=I(x,y)\\
\frac{\partial \phi}{\partial y}&=J(x,y).
\end{aligned}
$$

Lembrando que, dada uma função $z(x,y)$, o [Teorema de Schwarz](https://pt.wikipedia.org/wiki/Teorema_de_Clairaut-Schwarz#:~:text=Na%20an%C3%A1lise%20matem%C3%A1tica%2C%20o%20teorema,s%C3%A3o%20cont%C3%ADnuas%2C%20ent%C3%A3o%20s%C3%A3o%20iguais.) garante que

$$ \frac{\partial^2 z}{\partial x \partial y}=\frac{\partial^2 z}{\partial y \partial x},$$

_segue que, se a equação diferencial inicial é exata, então_

$$ \frac{\partial I}{\partial y}=\frac{\partial J}{\partial x}.$$

<div markdown="1" class="example">

_Para ilustrar, considere_

$$ \left(\frac{x+y}{1+y^2}\right)y'=-(x+arctan(y)),$$

_e observe que_

$$
\begin{aligned}
\left(\frac{x+y}{1+y^2}\right)y'&=-(x+arctan(y))\\
\left(\frac{x+y}{1+y^2}\right)\frac{dy}{dx}&=-(x+arctan(y))\\
\left(\frac{x+y}{1+y^2}\right)dy\, &+\, (x+arctan(y))dx =0.\\
\end{aligned}
$$

_Lembrando que qualquer equação diferencial linear de primeira ordem pode ser escrita assim, o que não implica que ela é exata. Nesse caso é preciso verificar. Veja que_

$$
\begin{aligned}
I(x,y)&=(x+arctan(y))\\
J(x,y)&=\left(\frac{x+y}{1+y^2}\right).
\end{aligned}
$$

_Então_

$$ \frac{\partial I}{\partial y}=\frac{1}{1+y^2}=\frac{\partial J}{\partial x}$$

_e a função_

$$ \phi(x,y)=\frac{x^2}{2}+x\,arctan(y)+\frac{1}{2}ln(1+y^2)$$

_satisfaz a condição necessária para ser função potencial da equação desse exemplo._

</div>


## equação diferencial linear de primeira ordem

_Além do fato da equação diferencial linear_

$$ y' + p(x)\, y=q(x)$$

_possuir solução geral, ela aparece em dois métodos de resolução, então seria legal saber como encontrar soluções pra ela. Pra isso é conveniente escrevê-la da seguinte forma_

$$ dy + \left[ p(x)y-q(x) \right]dx=0.$$

_Apesar de ser tentador classificar a equação acima como exata, não é possível saber, a princípio, se é ou não.
A ideia por trás da obtenção da solução geral é "forçá-la" a ser exata. Para isso multiplica-se uma função $v(x)$ em ambos os lados da igualdade_

$$ v(x)\left[ p(x)y - q(x) \right]dx + v(x)dy=0$$

_e procura-se as condições que tornam a equação exata. Dessa equação se obtém que_

$$ \int v(x)p(x)ydx - \int v(x)q(x)dx + \int v(x)dy=C_1,$$

_Mas se a equação anterior for exata, vai ser verdade que_

$$ \frac{\partial}{\partial y}\left[ v(x)p(x)y - v(x)q(x) \right]=\frac{\partial}{\partial x}v(x)$$

_Ou seja_

$$
\begin{aligned}
v(x)p(x) &=\frac{dv}{dx}\\
p\,dx &= \frac{dv}{v}
\end{aligned}
$$

_Que leva à_

$$ v(x)=e^{( \int p(x)\,dx )}.$$

_Assim_

$$
\begin{aligned}
\int v(x)p(x)ydx - \int v(x)q(x)dx + \int v(x)dy&=C\\
\int v'(x)ydx - \int v(x)q(x)dx + \int v(x)dy&=C\\
v(x)y - \int v(x)q(x)dx + v(x)y&=C\\
v(x)y - \int v(x)q(x)dx&=K\\
y\,e^{( \int p(x)\,dx )} - \int e^{( \int p(x)\,dx )}q(x)dx&=K
\end{aligned}
$$

_Então_ 

$$\boxed{ y(x) = K\,e^{ -\int p(x)\,dx} + e^{ -\int p(x)\,dx}\int e^{ \int p(x)\,dx }q(x)dx }$$

_é solução da equação diferencial linear._

<div markdown="1" class="example">

_Para ilustrar, considere_

$$ y'-y=e^{2x}.$$

_Nesse caso_

$$
\begin{aligned}
p(x) &=-1\\
q(x) &= e^{2x},
\end{aligned}
$$

_Então_

$$
\begin{aligned}
y(x) &= K\,e^{ -\int p(x)\,dx} + e^{ -\int p(x)\,dx}\int e^{ \int p(x)\,dx }q(x)dx\\
y(x) &= K\,e^{ \int dx} + e^{ \int dx}\int e^{ -\int dx }e^{2x}dx\\
y(x) &= K\,e^{x} + e^{x}\int e^{x}dx\\
y(x) &= K\,e^{x} + e^{2x}\\
\end{aligned}
$$

_é solução da equação diferencial inicial._

</div>

_Nesse ponto, é interessante citar a ideia de operador diferencial._

## operador diferencial

_A maneira como eu entendo operadores é a seguinte: operadores são coisas que você gruda em outras coisas para aplicar alguma regra nelas. Um bom exemplo de operador é o gradiente, $\nabla$, que a grosso modo, no $R^3$, tem a seguinte cara_

$$ \nabla \equiv \left( \frac{\partial}{\partial x}\hat{x} + \frac{\partial}{\partial y}\hat{y} + \frac{\partial}{\partial z}\hat{z}\right).$$

_Assim, dada a função_

$$ f(x,y,z)=cos(xy) + 5z^2x$$

_pode-se aplicar esse operador através de uma espécie de multiplicação, por exemplo_

$$
\begin{aligned}
\nabla f &= \left( \frac{\partial}{\partial x}\hat{x} + \frac{\partial}{\partial y}\hat{y} + \frac{\partial}{\partial z}\hat{z}\right)f\\
\nabla f &= \frac{\partial f}{\partial x}\hat{x} + \frac{\partial f}{\partial y}\hat{y} + \frac{\partial f}{\partial z}\hat{z}\\
\nabla f &= [-sin(xy)y+5z^2]\;\hat{x} + [-sin(xy)x]\;\hat{y} + [10xz]\;\hat{z}\\
\nabla f &= \left(-sin(xy)y+5z^2,\;\; -sin(xy)x,\;\; 10xz\right),
\end{aligned}
$$

_obtendo-se o gradiente de $f$._

_É interessante notar que o gradiente aplicado a uma função escalar resulta em uma função vetorial. É possível "combinar" o nabla $\nabla$ à funções escalares e vetoriais de outras formas de modo a obter outras coisas além do gradiente, como, por exemplo, o divergente, o rotacional e o laplaciano._

_Fica claro então que basta alguma regra associada a algum tipo de objeto matemático para se criar um operador. Além disso essa regra pode ser complicada de se escrever, então do ponto de vista estético o uso de operadores tende a deixar as coisas mais claras._

_Dito tudo isso, segue uma "definição", digamos, do tal operador diferencial:_

$$ D^n_t \equiv \frac{d^n}{dt^n}.$$

_Então a aplicação do operador diferencial $D^n_t$ em uma função escalar resulta na n-ésima derivada da função com respeito à variável $t$._

_Como tudo até aqui tem sido dependente da variável $x$, é conveniente simplificar a coisa para_

$$D^n \equiv \frac{d^n}{dx^n}.$$

_Então na prática é o seguinte:_

$$ D^ny \equiv \frac{d^ny}{dx^n},$$

_Então algo como_

$$ \frac{d^6y}{dx^6}+2\frac{d^5y}{dx^5}-2\frac{d^3}{dx^3}-\frac{dy}{dx}+22y=0$$

_passa a ser escrito como_

$$ (D^6+2D^5-2D^3-D+22)y=0.$$

_Eventualmente pode ser interessante definir $D^6+2D^5-D^3-D+22$ como um certo $L$ de modo que se possa escrever a equação acima como_

$L(y)=0.$

_Então, pra concluir essa primeira parte, seria possível definir $L$ tal que_

$$L=D-1$$

_e aí reescrever aquele exemplo da equação diferencial linear como_

$$ L(y)=e^{2x}.$$

<br/>
<p style="color: red; font-weight: light;"> <i>(não tenho ideia do que esse final anticlimático deveria significar)</i></p> 
<br/>

## equação diferencial de segunda ordem

A equação diferencial de segunda ordem homogênea

$$ y''+ay'+by=0$$

também tem solução geral. Para se chegar nela é interessante estudar separadamente as soluções de cada forma que essa equação assume.

caso 1: $$ a=b=0$$

A solução geral desse caso se obtém por uma sequência de integrações:

$$
\begin{aligned}
y'' &= 0\\
y' &=C_1\\
y &= C_1x + C_2.\\
\end{aligned}
$$

caso 2: $$ a=0$$, $$ b<0$$

Nesse caso um primeiro detalhe é que qualquer número ao quadrado pode ser escrito como um certo $$ -k^2$$. Então

$$
\begin{aligned}
y'' +by&= 0\\
y'' &=-by\\
y'' &= k^2y.\\
\end{aligned}
$$

Nesse ponto não tem jeito, tem que procurar alguma função que satisfaça a igualdade acima. Procurando, pensando e inspecionando um pouco conclui-se que duas funções são soluções dessa equação:

$$ y=e^{kx}$$

e

$$ y=e^{-kx}.$$

O princípio da superposição garante que a combinação linear de soluções de equações diferenciais lineares também são soluções, então a solução geral desse caso é

$$ y=C_1e^{kx}+C_2e^{-kx}.$$

caso 3: $$ a=0$$, $$ b>0$$

Analogamente ao caso anterior, qualquer número positivo pode ser escrito como um certo $$ k^2$$, então

$$
\begin{aligned}
y'' +by&= 0\\
y'' &=-by\\
y'' &= -k^2y.\\
\end{aligned}
$$

Novamente, depois de procurar, pensar e inspecionar conclui-se que

$$ y=cos(kx)$$

e

$$ y=sin(kx)$$

são soluções. Novamente pelo princípio da superposição se obtém a solução geral

$$ y=C_1cos(kx)+C_2sin(kx).$$

caso 4: $$ a\neq 0$$, $$ b\neq0$$

Esse é o caso mais geral. A motivação do raciocínio que conduz até a solução geral é querer reduzir essa forma em uma das três anteriores, já que suas soluções já são conhecidas. Para isso se usa uma variação de uma estratégia recorrente na tentativa de resolução de equações diferenciais como por exemplo

$$ \frac{dy}{dx}=\frac{y-x}{y+x}$$

que é fazer uma substituição do tipo $$ y=ux$$. No caso a escolha será $$ y=uv$$. Dessa substituição segue que

$$
\begin{aligned}
y'&=u'v+uv'\\
y''&=u''v+2u'v'+uv''.
\end{aligned}
$$

Então

$$
\begin{aligned}
y''+ay'+b&=0\\
u''v+2u'v'+uv'' + a(u'v+uv')+buv&=0\\
(v''+av'+bv)u+(2v'+av)u' + vu''&=0.\\
\end{aligned}
$$

Para que a equação acima assuma alguma forma cuja solução seja conhecida é preciso que o termo com $$ u$$ suma. Para isso

$$
\begin{aligned}
2v'&=-av\\
\frac{2}{a} \left( \frac{v'}{v} \right) &= -1\\
\frac{2}{a} ln(v) &= -x + C\\
v &= Ke^{-\frac{ax}{2}}
\end{aligned}
$$

Então qualquer $$ v$$ com essa forma faz o trabalho de eliminar o $$ u'$$. Agora sabe-se que

$$ v'=-\frac{a}{2}v$$

e

$$ v''=\frac{a^2}{4}v,$$

então pode-se reescrever a relação obtida anteriormente da seguinte forma

$$
\begin{aligned}
y''+ay'+b&=0\\
(v''+av'+bv)u+(2v'+av)u' + vu''&=0\\
\left( \frac{a^2v}{4}-\frac{a^2v}{2}+bv \right)u +v''u&=0\\
\left( u''-\frac{4b-a^2}{4}u \right)v&=0
\end{aligned}
$$

Lembrando que $$ v$$ nunca vai ser igual a zero segue que a solução da equação diferencial inicial será

$$ y=e^{-\frac{ax}{2}}u,$$

onde $$ u$$ satisfaz

$$ u''-\frac{4b-a^2}{4}u = 0,$$

que é exatamente a forma estudada nos casos anteriores! Então assim como as soluções depediam do sinal de $$ b$$, agora a natureza da solução da equação diferencial inicial depende do sinal do numerador de

$$ d=\frac{4b-a^2}{4}.$$

A união de tudo que foi dito até agora leva ao seguinte: a solução da equação diferencial

$$ y''+ay'+by=0$$

tem forma

$$ y=e^{-\frac{a}{2}x}\left( C_1 u_1 + C_2 u_2\right)$$

onde a natureza de $$ u_1$$ e $$ u_2$$ é determinada pelo sinal de $$ d$$ de modo que

$$
\begin{aligned}
d=0 & \Rightarrow & u_1&=1 &u_2 &=x &\\
d0 & \Rightarrow & u_1&=cos(kx) &u_2 &=sin(kx)& \;\; (d=k^2)\\
\end{aligned}
$$

A essa altura seria interessante mostrar esse resultado funcionando e geralmente é legal fazer isso através do estudo de circuitos elétricos, mas vou pular essa parte. Qualquer "y'' - 13y' + 7y = 0" no Wolfram Aplha já retorna a solução correta

$$ y(x) = C_1 e^{-\frac{1}{2} \left( \sqrt{141}-13 \right) x}+C_2 e^{\frac{1}{2} \left( 13 + \sqrt{141}\right) x}.
$$

Isso encerra essa segunda parte do passeio. O resto do texto provavelmente terá outras três partes: a próxima tratará do uso desse último resultado na resolução de equações diferenciais de ordem n, a seguinte tratará de alguns métodos de encontrar soluções particulares de equações diferenciais não homogêneas e por último fica o registro de um método envolvendo matrizes.

A SER CONTINUADO...

