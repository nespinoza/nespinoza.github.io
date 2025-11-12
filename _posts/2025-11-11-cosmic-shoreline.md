---
layout: post
title: "The Cosmic Shoreline concept via orders of magnitude"
date: 2025-11-11
---

As part of my visit to Columbia University's [Department of Astronomy](https://www.astro.columbia.edu/), on which I had the privilege to be the external examiner for ---now Dr.--- [Ben Cassese's](https://ben-cassese.github.io/) absolutely fantastic PhD thesis defense, I was given the chance to deliver a 15 min "pizza lunch chalkboard talk" about _anything_ I wanted. While my initial thought was to talk about how cool it is I can travel by train to New York from Baltimore (as a matter of fact, I'm writing this _in the train back_!), I decided to talk about rocky exoplanet atmospheres instead. 

To kickstart the talk, I did a little order-of-magnitude calculation motivated by the now seminal [Zahnle & Catling (2017)](https://arxiv.org/abs/1702.03386) paper on the "_Cosmic Shoreline_" that I wanted to replicate here --- mostly as a reminder to myself, but also to share it with the world. 

When starting the quest for detecting rocky exoplanet atmospheres, the first question one asks is where to start looking. Whether there is an atmosphere or not on an (exo)planet will depend strongly on the mass loss rate of that object, $\dot{M}$. Make this high, you likely will have no atmosphere at the end. Make it small, maybe replenishment wins and you have a steady atmosphere. This term, in turn, can be estimated as:

$$\dot{M} \sim \left(\textnormal{Input energy rate}\right) / \left(\textnormal{Binding energy per unit mass}\right).$$

In an energy-limited regime, the first term can be estimated as the energy being captured by the planet from the star. If we call the incident energy per unit area and time at the planet's location $I$ (the so called "instellation"), then the input energy rate at the planet location is:

$$\left(\textnormal{Input energy rate}\right) \sim \epsilon I\pi R_p^2,$$

where $R_p$ is the planetary radius and $\epsilon$ is an efficiency factor accounting for the actual fraction of energy that makes it into the planet (e.g., accounting for the fact some energy might be reflected back, or that the planet might not be as efficient capturing this energy as it could for some other reason). The second term, the binding energy (per atmospheric mass unit) is simply given by the gravitational potential of the planet itself, that is

$$\left(\textnormal{Binding energy per unit mass}\right) \sim G M_p/R_p.$$

Together, this gives

$$\dot{M} \sim \epsilon \frac{I \pi R_p^3}{GM_p}.$$

Now, given a timescale $t$, the total mass that is lost to space would be of order $t\dot{M}$. If this is larger than the total atmospheric mass, $M_{atm}$, then your atmosphere is lost. If we assume that this atmospheric mass is a fixed fraction of the total planet mass, $M_{atm} \sim f M_p$, this gives rise to the inequality

$$ t\dot{M} \gtrsim fM_p$$

for atmospheric loss. This gives, replacing our expression for $\dot{M}$ and solving for $I$,

$$ I \gtrsim \frac{f}{\epsilon} \frac{G}{\pi} \frac{M_p^2}{R_p^3}.$$

The key insight is that the right-hand side of this equation are all planetary parameters at heart. The left-hand side is, in principle, all about the star for a planet at a fixed distance from it. Now, let's rewrite the right-hand side only in terms of the escape velocity, $v_{esc} = GM_p/R_p$ and the planetary density, $\rho_p = (3/4 \pi ) M_p/R_p^3$. Noting that

$$v_{esc}^3 = \left(2G\right)^{3/2} \frac{M_p^{3/2}}{R_p^{3/2}},$$

and that,

$$\sqrt{\rho_p} = \sqrt{\frac{3}{4\pi}} \frac{M_p^{1/2}}{R_p^{3/2}},$$

we see the term $v_{esc}^3 \sqrt{\rho_p}$ is proportional to $M_p^2/R_p^3$. We can thus replace this in our expression for $I$ to get the boundary for atmospheric loss as

$$ I \propto v_{esc}^3 \sqrt{\rho_p}.$$

In my chalkboard talk, I jumped directly to this once I derived the first expression for $I$ (and noted that this should really be $I_{XUV}$). This is exactly the power-law relationship [Zahnle & Catling (2017)](https://arxiv.org/abs/1702.03386) derive in their paper --- with, of course, more assumptions (and perhaps a tad of intuition?) in our end. As they note in their paper, the actual (hand-drawn) relationship observed for the Solar System planets is actually $I \propto v_{esc}^4$ --- which is the mistery a lot of us are trying to uncover with actual observations of exoplanets, to see if the same holds elsewhere! This is one of the motivations for the [Rocky Worlds DDT program itself](https://rockyworlds.stsci.edu/).

It was cool to see how people, after understanding the assumptions, got really interested on the subject (which I then pivoted to our [TRAPPIST-1 results](https://ui.adsabs.harvard.edu/abs/2025ApJ...990L..52E/abstract) and [upcoming observations](https://www.stsci.edu/jwst-program-info/download/jwst/pdf/6456/)). When I've seen this relationship discussed, I think the point of the underlying physics (modulo all the assumptions!) gets typically lost, which is why I think order of magnitude calculations like these are very helpful to put everyone on an equal footing for discussion.

Thanks to [David Kipping](https://www.astro.columbia.edu/content/david-kipping) and Columbia University's Department of Astronomy for the invitation to chat briefly about this! Had a lot of fun. The Department is awesome and vibrant. The pizza was great. And I also love chalkboard talks. Mainly because I love chalkboards!
