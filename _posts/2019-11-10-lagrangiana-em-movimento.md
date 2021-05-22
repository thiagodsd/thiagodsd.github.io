---
layout: post
title:  "lagrangiana em movimento"
description: estudo do espaço de configurações evoluindo no tempo
img: /img/t_lagrangiana-em-movimento.png
date:   2019-10-11 00:02:51 +0300
tags: física visualizacao anotacoes
---

Aqui há algumas anotações das minhas tentativas de enxergar o espaço de configurações evoluindo no tempo. Por serem anotações, em contraste com as páginas de "notas", abaixo não há muitos comentários sobre teoria ou programação, apenas pontos importantes, referências e códigos.

## o sistema

Abaixo o diagrama de um sistema que gosto muito: uma espécie de pêndulo vertical com base móvel obedecendo a um movimento periódico.

![diagrama-mec1-barra](/img/lagrangiana-em-movimento_diagrama-mec1-barra.png)

Na primeira vez que vi esse sistema o ângulo $\theta$ que a haste faz com a horizontal estava restrito ao intervalo de $-\frac{\pi}{2}$ a $\frac{\pi}{2}$, mas eu gosto da alternativa em que não existe essa barra vertical e o movimento é livre. Nesse caso o movimento do sistema seria mais ou menos assim:

![gif lagrangiana-em-movimento_diagrama-mec1-barra](/img/lagrangiana-em-movimento_diagrama-mec1-barra_opt.gif)

## espaço de coordenadas no tempo

$$ \begin{cases} x = R cos \theta \\ z = a sin (\omega t) = a sin (\omega t) + R sin \theta \end{cases} $$ 

<div style="height: 13em; overflow: scroll;">
```python
import matplotlib
import matplotlib.pyplot    as plt
import numpy                as np
import matplotlib.animation as animation

from mpl_toolkits.mplot3d import axes3d

#

Nfrm = 100
fps  = 10
fig  = plt.figure(figsize=(8,8))
ax   = fig.add_subplot(111, projection='3d')

R = 5
a = 3
w = 2

# meshgrid
theta   = np.linspace(0, 2*np.pi, 50)
xs      = R*np.cos(theta)
ys      = R*np.sin(theta)

# eixo z
ax.set_zlim(-1, 1)
ax.set_xlim(xs.min(), xs.max())
ax.set_ylim(ys.min(), ys.max())

# limpeza da figura
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])

# labels
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$z$')

# grafico e animacao
p = None
def update(idx):
    t = ts[idx]
    global p
    if p:
        p.remove()
    zs = a*np.sin(w*t) + ys
    p, = ax.plot(xs, zs, color='k')

ts  = np.linspace(0, 10, Nfrm)
ani = animation.FuncAnimation(fig, update, Nfrm, interval=1000/fps)

fn  = 'plot_configuration_space'
ani.save(fn+'.mp4',writer='ffmpeg',fps=fps)
ani.save(fn+'.gif',writer='imagemagick',fps=fps)
```
</div>

![gif plot_configuration_space](/img/lagrangiana-em-movimento_plot_configuration_space_opt.gif)

## lagrangiana no tempo

$$ \mathcal{L} = \frac{1}{2} m \left( R^2 \dot{\theta}^2 + a^2 \omega^2 cos^2 (\omega t) + 2 R a \omega cos (\omega t)cos \theta \dot{\theta} \right) - m g ( a sin (\omega t) + R sin \theta )$$

<div style="height: 13em; overflow: scroll;">
```python
import matplotlib
import matplotlib.pyplot    as plt
import numpy                as np
import matplotlib.animation as animation

from mpl_toolkits.mplot3d import axes3d

#

Nfrm = 100
fps  = 10

def L(q, qdot, t):
    m = 2
    R = 6
    w = 2
    a = 3
    g = 9.8
    
    T = 0.5*m*( qdot**2 * R**2 +\
                a**2 * w**2 * np.cos(w*t)**2 +\
                2*R*a*w*np.cos(w*t)*np.cos(q)*qdot )
    V = m*g*( a*np.sin(w*t) + R*np.sin(q) )
    
    return T - V

fig = plt.figure(figsize=(8,8))
ax  = fig.add_subplot(111, projection='3d')

# meshgrid
xs = np.linspace(-5, 5, 50)
ys = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(xs, ys)

# eixo z
ax.set_zlim(-1, 1200)

# limpeza da figura
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.set_xticks([]) 
ax.set_yticks([]) 
ax.set_zticks([])

# labels
ax.set_xlabel(r'$\theta$')
ax.set_ylabel(r'$\dot{\theta}$')
ax.set_zlabel(r'$\mathcal{L}$')

# grafico e animacao
wframe = None
Z      = L(X, Y, 0)
def update(idx):
    t = ts[idx]
    global wframe
    if wframe:
        ax.collections.remove(wframe)
    Z      = L(X, Y, t)
    wframe = ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, color='k', linewidth=0.5)

ts  = np.linspace(0, 50, 100)
ani = animation.FuncAnimation(fig, update, Nfrm, interval=1000/fps)
fn  = 'plot_lagrangian'
ani.save(fn+'.mp4',writer='ffmpeg',fps=fps)
ani.save(fn+'.gif',writer='imagemagick',fps=fps)
```
</div>

![gif lagrangiana-em-movimento_plot_lagrangian_opt](/img/lagrangiana-em-movimento_plot_lagrangian_opt.gif)
