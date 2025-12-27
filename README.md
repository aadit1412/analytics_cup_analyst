## Modelling Defensive Pressure Conversion into Possession Disruption | Abstract
#### Introduction

Defensive pressure is widely acknowledged as a key mechanism through which teams disrupt opposition possession, yet quantifying how pressure translates into actual possession loss remains an open challenge. This project introduces a spatiotemporal framework that links defensive pressure intensity to short-horizon possession disruption, using tracking data and phase-of-play context. Rather than evaluating pressure as an isolated action, the model focuses on its **conversion efficiency**, the probability that pressure leads to a turnover within a defined temporal window.

#### Usecase(s)

Defensive pressure is estimated using arrival-time–based influence functions, where each defender’s contribution decays exponentially with time-to-ball. Individual influences are aggregated at the frame level and standardised within a match. Disruption is defined as a change in possession occurring within three seconds (30 frames at 10 FPS).  

By analysing the relationship between pressure intensity and disruption probability, the framework produces **pressure–disruption curves** that describe how marginal increases in pressure affect turnover likelihood. These curves are further segmented by defensive phase (e.g. high block, low block, chaotic defending), enabling phase-specific interpretation of pressure effectiveness. The framework can be used to:

- Evaluate whether increasing pressure yields diminishing or accelerating returns  
- Compare defensive phases based on pressure efficiency rather than volume  
- Identify tactical contexts where pressure is most likely to force turnovers

#### Potential Audience

This work is relevant for professional analysts, recruitment and performance departments, and researchers interested in possession dynamics, defensive tactics, and applied spatiotemporal modelling. It is particularly suited to teams seeking interpretable metrics that connect defensive behaviour to match outcomes, rather than standalone pressure counts.

## Video URL

https://youtu.be/vm-nh2vJyKQ

## Run Instructions

Run `submission.ipynb` in a clean environment. All helper functions are imported from the `src/` directory. Tracking data is loaded directly from the SkillCorner Open Data repository.
