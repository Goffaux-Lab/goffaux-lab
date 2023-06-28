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

{% include list.html data="members" component="portrait" filters="role: ^(?!pi$)" %}

# {% include icon.html icon="fa-solid fa-users" %}Alumni

{% include section.html %}

{% include list.html data="alumni" component="portrait" filters="role: alumni" %}
