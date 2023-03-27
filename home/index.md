---
title: Home
nav: 
  order: 1
  tooltip: About us
---
---

# Goffaux Lab

Short overall description about what our lab does
{% include section.html %}

## Highlights

{% capture text %}

very short description of SF prong of our research

{%
  include button.html
  link="research/spatial_frequency"
  text="Read more"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research/spatial_frequency"
  title="Spatial frequency processing"
  text=text
%}

{% capture text %}

very short description of Orientation prong of our research

{%
  include button.html
  link="research"
  text="Read more"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Orientation processing"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

very short description of CM prong of our research

{%
  include button.html
  link="research"
  text="Read more"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title="Contextual modulation"
  text=text
%}
