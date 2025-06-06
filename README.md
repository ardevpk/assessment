# NHANES Cholesterol Distribution Analysis

This project analyzes cholesterol distribution data from the National Health and Nutrition Examination Survey (NHANES) dataset, specifically focusing on males aged 55.

## Overview

The analysis visualizes the distribution of total cholesterol levels in males aged 55 using NHANES data. The visualization includes a histogram with kernel density estimation and highlights the 184 mg/dL cholesterol reference line.

## Data Sources

The project uses two NHANES datasets in XPT (SAS transport) format:

### 1. Total Cholesterol Laboratory Data (`data/tchol.xpt`)
- **Source**: NHANES Laboratory Data - Total Cholesterol
- **Key Variables**:
  - `SEQN`: Respondent sequence number (unique identifier)
  - `LBXTC`: Total cholesterol in mg/dL
- **Size**: ~253KB

### 2. Demographics Data (`data/demo.xpt`)
- **Source**: NHANES Demographics Data
- **Key Variables**:
  - `SEQN`: Respondent sequence number (unique identifier)
  - `RIDAGEYR`: Age in years at screening
  - `RIAGENDR`: Gender (1 = Male, 2 = Female)
- **Size**: ~2.5MB

## Requirements

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

### Dependencies
- `numpy` - Numerical computing
- `matplotlib` - Plotting library
- `scipy` - Scientific computing (includes SAS file reading capabilities)
- `seaborn` - Statistical data visualization

## Usage

Run the analysis script:

```bash
python main.py
```

The script will:
1. Load and merge the cholesterol and demographics datasets
2. Filter data for males aged 55
3. Generate a histogram showing cholesterol distribution with percentage on y-axis
4. Add a reference line at 184 mg/dL
5. Display the plot

## Analysis Details

- **Population**: Males aged 55 years
- **Measurement**: Total cholesterol levels (mg/dL)
- **Visualization**: Histogram with kernel density estimation
- **Reference Line**: 184 mg/dL (marked in red)
- **Output Format**: Percentage distribution

## Quick Results Preview

For a quick view of the analysis results without running the code, check the `results/` folder:

- **`results/cholesterol.png`**: Pre-generated visualization showing the cholesterol distribution for males aged 55

This allows you to quickly preview the analysis output before setting up the environment or running the code yourself.

## File Structure

```
.
├── main.py                     # Main analysis script
├── requirements.txt            # Python dependencies
├── data/
│   ├── tchol.xpt              # NHANES total cholesterol data
│   └── demo.xpt               # NHANES demographics data
├── results/
│   └── cholesterol.png        # Pre-saved visualization
└── README.md                  # This file
```

## Data Notes

- The NHANES data is publicly available from the CDC
- XPT files are SAS transport format files commonly used for NHANES datasets
- Missing cholesterol values are automatically excluded from the analysis
- The 184 mg/dL reference line represents a commonly used cholesterol threshold

## Output

The script generates:
1. An interactive plot display
2. Statistical visualization showing the percentage distribution of cholesterol levels

## About NHANES

The National Health and Nutrition Examination Survey (NHANES) is a program of studies designed to assess the health and nutritional status of adults and children in the United States. The survey combines interviews and physical examinations and is conducted by the Centers for Disease Control and Prevention (CDC).
