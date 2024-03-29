---
title: Spatial Frequency Integration
---
# Spatial Frequency Integration

Spatial frequencies (SF) refer to the different spatial resolutions composing an image, with low SF depicting the coarse structure of the image and higher SF representing its finest details. Natural images exhibit luminance variations aligned across a broad SF spectrum. Coarse-to-fine theories of vision propose that the coarse information carried by the low spatial frequencies (LSF) of visual input guides the integration of finer, high spatial frequency (HSF) detail. 

{% include section.html
  size=wide %}
  
{% capture sf_description1 %}
  Using functional resonance imaging (fMRI), we disrupted the processing of the coarse and fine content of full-spectrum human face stimuli via backward masking of selective SF ranges (LSFs: < 1.75cpd and HSFs: > 1.75cpd) at specific times (50, 83, 100 or 150 ms). In line with coarse-to-fine proposals, we found that <br> (1) the selective masking of stimulus LSF disrupted V1 activity in the earliest time window, and progressively decreased in influence, while <br> (2) an opposite trend was observed for the masking of stimulus’ HSF. <br> This pattern of activity was found in V1, as well as in ventral (i.e. the Fusiform Face area, FFA), dorsal, and orbitofrontal regions.
  {%
  include button.html
  type="article"
  link="https://doi.org/10.1016/j.neuroimage.2023.120139"
  text="Schuurmans et al., 2023"
  tooltip="Backward masking reveals coarse-to-fine dynamics in human V1"
  style="bare"
  %}
{% endcapture %}

{%
  include feature.html
  image="images/projects/SF/Schuurmans.png"
  link="images/projects/SF/Schuurmans.png"
  text=sf_description1
%}

{% include section.html 
  size=wide %}

{% capture sf_description2 %}
  We used multivariate decoding of EEG and MEG signals to separate the respective contribution of LSF and HSF to the neural response evoked by broad-band images. With both techniques, we found reduced HSF contribution when LSF was informative towards image content, indicating that coarse information does guide the processing of fine detail, in line with coarse-to-fine theories. <br> The reduction in HSF representational dominance was found in both early and higher-level visual areas and correlated with a reduction of gamma-band power in early visual cortex. <br> Our results indicate that the cross spatial frequency information redundancy that can be found in all natural images might be a driving factor in the efficient integration of fine image details.
  {%
  include button.html
  type="article"
  link="https://doi.org/10.1016/j.neuroimage.2018.10.086"
  text="Petras et al., 2019"
  style="bare"
  tooltip="Coarse-to-fine information integration in human vision"
  %}
  {%
  include button.html
  type="article"
  link="https://doi.org/10.1016/j.neuroimage.2021.118613"
  text="Petras et al., 2021"
  tooltip="Information redundancy across spatial scales modulates early visual cortical processing"
  style="bare"
  %}
{% endcapture %}

{%
  include feature.html
  image="images/projects/SF/PetrasImage.png"
  link="images/projects/SF/PetrasImage.png"
  text=sf_description2
  flip=true
%}

{% include section.html 
  size=wide %}
  Core aspects of face processing are primarily driven by the low spatial frequencies (SF) of the visual image. The processing of low SF information accounts for the early neurophysiological dissociation (N170) between face and object visual processing.
  {%
  include button.html
  type="article"
  link="https://doi.org/10.1016/S0926-6410(03)00056-9"
  text="Goffaux et al., 2003"
  tooltip="Spatial scale contribution to early visual differences between face and object processing"
  style="bare"
  %}
  
   <p style="text-align:center">  Low SF conveys the most essential cues for holistic/interactive face processing. </p>
  {%
  include button.html
  type="article"
  link="https://doi.org/10.1016/j.visres.2009.02.009"
  text="Goffaux et al., 2009"
  tooltip="Spatial interactions in upright and inverted faces: Re-exploration of spatial scale influence"
  style="bare"
  %}
  {%
  include button.html
  type="article"
  link="https://www.researchgate.net/publication/6940138_Faces_Are_Spatial-Holistic_Face_Perception_Is_Supported_by_Low_Spatial_Frequencies"
  text="Goffaux et al., 2006"
  tooltip="Faces Are “Spatial”—Holistic Face Perception Is Supported by Low Spatial Frequencies"
  style="bare"
  %}

  {% capture sf_description3 %}
  The FFA, a high-level visual region preferentially responding to faces, tunes to progressively higher SF ranges of face information over the course of visual processing, supporting coarse-to-fine recurrent models of vision. 
  {%
  include button.html
  type="article"
  link="https://doi.org/10.1093/cercor/bhq112"
  text="Goffaux et al., 2011"
  tooltip="From Coarse to Fine? Spatial and Temporal Dynamics of Cortical Face Processing"
  style="bare"
  %} 
{% endcapture %}

{% include section.html
  size=wide %}
{%
  include feature.html
  image="images/projects/SF/Project_SF022.gif"
  link="images/projects/SF/Project_SF022.gif"
  text=sf_description3
  %}
