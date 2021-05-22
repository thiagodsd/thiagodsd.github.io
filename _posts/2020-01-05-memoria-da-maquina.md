---
layout: text
title:  "memória da máquina"
description: anotações desordenadas sobre as periferias da inteligência artificial
img: /img/t_memoria-da-maquina.png
date:   2020-01-05 14:43:00 +0300
tags: aprendizagem-estatistica notas
---

Há algum tempo venho tentando entender de que se trata inteligência artificial. Até agora a única coisa razoavelmente clara é que essa entidade _Inteligência Artificial_ tem um monte de coisa dentro e cada uma dessas coisas recebe nomes diferentes quando vista de perspectivas diferentes. Muitas técnicas podem ser obtidas e entendidas a partir de múltiplos frameworks, seja _teoria da informação_, _otimização_, _estatística_, _teoria dos jogos_ ou mesmo _física_.

Como bom sujeito treinado em física, pensei em sistematizar algumas ideias seguindo a estrutura de princípios que combinados e usados com esperteza conduzem a resultados úteis. Porém o zoológico de ideias e técnicas é muito vasto e por isso me pareceu melhor maximizar a entropia e estruturar as coisas em pequenos fragmentos desordenados.

<br/><br/>

## o hello world do raciocínio probabilístico

<p class="topico">estatística</p>

Do ponto de vista estatístico ambas, regressão e classificação, podem ser pensadas como a busca pela aproximação de uma certa $f(y \| x, w)$ que relaciona o conjunto de propriedades $x$ de uma observação à chance $p$ de certa informação de interesse $y$ dessa observação possuir determinado valor.

Em uma regressão $y$ é uma variável contínua. No problema de classificação $y$ é discreta. Em particular $y \in \\{0, 1\\}$ dá origem a problemas de classificação binária.<br/>
Fundamentalmente essa função $f$ tal que $f(y \| x,w) \mapsto p$ nunca é completamente conhecida então há alguma liberdade na sua escolha. Desde um ponto de vista probabilístico as funções que compõem a chamada _família exponencial_ recebem atenção especial na tarefa de estimar $p$. Duas escolhas clássicas são

$$ \begin{cases}
p \sim \mathcal{N}(y|w^T \phi(x), \sigma^2) \qquad \text{(regressão)}         \nonumber \\
p \sim Bern\left( y | \frac{1}{1+e^{-w^T x}} \right) \quad \text{(classificação)} 
\end{cases} $$

## a regressão logística

<p class="topico">classificação</p>

Nos primórdios nada havia. Então surgiu a regressão linear. Muita gente boa debruçou sobre esse problema, dando origem a métodos como o dos mínimos quadrados.<br/>
A princípio os métodos de regressão só funcionam quando a variável de interesse $y$ -- ou _"target"_, ou _"variável resposta"_, ou _"variável dependente"_ -- é contínua.

A ideia na regressão logística é usar técnicas/algoritmos de regressão para resolver problemas de classificação. Daí a esquizofrenia da regressão logística -- um método de classificação com "regressão" no nome.

O truque é limitar o resultado da regressão no intervalo $\[0, 1\]$, para ter cara de probabilidade, e eventualmente definir um valor de probabilidade que separa as classes $0$ e $1$.

Há algumas funções que satisfazem essa necessidade, mas no lugar de sacar uma delas é interessante pensar no problema inverso: como levar algo de $[0,1]$ em $\mathbb{R}$?

Algo com a cara $\mathcal{F}(x) = \frac{1}{x}$ serve para levar para o infinito. Nesse caso:

$$\begin{cases}
\mathcal{F}(p=0) = \infty \nonumber \\
\mathcal{F}(p=1) = 1
\end{cases}$$

Um detalhe da $\mathcal{F}$ é que probabilidades altas levam a valores pequenos e vice-versa. Uma forma de acalmar os corações mais desesperados dos apostadores do mundo é construí-la como $\mathcal{F}(x) = \frac{1}{\frac{1}{x}-1}$, assim:

