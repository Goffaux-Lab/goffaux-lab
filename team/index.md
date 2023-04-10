---
title: Team
nav:
  order: 4
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

decribe the team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)" %}

{% include grid.html style="square" content=content %}
