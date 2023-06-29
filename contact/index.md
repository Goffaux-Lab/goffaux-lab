---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

{%
  include button.html
  type="email"
  text="Email us"
  link="goffauxlab@gmail.com"
%}

{% 
  include button.html 
  type="phone" 
  text="Phone" 
  link=" +32(0)10473877" 
%} 

{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://goo.gl/maps/z4Y6H3Se6YukUR6C9"
%}

{% include section.html %}

Our visiting address: 
Faculty of Psychology and Educational Sciences
Université Catholique de Louvain
Place Cardinal Mercier 10
Third floor, Hall D, Room D-319
1348 Louvain-la-Neuve
Belgium


{%
  include figure.html
  image="images/lln1.jpg"
  caption="Lorem ipsum"
%}

{% include section.html %}

{%
  include figure.html
  image="images/logos_affiliation.gif"
  caption="Lorem ipsum"
%}

{% include cols.html col1=col1 col2=col2 %}