$$\begin{cases}
\mathcal{F}(p=0) = 0 \nonumber \\
\mathcal{F}(p=1) = +\infty
\end{cases}$$

Para atingir o outro infinito a $\mathcal{G}(x) = log(x)$ resolve:

$$\begin{cases}
\mathcal{G}(\mathcal{F}(p=0)) = -\infty \nonumber \\
\mathcal{G}(\mathcal{F}(p=1)) = +\infty
\end{cases}$$

Essas duas funções $\mathcal{F}(p)$ e $\mathcal{G}(\mathcal{F}(p))$ são chamadas por aí respectivamente de _**odds**_, ou "chance", e _**logit**_, que já vi chamarem de "logíto" também.<br/>
$\mathcal{G}(\mathcal{F}(p))$ leva _pseudo-probabilidades_ nos reais, então para para resolver um problema de classificação usando os métodos de regressão, basta aplicar $\mathcal{F}^{-1}(\mathcal{G}^{-1}(\cdot)) \equiv \sigma(\cdot)$ no resultado.<br/>
Essa inversa também tem nome: _**função sigmoide**_

$$ \sigma(x) = \frac{1}{1+e^{-x}} $$

<br/>

Com respeito ao modelo é interessante observar que os parâmetros de ajuste $w$ não são as probabilidades, senão os logitos. Como $p \sim \sigma(w^T x)$, então 

$$ \boxed{ w^Tx = log \left( \frac{p}{1-p} \right) } \label{reglog}$$


<br/>

Uma das hipóteses da regressão logística é que as observações são distribuídas de forma que $p(y=c) \sim Bern$, com $c \in \\{0, 1\\}$, ou seja

$$\begin{cases}
 Bern(y=1) = p   \nonumber \\
 Bern(y=0) = 1-p 
\end{cases}$$

À luz disso é interessante olhar pra $\mathcal{F}$ uma última vez:

$$\text{odds} = \frac{p}{1-p} = \frac{Bern(y=1)}{Bern(y=0)} = \frac{\text{evento}}{\neg\text{evento}} = \frac{p_+}{p_-} =  \frac{\sigma(w^T x)}{1-\sigma(w^T x)} = \frac{\sigma(w^T x)}{\sigma(-w^T x)}  \nonumber$$

<br/>
<p style="color: red; font-weight: 600;"> a partir daqui os parágrafos são rascunhos e esboços </p> 
<br/>

Do ponto de vista prático a $\ref{reglog}$ é a equação que caracteriza a regressão logística binária. Para


























## construção axiomática de kolmogorov

<p class="topico">probabilidade</p>

Dados eventos $A_1, A_2, \dots ,A_n \in \mathcal{A}$, disjuntos, em que $\mathcal{A}$ é uma $\sigma$-álgebra do conjunto $\Omega$, denotando $P(A_i)$ a probabilidade de $A_i$, segue uma função $P$ definida em $\mathcal{A}$ satisfazendo

A1. $P(A) \geq 0$

A2. $P(\Omega) = 1$

A3. $P \left( \bigcup_{n=1}^{\infty} A_n \right) = \sum_{n=1}^{\infty} P(A_n)$

é chamada **medida de probabilidade** em $\mathcal{A}$ e satisfaz as seguintes propriedades

P1. $P(A^c) = 1 - P(A)$

P2. $0 \leq P(a) \leq 1$

P3. $A_1 \subset A_2 \Rightarrow P(A_1) \leq P(A_2)$

P4. $P \left( \bigcup_{i=1}^{\infty} A_i \right) \leq \sum_{i=1}^{\infty} P(A_i)$

P5. $A_n \uparrow A \Rightarrow P(A_n) \uparrow P(A) \qquad e \qquad A_n \downarrow A \Rightarrow P(A_n) \downarrow P(A)$

<br/>

### probabilidade condicional

A probabilidade condicional do evento $A$ dada observação de $B$ pode ser definida como

$$P(A  \mid  B) = \frac{P(A \cap B)}{P(B)} \nonumber$$

expresando um resultado intuitivo: dados $n$ ensaios independentes de $A$ e $B$, no limite de $n \to \infty$ é razoável que

