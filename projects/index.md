---
title: Projects
nav:
  order: 2
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

All publications listed (with a representative picture)
Search engine: seach by keywords, last name of author and separate selection button for date


{% include search-info.html %}

{% include section.html %}

## Featured

{% include list.html component="card" data="projects" filters="group: featured" %}

{% include section.html %}

## More

{% include list.html component="card" data="projects" filters="group: " style="small" %}
