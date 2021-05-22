---
layout: post
title:  "tensor de faraday"
description: construção do tensor de faraday a partir de analogias com a forma clássica da força de lorentz
img: /img/t_faraday.png
date:   2017-07-21 05:02:41 +0300
tags: física notas
---

No limite clássico a relação entre presença de campos elétricos e magnéticos e a força por eles exercida sobre um corpo eletricamente carregado é descrita pela equação de [força de Lorentz](https://en.wikipedia.org/wiki/Lorentz_force)

$$F=q(E+v \times B)$$

Então é possível encontrar uma "versão relativística" da força de Lorentz. Em geral uma forma análoga seria

$$\frac{dp^\mu}{d\tau}=\frac{q}{c}F_\beta^\mu \eta^\beta$$

onde

- $ x^\mu \equiv (x^0, x^1, x^2, x^3) = (ct, x, y, z) = (ct, x^i) $
- $ u^i = v_{AS}^{i} $, a velocidade de um sistema A em relação a um referencial S
- $\gamma = \gamma_u \equiv \frac{1}{\sqrt{1 - \frac{u^2}{c^2}}}$
- $d\tau = \sqrt{ 1 - \frac{u^2}{c^2} } dt = \frac{dt}{\gamma}$
- $\eta^\mu \equiv (\gamma c, \gamma u^i)$
- $p^\mu = (\frac{E}{c}, m \eta^i) = (m \gamma c, m\gamma, u^i)$
- $\frac{1}{c}$ é uma constante

Pode-se escrever o primeiro termo de forma mais conveniente, primeiro aplicando a regra do produto

$$\frac{dp^\alpha}{d\tau}=\frac{d}{d\tau}m\eta^\alpha=\frac{dm}{d\tau}\eta^\alpha + m\frac{d\eta^\alpha}{d\tau}$$

e daí multiplicando tudo por $\eta_\alpha$

$$\frac{dp^\alpha}{d\tau}\eta_\alpha=\frac{dm}{d\tau}\eta^\alpha\eta_\alpha + m\frac{d\eta^\alpha}{d\tau}\eta_\alpha.$$

Se a massa é invariante por transformações de Lorentz, então

$$\frac{dp^\alpha}{d\tau}\eta_\alpha=m\frac{d\eta^\alpha}{d\tau}\eta_\alpha.$$

Por outro lado:

$$\frac{d}{d\tau}\left( \eta^\alpha \eta_\alpha \right)=\frac{d\eta^\alpha}{d\tau}\eta_\alpha + \eta^\alpha\frac{d\eta_\alpha}{d\tau}=2\frac{d\eta^\alpha}{d\tau}\eta_\alpha,$$

Mas como os objetos estudados são campos eletromagnéticos no vácuo; em todo referencial a velocidade de propagação é igual a $c$, então

$$\eta^2=-c^2 \Rightarrow \frac{d}{d\tau}\eta^2=\frac{d}{d\tau}\left( \eta^\alpha \eta_\alpha \right)=0.$$

Juntando tudo:

$$\frac{dp^\mu}{d\tau}\eta_\mu=m\frac{d\eta^\mu}{d\tau}\eta_\mu=\frac{1}{2}\frac{d}{d\tau}\left( \eta^\mu \eta_\mu \right)=0.$$

Então, da equação inicial, segue que

$$\frac{dp^\mu}{d\tau}\eta_\mu = \frac{q}{c} \boxed{F_\beta^\mu \eta^\beta \eta_\mu = 0}.$$

```
.
.
.
(a ser desenvolvido)
.
.
.
```

É possível usar o tensor métrico

$$g_{\mu\nu}
\equiv
\begin{pmatrix}
-1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1
\end{pmatrix} = g^{\mu\nu}$$

reescrever a equação destacada da seguinte forma

$$F^{\beta \mu} \eta_\beta \eta_\mu=0.$$

Das propriedades dos tensores, algo na forma

$$a_\alpha a_\nu$$

é um tensor chamado simétrico. Então, para essa última igualdade valer sempre é preciso que

$$F^{\beta\mu}$$

seja um tensor antissimetrico. A propriedade especial de um tensor antissimétrico é

$$\chi^{ij}=-\chi^{ji}.$$

Comparando as forças de Lorentz clássica e tensorial

$$F=q(E+v \times B)$$

e

$$\frac{dp^\mu}{d\tau}=\frac{q}{c}F_\beta^\mu \eta^\beta,$$

resta buscar as condições para que as duas sejam iguais. Para isso é conveniente identificar o produto vetorial como

$$(\nabla \times B)_i = \epsilon_{ijk}\partial_j B_k$$

onde $\epsilon^{ijk}$ é o "símbolo de Levi-Civita".

Começando pelos termos da esquerda:

$$\frac{dp^{i}}{d\tau}=\frac{dp^{i}}{\frac{dt}{\gamma} }=\gamma \frac{dp^{i}}{dt}.$$

Então

$$\frac{dp^i}{dt} = q(E^i + \epsilon_{ijk}v^j B^k) \qquad \text{(classico)}$$

$$\frac{dp^i}{d\tau} = \gamma \frac{dp^{i}}{dt} = \frac{q}{c} \left( F^{i}_{\alpha}\eta^{\alpha} \right) = \frac{q}{c} \left( F^{i}_{0}\eta^{0} + F^{i}_{j}\eta^{j} \right), \qquad \text{(relativistico)}$$

daí

$$\not{\gamma} \frac{dp^{i}}{dt} = \frac{q}{\not{c}} F^{i}_{0}\not{\gamma}\not{c} + \frac{q}{c} F^{i}_{j}\not{\gamma}v^{j}.$$

Então comparando as formas clássica e relativística:

$$\boxed{F^{i}_0=E^i}$$

e

$$\boxed{F^{i}_j=c\epsilon^{ijk}B^{k}}.$$

A última equação não está tensorialmente correta. É preciso que os índices "combinem" e nela nota-se que o índice $j$ de $F$ não está na mesma posição que o de $\epsilon$. Novamente usa-se o tensor métrico para "subir os índices":

$$F^{i0}=F^{i}_{0}g^{00}=-E^i$$

e

$$F^{ij}=F^{i}_{\rho}g^{\rho j}=c\epsilon^{ijk}B^{k} \qquad (j \neq 0)$$

um exemplo para perceber melhor o que ocorre na última igualdade é o seguinte:

$$
\begin{aligned}
F^{12} &= F^{1}_{2} g^{12}\\
&= c\epsilon^{12k}B^{k} g^{12}\\
&=c \not{\epsilon^{121}} B^{1} g^{12} + c \not{\epsilon^{122}} B^{2} g^{12} + c\epsilon^{123}B^{3} g^{12}\\
&= c\epsilon^{123}B^{3}.
\end{aligned}
$$

Então, pela antissimetria de $F^{\alpha \beta}$

$$F^{\mu\nu}=\begin{pmatrix}
0 & \mp F^{10} & \mp F^{20} & \mp F^{30}\\
\pm F^{10} & 0 & \mp F^{21} & \mp F^{31}\\
\pm F^{20} & \pm F^{21} & 0 & \mp F^{32}\\
\pm F^{30} & \pm F^{31} & \pm F^{32} & 0
\end{pmatrix}$$

Como $F^{i0}=-E^i$, então

$$F^{\mu\nu}=\begin{pmatrix}
0 & E_x & E_y & E_z\\
-E_x & 0 & \mp F^{21} & \mp F^{31}\\
-E_y & \pm F^{21} & 0 & \mp F^{32}\\
-E_z & \pm F^{31} & \pm F^{32} & 0
\end{pmatrix}$$

Por $F^{ij}=c\epsilon^{ijk}B^{k}$, tendo em mente as propriedades do símbolo de levi-civita

$$\boxed{F^{\mu\nu}=\begin{pmatrix}
0 & E_x & E_y & E_z\\
-E_x & 0 & cB_z & -cB_y\\
-E_y & -cB_z & 0 & cB_x\\
-E_z & cB_y & -cB_x & 0
\end{pmatrix} }.$$

Então se o tensor de campo $F^{\mu\nu}$ tiver a forma da equação anterior, a forma relativística da força de Lorentz é análoga à forma clássica. É possível partir desse ponto e desenvolver alguns outros resultados a fim de reescrever as equações de Maxwell em forma tensorial.

```
(. . .)
```