$$P(A \mid B) \sim \frac{1}{n} \left( \frac{\text{# ocorrências de A e B}}{\text{# ocorrências de B}} \right) \nonumber$$

Disso segue que

- $P(A \cap B) = P(B)P(A \mid B)$
- $P(A \cap B \cap C) = P(A)P(B \mid A)P(C \mid A \cap B)$

esse segundo resultando podendo ser generalizado para o **teorema da probabilidade composta**, onde vale que

$$P(A_1 \cap \dots \cap A_n) = P(A_1)P(A_2  \mid  A_1)P(A_3 \mid A_1 \cap A_2) \dots P(A_n  \mid  A_1 \cap \dots \cap A_{n-1}) \nonumber$$

Dada a disjuntividade dos $A_i$, um evento $B \in \mathcal{A}$ pode ser representado como 

$$B = \bigcup_i (A_i \cap B) \nonumber$$

consequentemente

$$P(B) = \sum_i P(A_i \cap B) = \sum_i P(A_i)P(B \mid A_i) \nonumber$$

<br/>

### fórmula de bayes

Combinando os resultados anteriores segue a fórmula de Bayes

$$ \boxed{ P(A_i  \mid  B) = \frac{P(A_i \cap B)}{P(B)} = \frac{P(A_i)P(B \mid A_i)}{\sum_j P(A_j)P(B \mid A_j)} } $$

### Exemplo 1 

Uma caixa contém duas moedas honestas e uma com duas caras. Lançando uma delas ao acaso e verificando que o resultado foi cara, qual é a probabilidade da moeda lançada ter sido a de duas caras?

Definindo

+ $A_1$ como moeda honesta
+ $A_2$ como moeda de duas caras
+ $B$ como resultado igual a cara

a probabilidade deseja é definida por $P(A_2  \mid  B)$. Pela fórmula de Bayes

$$P(A_2  \mid  B) = \frac{P(A_2)P(B \mid A_2)}{P(A_1)P(B \mid A_1) + P(A_2)P(B \mid A_2)} = \frac{\frac{1}{3}1}{\frac{2}{3}\frac{1}{2} + \frac{1}{3}1} = \frac{1}{2}$$

### Exemplo 2

Definindo o estado de saúde de uma pessoa como

+ $d=1$ a pessoa tem a doença $D$
+ $d=0$ a pessoa não tem a doença $D$

sabendo que um teste $T$ possui 95% de acurácia para detectar a doença em pacientes que de fato possuem a doença $D$, e que esse mesmo teste possui 95% de acurácia para detectar que pacientes saudáveis não possuem a doença $D$.

Se apenas 1% da população mundial possui a doença $D$, qual a chance de alguém obter positivo no teste $T$ e realmente ter a doença $D$?

Denotando por

+ $t=1$ o resultado do teste sendo positivo
+ $t=0$ o resultado do teste sendo negativo

seguem das informações de acurácia do teste que

+ $P(t=1  \mid  d=1) = 0.95$
+ $P(t=0  \mid  d=1) = 0.05$
+ $P(t=1  \mid  d=0) = 0.05$
+ $P(t=0  \mid  d=0) = 0.95$

e das informações da população mundial segue que

+ $P(d=1) = 0.01$
+ $P(d=0) = 0.99$

então a fórmula de Bayes mostra que

$$P(d=1  \mid  t=1) = \frac{P(t=1 \mid d=1)P(d=1)}{P(t=1 \mid d=1)P(d=1)+P(t=1 \mid d=0)P(d=0)} = 0.16$$

### Exemplo 3

![](../assets/img/img_urnas.png)

Dadas $11$ urnas $u=0, u=1, \dots, u={10}$, todas com $10$ bolas, sendo $u$ delas bolas pretas. Alguém escolhe uma das urnas ao acaso e realiza $N$ sorteios com reposição. Se após $N$ sorteios, $n_B$ bolas pretas foram obtidas, qual a probabilidade da urna $u$ ter sido a escolhida?

A probabilidade buscada é $$P(u  \mid  n_B, N)$$ ou seja, a probabilidade da urna $u$ ter sido escolhida, dado que das $N$ bolas, $n_B$ são pretas.

Pela fórmula de Bayes

$$P(u  \mid  n_B, N) = \frac{P(n_B  \mid  u, N)P(u  \mid  N)}{P(n_B  \mid  N)}.$$

$P(n_B  \mid  u, N)$ é a probabilidade de se obter $n_B$ bolas pretas dado que $N$ sorteios foram realizados na urna $u$. 
A probabilidade de sortear uma bola preta, na urna $u$, em um sorteio único é $$\frac{u}{10}$$ enquanto a probabilidade da bola sorteada não ser preta é $$\left(1 - \frac{u}{10} \right).$$

Em $N$ sorteios, a probabilidade de sortear $n_B$ bolas pretas é dada pelo produto

$$\left[ \left( \frac{u}{10} \right)\left( \frac{u}{10} \right) \dots \left(1 - \frac{u}{10} \right)\left(1 - \frac{u}{10} \right) \right]= \left( \frac{u}{10} \right)^{n_B}\left(1 - \frac{u}{10} \right)^{N-n_B}.$$

Como a ordem não importa, segue que

$$P(n_B  \mid  u, N) = \frac{N!}{n_B!(N-n_B)!}\left( \frac{u}{10} \right)^{n_B}\left(1 - \frac{u}{10} \right)^{N-n_B}.$$

$P(u  \mid  N)$ é a probabilidade de escolher a urna $u$ - que essencialmente não depende de N, portanto $$P(u  \mid  N)=P(u)=\frac{1}{11}.$$

$P(n_B  \mid  N)$ é a probabilidade marginal de $n_B$ - eventualmente chamada de _evidência_, uma vez que depende das informações dadas. Reescrevendo a evidência usando as _regra do produto_ e _regra da soma_:

$$P(n_B  \mid  N) = \sum_{u} P(n_B, u  \mid  N) = \sum_{u} P(n_B  \mid  u, N)P(u  \mid  N).$$

Então, finalmente

$$\boxed{ P(u  \mid  n_B, N) = \frac{1}{11}\frac{1}{P(n_B  \mid  N)} \frac{N!}{n_B!(N-n_B)!}\left( \frac{u}{10} \right)^{n_B}\left(1 - \frac{u}{10} \right)^{N-n_B}}$$

Visualizando a distribuição dados $N$ e $n_B$

```python
from math import factorial as fac
import matplotlib.pyplot as plt
%matplotlib inline

def comb(a,b):
    return  fac(a) / (fac(b)*fac(a-b))

def P(u, nb, N):
    marg = (1/11) * sum( [ comb(N, nb)*((U/10)**nb)*(1-(U/10))**(N-nb) for U in range(11) ] )
    return (1/11)*(1/marg)*comb(N, nb)*((u/10)**nb)*(1-(u/10))**(N-nb)

def g(sorteios, bolas_p):
    plt.bar( [i for i in range(11)], [P(j, bolas_p, sorteios) for j in range(11)], width=0.0005)
    plt.xlim([-0.5, 10.5])
    plt.title('Probabilidade de ser a urna u')
    plt.xticks([i for i in range(11)]);
    
def l(sorteios, bolas_p):
    L = []
    for i,v in enumerate([j for j in range(11)]):
        L.append(float('{:.7f}'.format(P(v, bolas_p, sorteios))))
    return L
```

Por exemplo $N=10, n_B=6$:

```python
g(10,6)
```


![](../assets/img/out_0000.png)

Visualizando a distribuição em toda sua extensão

```python
plt.figure(figsize=(12,9))
plt.imshow([l(10, i) for i in range(11)], interpolation='nearest')
plt.colorbar()
plt.title('Probabilidade')
plt.ylabel('u')
plt.xlabel('nb')
plt.yticks([i for i in range(11)]);
plt.xticks([i for i in range(11)]);
```


![](../assets/img/out_0001.png)



<br/><br/>

# referências

<div class="tex2jax_ignore">
</div>
