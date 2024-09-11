---
title: Team
nav:
  order: 4
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

{% include section.html %}

{% include list.html data="members" component="portrait" filters="role: pi" %}

{% include list.html data="members" component="portrait" filters="role: ^(?!pi$), role: ^(?!alumni$)" %}

# {% include icon.html icon="fa-solid fa-users" %}Alumni

{% include section.html %}

<!-- Postdoctoral Researchers -->
{% include list.html data="members" component="portrait" filters="role: alumni, description: ^(Postdoctoral Researcher|Visiting Postdoctoral Researcher)$" %}

<!-- PhD Candidates -->
{% include list.html data="members" component="portrait" filters="role: alumni, description: ^(PhD|PhD Candidate|Visiting PhD Candidate)$" %}

<!-- Other Alumni -->
{% include list.html data="members" component="portrait" filters="role: alumni, description: ^(?!Postdoctoral Researcher$|Visiting Postdoctoral Researcher$|PhD|PhD Candidate$|Visiting PhD Candidate$)" %}
