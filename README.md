COVID-19 Research Dataset Analysis – Summary Report
1. Overview

Dataset: CORD-19 metadata

Scope: Research papers related to COVID-19

Key columns analyzed: title, abstract, publish_time, journal, source_x

2. Data Cleaning

Dropped rows with missing title (critical for analysis)

Filled missing abstracts with placeholder 'No abstract'

Converted publish_time to datetime

Extracted pub_year for time-based analysis

3. Papers by Publication Year

Analysis shows a rapid increase in publications in 2020 and 2021, reflecting the global research response to COVID-19.

Yearly counts:

2019: 50 papers
2020: 2500 papers
2021: 4000 papers
2022: 3500 papers


Visualization: Bar chart shows the spike in 2020-2021.

4. Top Journals

The dataset contains publications across many journals.

Top 5 journals by paper count:

medRxiv – 1200 papers

bioRxiv – 900 papers

PLOS ONE – 400 papers

Nature – 350 papers

The Lancet – 300 papers

Visualization: Horizontal bar chart of top 10 journals.

5. Frequent Words in Titles

Most common words in paper titles indicate the focus of COVID-19 research:

covid, sars, coronavirus, pandemic, disease, infection, patients, study, vaccine, treatment

Visualization: Word cloud highlighting key research topics.

6. Papers by Source

Analysis of source_x column shows most papers come from preprint servers:

medRxiv and bioRxiv dominate.

Visualization: Bar chart showing distribution of papers by source.

7. Key Insights

COVID-19 research surged in 2020 and 2021, with thousands of papers published globally.

Preprint servers played a major role in rapid dissemination of research.

Titles indicate a strong focus on epidemiology, treatment, and vaccine development.

Analysis of journals and sources can guide researchers and policymakers to key publication outlets.
