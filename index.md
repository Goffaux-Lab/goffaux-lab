---
---
<p style="text-align:center"> Goffaux Lab </p>

<p style="text-align:center"> Short overall description about what our lab does </p>

{% include section.html %}

## Highlights

{% capture text %}

very short description of SF prong of our research

{%
  include button.html
  link="SF"
  text="Read more"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="SF"
  title="Spatial frequency processing"
  text=text
%}

{% capture text %}

very short description of Orientation prong of our research

{%
  include button.html
  link="tools"
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
