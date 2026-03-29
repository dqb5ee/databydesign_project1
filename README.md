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

## Data Creation

The raw data for this project was synthesized from two primary state-level repositories to correlate environmental conditions with historical wildfire behavior in Southern California. The foundational dataset consists of Live Fuel Moisture (LFM) observations sourced from the National Fuel Moisture Database (NFMD) and the CAL FIRE Vegetation Sampling Program. This data represents field-collected "ground truth" measurements from 28 specific sampling sites across the Southern California coastal range (including Los Angeles, Ventura, and Santa Barbara counties). These measurements are taken by clipping live vegetation (primarily chamise and sage scrub), weighing it before and after oven-drying, and calculating the percentage of water content relative to dry biomass. This dataset provides the physiological "red line" necessary to understand the landscape's readiness for ignition.

To evaluate the impact of these moisture levels on actual disaster events, I acquired the California Historic Wildfire Perimeters (Firep24_1) dataset from the CAL FIRE Fire and Resource Assessment Program (FRAP). This GIS-based dataset contains the spatial boundaries and metadata for all recorded wildfires in California since 1878, including the "Alarm Date" and total "GIS Calculated Acres." By filtering these perimeters for the Southern California units that match the geographic coordinates of the LFM sampling sites, I was able to cross-reference the exact fuel moisture percentage present on the day of major fire ignitions. This dual-source acquisition process allows the project to move beyond general weather patterns and pinpoint the specific biological thresholds that lead to explosive fire growth.


| File Processed | Description | Code File Hyperlinked |
| :--- | :--- | :--- |
| `lfmc_observations.csv` | Aggregates 10,000+ field samples into a monthly regional baseline to establish the "Landscape Reservoir" levels for Southern California. | [`process_lfmc.py`](https://github.com/dqb5ee/databydesign_project1/blob/main/code/process_lfmc.py) |
| `California_Historic_Fire_Perimeters.csv` | Merges two statewide GIS record chunks and filters for Southern California Unit IDs and major ignition events (>10k acres). | [`filter_fires.py`](https://github.com/dqb5ee/databydesign_project1/blob/main/code/filter_fires.py) |
| `fire_moisture_master.csv` | The integrated dataset used for the threshold analysis and final visualization. | [`fire_moisture_master.py`](https://github.com/dqb5ee/databydesign_project1/blob/main/code/fire_moisture_master.py) |
| **Correlation Model** | Performs a relational join to map historical fire ignitions to the corresponding fuel moisture percentage recorded at the time of alarm. | [`correlation_model.py`](https://github.com/dqb5ee/databydesign_project1/blob/main/code/correlation_model.py) |


This table contains the original data file found online, a description of what it is and how the script edits it, and then a link to the script in a GitHub repository that edits it to the version I used it in.


Bias could have been/was introduced into the data collection process primarily through spatial selection and reporting thresholds. Live Fuel Moisture (LFM) sampling sites are fixed and often located near accessible roads or fire breaks for technician safety. This roadside bias means the data captures vegetation exposed to different micro-climates and stress factors, such as asphalt heat reflection, rather than interior canyon brush. Additionally, site distribution is heavily weighted toward the Wildland-Urban Interface (WUI), making the model more accurate for populated canyons than remote wilderness areas. Further, the CAL FIRE perimeter data is subject to reporting bias for smaller historical events. By focusing this project on fires over 10,000 acres, a success bias is introduced where the model identifies the threshold for catastrophic growth rather than simple ignition, meaning it does not account for the thousands of small starts that occur when moisture is high but fail to spread, which can be just as harmful to smaller areas. Finally, the discrete bi-weekly or monthly sampling of LFM creates a temporal lag where the moisture level at ignition is an estimate that may miss rapid drying trends caused by offshore wind events.


To make sure the "Santa Ana Threshold" is a reliable predictor, the analysis uses statistical aggregation and strategic filtering to account for identified biases. To mitigate roadside bias and non uniformed sensor distribution, the model uses a regional monthly baseline that aggregates data from 28 distinct sites. This smoothing process helps prevent localized micro-climate anomalies from individual sensors from skew the broader representation of the canyon landscape's moisture levels. Also, the analysis handles success bias by using a 10,000 acre filter, which shifts the study from simple ignition to catastrophic spread. This allows the model to quantify the specific conditions where fuel moisture is low enough to make standard fire suppression ineffective. Lastly, the temporal lag between field samples is mitigated by aligning ignitions with monthly regional trends to make sure the model captures the overall landscape dryness rather than relying on potentially outdated discrete samples.


The model is built on prioritizing public safety over spatial precision in some instances. A major judgment call was setting the 75% moisture threshold, which is a more conservative "early warning" limit that marks conditions high risk before they reach the normal 60% critical state. While this increases the potential for false positives, it also makes sure that the model identifies the onset of the ignition window rather than just the height of a disaster. Similarly, the decision to use a regional monthly baseline (aggregating data from 28 distinct sites) mitigates the high uncertainty that comes with localized sensors and roadside climate anomalies. This assumes that fire risk is a landscape level phenomenon requiring a regional signal for effective decision making. Finally, the use of a 10,000-acre filter intentionally isolates suppression resistant fire behavior, removing the noise of varying fire department response times to focus only on the biological conditions that allow for uncontrollable spread.

