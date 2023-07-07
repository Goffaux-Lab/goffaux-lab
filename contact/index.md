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
  text="Phone number" 
  link=" +32(0)10473877" 
%} 

{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://goo.gl/maps/z4Y6H3Se6YukUR6C9"
%}

{% include section.html %}


{%
  include figure.html
  image="images/lln1.jpg"
%}

{% capture col1 %}
<center>
Our visiting address:
Faculty of Psychology and Educational Sciences <br>
Université Catholique de Louvain <br>
Place Cardinal Mercier 10 <br>
Third floor, Hall D, Room D-319 <br>
1348 Louvain-la-Neuve <br>
Belgium  </center>
{% endcapture %}

{% capture col2 %}
<center>
Our postal address:
Faculty of Psychology and Educational Sciences <br>
Université Catholique de Louvain <br>
Place Cardinal Mercier 10 box L3.05.01 <br>
1348 Louvain-la-Neuve <br>
Belgium  </center>
{% endcapture %}

{%
  include cols.html
  col1=col1
  col2=col2
%}

{%
  include figure.html
  image="images/logos_affiliation.gif"
%}

{% include cols.html col1=col1 col2=col2 %}
