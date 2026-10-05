# Candidate AR Interaction and Guidance Ontology

## Interaction representation

Represent an interaction instance as:

`I = (Task, Input, Fusion, Target, Feedback, Guidance, Context, User, Metric)`

### Task
selection; manipulation; navigation/locomotion; system control; text/data entry; annotation; communication/collaboration; authoring.

### Input modality
touch; controller/button; gesture/hand; gaze/head; speech/voice; tangible/physical object; body/posture; pen/stylus; physiological/BCI; environmental/context sensing.

### Fusion
unimodal; sequential multimodal; complementary multimodal; redundant multimodal; adaptive/context-selected modality.

### Feedback/output
visual; auditory; haptic/tactile; spatial/projected; multimodal.

### Guidance/attention
in-view highlighting; world-fixed cue; screen/viewport-fixed cue; directional cue; distance encoding; reference line; subtle/peripheral cue; feedback-on-progress.

## Comparability rule
Interaction techniques are candidates for comparison only when **task + input/fusion + target/context + feedback/guidance + user population + metric** are sufficiently aligned.

A gesture-selection study and a speech-system-control study are not comparable merely because both use a HoloLens.

## Literature lineage
- Zhou et al. 2008: historical ISMAR tracking/interaction/display roadmap.
- Hertel et al. 2021: 44-paper immersive-AR taxonomy centered on task and modality.
- Bai et al. 2025: 16 studies specifically integrating gesture and speech/multimodal interaction.
- Hughes & Karwowski 2025: interaction implementation linked to UX evaluation across 86 studies.
- Quinn & Gabbard 2024: attention guidance for out-of-view objects requires visualization-characteristic coding.

## Candidate research implication
The meaningful unit is not “interaction method” alone but **interaction configuration under a task and context**. This prevents false rankings of modalities across incompatible tasks.
