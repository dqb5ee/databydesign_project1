# DS 4320 Project 1: Finding the Arid Edge
### Optimizing Live Fuel Moisture Thresholds for Southern California Wildfire Readiness

Executive Summary: Short paragraph explaining the contents of the respository in executive form

Name: Avalon Bennett

NetID: dqb5ee

DOI:

Press Release

Data

Pipeline

License


## Problem Definition

General Problem: Predicting Wildfire Risk

Refined Statement: Rather than relying on numerous "High Fire Danger" alerts, this project seeks to identify the "Santa Ana Threshold" to give a more informed risk alert in specific locations. By defining this "Red Line," we can distinguish between routine wind events and "Flash Fire" windows, providing a specific data signal for when the landscape is physically primed for catastrophic ignition and residents actually need to prepare.


The refinement from prediction to identifying thresholds is necessary to defend against an immense amount of alerts in Southern California. General wind warnings are common, but they only result in catastrophic fires when the fuel state has crossed a physiological threshold of dryness. By focusing on the "Santa Ana Threshold," we move away from broad meteorological guesswork and toward a specific, evidence-based trigger. This approach allows us to ignore the "noise" of typical windy days and focus exclusively on the high-stakes windows where people actually need to prioritize satefy because the air's "thirst" makes a community-destroying that much more probable.


The motivation for this project is the increasing vulnerability of Southern California’s Wildland-Urban Interface (WUI). As urban development pushes further into the foothills, the margin for error during Santa Ana wind events has disappeared. Recent events, such as the Palisades and Eaton fires, demonstrate that the difference between a manageable brush fire and a neighborhood-wide disaster is often found in the moisture levels of the vegetation. This project is motivated by a desire to provide WUI communities and emergency responders with a clearer "Vision" of danger—moving from "gut feelings" about the wind to a hard "Red Line" in the data that can save lives and property.


Press Release Headline: From Wind Gusts to Data Signals: Pinpointing the 'Santa Ana Threshold' to Get Ahead of Wildfires in Southern California Canyons

[Jump to Press Release](#press-release-link)


## Domain Exposition

| Category | Term | Definition / Significance | KPI Type |
| :--- | :--- | :--- | :--- |
| **Atmospheric** | **Santa Ana Winds** | Strong, dry downslope winds from the Great Basin that accelerate through southern Californian (SoCal) canyons. These are the primary "Training Load" for fire spread. | **Input Variable** |
| **Atmospheric** | **Vapor Pressure Deficit (VPD)** | Measure of the air's lack of moisture. High VPD indicates the atmosphere is pulling moisture out of the vegetation to rehydrate. | **Predictive KPI** |
| **Biological** | **Live Fuel Moisture (LFM)** | Percentage of water content in living plants (Chaparral). LFM < 60% is a critical indicator of  where the landscape becomes explosive. | **Biological KPI** |
| **Geospatial** | **Wildland-Urban Interface (WUI)** | High stakes zone where human development meets flammable natural vegetation. | **Spatial Metric** |
| **Geospatial** | **Slope Aspect** | Compass direction a slope faces. South facing slopes in SoCal receive more solar radiation and dry out faster. | **Topographic Variable** |
| **Regulatory** | **FHSZ (Fire Hazard Severity Zones)** | Classifications (Moderate, High, Very High) assigned by CAL FIRE based on fire history and vegetation density. | **Benchmark Metric** |
| **Operational** | **Ignition Window** | Specific intersection of high wind, low humidity, and low fuel moisture where a "flash fire" is nearly guaranteed if a spark occurs. | **Primary Output** |
| **Weather** | **Relative Humidity (RH)** | Amount of water vapor in the air. During Santa Ana events, RH levels in SoCal can drop to dangerously low single digits (<10%). | **Input Variable** |


This project lives at the intersection of Environmental Data Science and Public Safety Analytics. Specifically, it focuses on the domain of Wildfire Risk Modeling, which is a field that combines meteorology, botany (fuel science), and geospatial physics to predict the behavior of natural disasters. Unlike traditional fire response, which focuses on putting out after a fire after it has started, this domain focuses on pre-emptive risk identification. By analyzing historical fire perimeters alongside real-time atmospheric "load" (wind and humidity) and biological "readiness" (fuel moisture), we can treat a landscape like a monitored system. In the context of Southern California, this domain is specialized to account for the unique "Santa Ana" weather patterns and the complex topography of the Wildland-Urban Interface (WUI), where human infrastructure directly overlaps with fire-prone ecosystems.

The following table summarizes some foundational research and articles used to define the domain and technical approach for this project. These resources cover the atmospheric drivers of SoCal fires, machine learning methodologies, challenges of evidence-based environmental regulation, and personal accounts of the destruction of these fires.

| Title | Description | Read More |
| :--- | :--- | :--- |
| **Can data science achieve the ideal of evidence-based decision-making?** | Explores the limitations and opportunities of using Big Data in environmental regulation, emphasizing the need for spatial and temporal specificity. | [Link](#https://drive.google.com/file/d/1b-XiXXpzG19eBS3i31tU5qqhtIN_nYY_/view?usp=sharing) |
| **Wildfire Risk Modeling** | Comprehensive overview of current methods in wildfire risk assessment, focusing on causation and the integration of machine learning to develop predictive models. | [Link](#https://drive.google.com/file/d/1-9tWExGuPs1UcbNYFz9Rw8n2oMnD6vQq/view?usp=sharing) |
| **Machine Learning Algorithms Applied to Wildfire Data** | Technical study comparing different ML algorithms to predict wildfires, providing a baseline for the predictive side of this tool. | [Link](#https://drive.google.com/file/d/1ZMZgg13yV6a7NPapeAgL9KybF6AYP0SI/view?usp=share_link) |
| **How Santa Ana Winds Fueled the Deadly Fires in SoCal** | Explains the specific meteorological phenomenon of Santa Ana winds and how topography and "the atmosphere's thirst" create the breeding grounds for extreme fire spread in the region. | [Link](#https://drive.google.com/file/d/1Qof0sO0DiIM5gPzLRJ9YZfGPjr2HWTYm/view?usp=sharing) |
| **The Impact of the Southern California Fires** | Blog post detailing the socio-economic and human costs of recent fires (like in the Pacific Palisades), emphasizing the need for better early warning systems. | [Link](#https://drive.google.com/file/d/1Wc51ZfeJ8zaVdD3cVXkk2eg-YCG-tLKT/view?usp=sharing) |

[Link to the folder.](#https://drive.google.com/drive/folders/11-r02cnrSotbQbwu6KsYLgSbQv2nI7pR?usp=share_link)

